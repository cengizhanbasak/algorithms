# problem: swap two integers without using a temporary variable
# input two integers
x = int(input())
y = int(input())
print("x: ",x)
print("y: ",y)
x=x^y
y=x^y
x=x^y
# swap done
print("x: ",x)
print("y: ",y)
