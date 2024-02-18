import time
import os
import tkinter as tk

class TOWER_OF_HANOI:
    def __init__(self, num_discs=3, start_peg='A', target_peg='B', aux_peg='C'):
        self.num_discs = num_discs
        self.moves = []
        self.start = start_peg
        self.target = target_peg
        self.aux = aux_peg
        self.peg_names = (start_peg, aux_peg, target_peg)
        self.towers = None
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()

    def solve_via_iteration(self):
        self.moves = []
        n = self.num_discs
        if n == 0:
            return
        stack = [(n, 0, 1, 2, False)]
        while stack:
            num_discs, start, target, aux, done = stack.pop()
            if num_discs == 1:
                self.moves.append((1, self.peg_names[start], self.peg_names[target]))
                continue
            if not done:
                stack.append((num_discs, start, target, aux, True))
                stack.append((num_discs - 1, start, aux, target, False))
            else:
                self.moves.append((num_discs, self.peg_names[start], self.peg_names[target]))
                stack.append((num_discs - 1, aux, target, start, False))

    def solve_via_recursion(self):
        self.moves = []
        self.recursive_solution_cb(self.num_discs, self.peg_names[0], self.peg_names[1], self.peg_names[2])

    def recursive_solution_cb(self, n, start, target, aux):
        if n == 0:
            return
        self.recursive_solution_cb(n - 1, start, aux, target)
        self.moves.append((n, start, target))
        self.recursive_solution_cb(n - 1, aux, target, start)

    def play(self, speed):
        self.towers = None
        self.towers = [[[], [], []] for _ in range(2 ** self.num_discs - 1)]
        self.towers[0][0] = [x for x in range(self.num_discs, 0, -1)]
        prev_towers = None
        turn = 1
        for i in range(len(self.moves)):
            start = self.moves[i][1]
            target = self.moves[i][2]
            if prev_towers:
                disc = prev_towers[start].pop()
                prev_towers[target].append(disc)
                self.towers[i] = [peg.copy() for peg in prev_towers]
            else:
                disc = self.towers[i][start].pop()
                self.towers[i][target].append(disc)
            prev_towers = [peg.copy() for peg in self.towers[i]]
            self.canvas.delete("all")
            self.draw_towers()
            self.window.update()
            time.sleep(speed)

    def draw_towers(self):
        for i in range(3):
            for j, disc in enumerate(self.towers[-1][i]):
                width = disc * 20
                height = 20
                x = 50 + i * 200 - width / 2
                y = 380 - j * height
                self.canvas.create_rectangle(x, y, x + width, y + height, fill="blue")

    def gui(self):
        while True:
            print("how many discs do you want to solve for: (q to quit)", end=' ')
            discs = input()
            if discs == 'q':
                break
            print("how many seconds for each frame:", end=' ')
            spf = float(input())
            print(f"solving for {discs} discs")
            self.num_discs = int(discs)
            self.solve_via_recursion()
            self.play(spf)
        self.window.destroy()

toh = TOWER_OF_HANOI()
toh.gui()
