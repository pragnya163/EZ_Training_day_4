stack=[]
n=int(input("enter no of elements:"))
for i in range(n):
    stack.append(int(input("enter a element:")))
print(stack)
for i in range(n):
    print(stack.pop())
print(stack)