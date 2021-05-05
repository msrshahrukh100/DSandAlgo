



def find_next_greatest_to_right(arr):

    stack = []
    answer = []
    for i in arr[::-1]:
        if not stack:
            answer.append(-1)
        
        elif stack and stack[-1] > i:
            answer.append(stack[-1])
        
        elif stack and stack[-1] <= i:
            while stack and stack[-1] <= i:
                stack.pop()
            
            if not stack:
                answer.append(-1)
            else:
                answer.append(stack[-1])
    
        stack.append(i)

    return answer[::-1]

arr = [1, 3, 0, 0, 1, 2, 4]

print(find_next_greatest_to_right(arr))

