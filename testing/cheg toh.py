class TOWER_OF_HANOI:
    def __init__(self, num_discs=3, start_peg='A', target_peg='B', aux_peg='C'):
        self.num_discs = num_discs
        self.moves = []  # Store moves for visualization
        self.peg_names = (start_peg, aux_peg, target_peg)  # Tuple for peg names

    def solve_via_iteration(self):
        n = self.num_discs
        if n == 0:
            return  # No discs, nothing to do

        # Initialize stack for iterative simulation
        stack = [(n, 0, 1, 2, False)]  # Each element: (number of discs, start peg, target peg, auxiliary peg, is_done flag)

        while stack:
            num_discs, start, target, aux, is_done = stack.pop()  # Pop the top element from stack

            if num_discs == 1:  # Base case: only one disc left
                self.moves.append((1, self.peg_names[start], self.peg_names[target]))  # Move disc directly to target
                continue  # Skip to next iteration

            if not is_done:
                # Push the next moves onto the stack
                stack.append((num_discs, start, target, aux, True))  # Mark current move as done
                stack.append((num_discs - 1, start, aux, target, False))  # Move n-1 discs from start to aux
            else:
                # Record the move
                self.moves.append((num_discs, self.peg_names[start], self.peg_names[target]))
                # Push the next moves onto the stack
                stack.append((num_discs - 1, aux, target, start, False))  # Move n-1 discs from aux to target

        # Note: At the end, self.moves will contain the solution steps.

# Example usage:
hanoi = TOWER_OF_HANOI()
hanoi.solve_via_iteration()
print(hanoi.moves)