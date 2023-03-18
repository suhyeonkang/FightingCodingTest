
## 내가 짠 코드 

class Solution:
    def isValid(s: str) :
        stack = []
        for i in s :
            if(i == ')' or i == '}' or i == ']' ) :
                if(stack[len(stack)-1] + i == '()' or stack[len(stack)-1] + i == '{}' or stack[len(stack)-1] + i == '[]'):
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
        return True
                   
                    
print(Solution.isValid(s='[(){()}]'))

## 더 간결한 코드 

def isValid(s: str):
    stack = []
    for i in s :
        if ( i == '(' ):
            stack.append(')')
        elif ( i == '{' ) :
            stack.append('}') 
        elif ( i == '[') :
            stack.append(']')
        elif (i not in stack) or (stack.pop() != i) :
            return False
    return True

print(isValid(s= '[(){()}]'))    
         