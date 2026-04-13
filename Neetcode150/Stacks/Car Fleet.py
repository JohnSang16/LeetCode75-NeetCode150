#have a stack where you append when its a new item
#if the new item reaches target <= in time as the pre-existing item on the stack, we pop
#repeat and at the end check how many items are left on stack
#that is the amount of car fleets

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        