import sys

a = 1000

sys.stdout.write("Enter 2 digits: ")
sys.stdout.flush()
a = sys.stdin.read(4)
b = sys.stdin.read(5)
c = sys.stdin.read(2)

print("a=",a)
print("b=",b)
print("c=",c)
