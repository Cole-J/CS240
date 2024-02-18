'''
Cole Johnson 2/15
For CS2
'''
# import time for speed control
import time
# import os for terminal control
import os

class TOWER_OF_HANOI:
    def __init__(self, num_discs = 3, start_peg = 'A', target_peg = 'B', aux_peg = 'C'): # O(1)
        self.num_discs = num_discs
        self.moves = []  # Store moves for visualization
        self.start = start_peg # save peg naemes
        self.target = target_peg
        self.aux = aux_peg
        self.peg_names = (start_peg, aux_peg, target_peg)

        self.towers = None
        
    # solve the toh problem via iteration
    def solve_via_iteration(self): # O(2^n)
        self.moves = [] # reset moves
        n = self.num_discs
        if n == 0:
            return 
        # create a stack for simulating
        # elements are [(number of discs, start peg, target peg, auxiliary peg, is done flag)]
        stack = [(n, 0, 1, 2, False)]  
        # while the stack discs exists
        while stack:
            # pop first element from the stack
            num_discs, start, target, aux, done = stack.pop()
            # base case when only 1 disc
            if num_discs == 1:
                # move disc to final target
                self.moves.append((1, self.peg_names[start], self.peg_names[target]))  
                continue
            # while not done with the sorting
            if not done:
                # append the next moves onto the stack
                stack.append((num_discs, start, target, aux, True))  # current is as done
                stack.append((num_discs - 1, start, aux, target, False))  # move n-1 discs from start to aux
            else:
                # save the move
                self.moves.append((num_discs, self.peg_names[start], self.peg_names[target]))
                # append the next moves onto the stack
                stack.append((num_discs - 1, aux, target, start, False))  # move n-1 discs from aux to target

    # solve the toh problem via recursion
    def solve_via_recursion(self): # base function is O(1) but calls a O(2^n) function
        self.moves = [] # reset moves
        # use the cb function to populate moves
        self.recursive_solution_cb(self.num_discs, self.peg_names[0], self.peg_names[1], self.peg_names[2])
    def recursive_solution_cb(self, n, start, target, aux): # O(2^n)
        # base case of no discs
        if (n == 0):
            return
        # move from start peg to aux peg
        self.recursive_solution_cb(n - 1, start, aux, target)
        # save move
        self.moves.append((n, start, target))
        # move from aux peg to target peg
        self.recursive_solution_cb(n - 1, aux, target, start)

    # function to play the animation in the terminal 1 time
    # parameter is the speed / how many seconds between each frame
    def play(self, speed): # O(2^n)
        # function is used to simulate the towers of hanoi problem
        # it needs the instructions saved in self.moves to work properly
        # this function cannot solve the problem on its own however it uses
        # the moves another function found as a solution and simulates it / prints it to the terminal
        # reset towers
        self.towers = None # populate towers based off of moves
        self.towers = [[[], [], []] for _ in range(2 ** self.num_discs - 1)]
        # populate first move
        self.towers[0][0] = [x for x in range(self.num_discs, 0, -1)]
        # variable to save prev towers
        prev_towers = None
        # print turn 0
        self.print_to_terminal(0, 0)
        # variable to save current turn number
        turn = 1
        # for loop for each move
        for i in range(len(self.moves)):
            # the start and target of each move
            start = self.moves[i][1]
            target = self.moves[i][2]
            # for the second move, third move, etc
            # when a prev towers array has been saved
            if prev_towers:
                # get the disc from the start peg
                if start == self.start:
                    disc = prev_towers[0].pop()
                elif start == self.aux:
                    disc = prev_towers[1].pop()
                else:
                    disc = prev_towers[2].pop()
                # move the disc to the target peg
                if target == self.start:
                    prev_towers[0].append(disc)
                elif target == self.aux:
                    prev_towers[1].append(disc)
                else:
                    prev_towers[2].append(disc)
                self.towers[i] = prev_towers
            else:
                # for the first move
                # get the disc from the start peg
                if start == self.start:
                    disc = self.towers[i][0].pop()
                elif start == self.aux:
                    disc = self.towers[i][1].pop()
                else:
                    disc = self.towers[i][2].pop()
                # move the disc to the target peg
                if target == self.start:
                    self.towers[i][0].append(disc)
                elif target == self.aux:
                    self.towers[i][1].append(disc)
                else:
                    self.towers[i][2].append(disc)
            # save the prev towers
            prev_towers = self.towers[i]
            # wait for the given amount of time
            time.sleep(speed)
            # print turn n to terminal
            self.print_to_terminal(turn, i)
            turn += 1

    # function to print the current move / position of the pegs and discs to the terminal
    # it needs the turn number and the move number
    def print_to_terminal(self, turn_number, move_number): # O(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("move", turn_number)
            # print start peg info
            print(self.start, end=' ')
            for d in self.towers[move_number][0]:
                if d:
                    print(d, end=' ')
            print()
            # print target pegs info
            print(self.target, end=' ')
            for d in self.towers[move_number][1]:
                if d:
                    print(d, end=' ')
            print()
            # print aux pegs info
            print(self.aux, end=' ')
            for d in self.towers[move_number][2]:
                if d:
                    print(d, end=' ')
            print("\n")

    # function to create a terminal ui for the user to interact with and to show the solutions
    def gui(self):
        while True:
            # get how many discs the user wants to solve for
            print("how many discs do you want to solve for: (q to quit)", end=' ')
            discs = input()
            # quit case
            if discs == 'q':
                break
            print("how many seconds for each frame:", end=' ')
            spf = float(input())
            print(f"solving for {discs} discs")
            # set disc num
            self.num_discs = int(discs)
            # solve the problem
            #self.solve_via_iteration()
            self.solve_via_recursion()
            # play the frame by frame animation
            self.play(spf)

# create the class
toh = TOWER_OF_HANOI()
# start the main loop
toh.gui()