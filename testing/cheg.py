import tkinter as tk
import time

class TowerOfHanoi:
    def __init__(self, num_discs, num_pegs=3):
        """
        Initialize the Tower of Hanoi problem with the specified number of discs and pegs.
        """
        self.num_discs = num_discs
        self.num_pegs = num_pegs
        self.pegs = [[] for _ in range(num_pegs)]  # Initialize pegs
        self.moves = []  # Store moves for visualization

        # Initialize starting peg
        for disc in range(num_discs, 0, -1):
            self.pegs[0].append(disc)

    def recursive_solve(self, n, start, target, auxiliary):
        """
        Recursive function to solve the Tower of Hanoi problem.
        """
        if n == 1:
            self.moves.append((start, target))
            return
        self.recursive_solve(n - 1, start, auxiliary, target)
        self.moves.append((start, target))
        self.recursive_solve(n - 1, auxiliary, target, start)

    def iterative_solve(self):
        """
        Iterative function to solve the Tower of Hanoi problem.
        """
        total_moves = 2 ** self.num_discs - 1
        if self.num_discs % 2 == 0:
            iter_pegs = [(0, 1), (0, 2), (1, 2)]
        else:
            iter_pegs = [(0, 2), (0, 1), (1, 2)]

        for move in range(total_moves):
            source, dest = iter_pegs[move % 3]
            self.moves.append((source, dest))

    def move_disc(self, source, target):
        """
        Move a disc from the source peg to the target peg.
        """
        disc = self.pegs[source].pop()
        self.pegs[target].append(disc)

    def visualize(self, speed):
        """
        Visualize the Tower of Hanoi problem with graphical animation.
        """
        root = tk.Tk()
        canvas = tk.Canvas(root, width=800, height=400)
        canvas.pack()

        disc_width = 30
        disc_height = 20
        peg_width = 10
        peg_height = 200
        peg_distance = 300 // self.num_pegs

        peg_centers = [(i * peg_distance + peg_width // 2, 200) for i in range(self.num_pegs)]

        discs = []
        for peg in range(self.num_pegs):
            for i, disc in enumerate(self.pegs[peg]):
                x0 = peg_centers[peg][0] - disc * disc_width // 2
                y0 = 380 - (i * disc_height)
                x1 = x0 + disc * disc_width
                y1 = y0 - disc_height
                discs.append(canvas.create_rectangle(x0, y0, x1, y1, fill="blue"))

        for move in self.moves:
            source, target = move
            canvas.update()
            time.sleep(speed)

            source_center = peg_centers[source]
            target_center = peg_centers[target]

            disc_id = self.pegs[source][-1] - 1
            disc = discs[disc_id]

            dx = target_center[0] - source_center[0]
            dy = target_center[1] - source_center[1]

            canvas.move(disc, dx, dy)
            canvas.update()

            self.move_disc(source, target)

        root.mainloop()


if __name__ == "__main__":
    num_discs = int(input("Enter the number of discs: "))
    speed = float(input("Enter the animation speed (seconds per move): "))
    num_pegs = int(input("Enter the number of pegs (minimum 3): "))

    hanoi = TowerOfHanoi(num_discs, num_pegs)
    hanoi.recursive_solve(num_discs, 0, num_pegs - 1, 1)
    hanoi.visualize(speed)