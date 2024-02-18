    '''def iterative_solution_cb(self, n, start, target, aux):
        stack = [(n, start, target, aux, False)]

        while stack:
            n, start, target, aux, moving_second = stack.pop()

            if n == 1:
                self.moves.append((n, start, target))
            elif not moving_second:
                # Push the recursive calls onto the stack in the correct order
                stack.append((n - 1, aux, target, start, False))
                stack.append((1, start, target, aux, True))
                stack.append((n - 1, start, aux, target, False))
            else:
                # Push the next recursive call onto the stack
                stack.append((n - 1, start, target, aux, False))'''