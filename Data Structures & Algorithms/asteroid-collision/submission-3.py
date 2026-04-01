class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        myStack = []
        contColsn = True
        index = 0

        while contColsn:
            if index == len(asteroids):
                contColsn = False
                break

            if not myStack:
                myStack.append(asteroids[index])
                index += 1
                continue

            # collision only when stack top is + and current is -
            if asteroids[index] < 0 and myStack[-1] > 0:
                if abs(myStack[-1]) == abs(asteroids[index]):
                    myStack.pop()
                    index += 1
                    continue
                elif abs(myStack[-1]) > abs(asteroids[index]):
                    index += 1
                    continue
                else:
                    myStack.pop()
                    continue   # <-- important: re-check same asteroid with new top
            else:
                myStack.append(asteroids[index])
                index += 1

        return myStack