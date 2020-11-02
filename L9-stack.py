#121910313025
#Push and Pop in stack
stack = []
n=int(input("Enter number of elements:"))
# append() function to push
# element in the stack
for i in range(0,n):
      ele=int(input())
      stack.append(ele)

 
print('Initial stack')
print(stack)
 
# pop() fucntion to pop
# element from stack 

m=int(input("enter number of elements to remove"))
print('\nElements poped from stack:')
for i in range(0,m):
    stack.pop()
 
print('\nStack after elements are poped:')
print(stack)
