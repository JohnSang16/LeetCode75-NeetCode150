#use stack and res list init with 0's
#use for loop to go to every item in temperatures and push its idx onto the stack
#use a while loop within it to check if stack has item + if curr temp is greater than temp at the stack idx
#we start from first item idx pushed onto stack, we pop when the new item is greater in val
#than the item at the idx at the top of stack, and then we get the dist by cur_idx - popped_idx
#then we set that dist to the idx which equals popped in a res arr
#if an item is still on the stack after going through the whole loop leave as 0 in res list

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #res = [0, 0, 0, 0, 0, 0, 0]
        res = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
       
            while stack and temp > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped

                 #stack = [0]
            stack.append(i)
        return res