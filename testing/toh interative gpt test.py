class TOWER_OF_HANOI:
    def __init__(self, num_discs=3):
        self.num_discs = num_discs
        self.moves = []  # Store moves for visualization
        self.peg_names = ('A', 'C', 'B')

    def solve_via_iteration(self):
        stack = [(self.num_discs, 0, 1, 2, True)]  # Initial state: (number of discs, source peg, auxiliary peg, destination peg, moving forward)
        while stack:
            num_discs, source, auxiliary, destination, moving_forward = stack.pop()

            if num_discs == 1:
                # Move the smallest disc
                self.moves.append((source, destination))
            else:
                if moving_forward:
                    # Move n-1 discs from source to auxiliary peg
                    stack.append((num_discs - 1, source, destination, auxiliary, not moving_forward))
                    # Move the largest disc from source to destination peg
                    self.moves.append((source, destination))
                    # Move the n-1 discs from auxiliary to destination peg
                    stack.append((num_discs - 1, auxiliary, source, destination, not moving_forward))
                    # Move the smallest disc from source to auxiliary peg
                    stack.append((1, source, auxiliary, destination, not moving_forward))
                else:
                    # Move the smallest disc from auxiliary to destination peg
                    self.moves.append((auxiliary, destination))

        return self.moves


# Example usage:
tower = TOWER_OF_HANOI(2)
tower.solve_via_iteration()
print(tower.moves)
