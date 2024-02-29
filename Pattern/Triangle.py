# Problem 1

i=1;
n=int(input("Enter the number "))
count=1;
while(i<=n):
    j=1;
    while(j<=i):
        print(count,end=" ")
        count=count+1
        j=j+1
    print()
    i=i+1

# Problem 2

# i=1;
n=int(input("Enter the number "))
while(i<=n):
    j=1;
    while(j<=n):
        char=ord('A')+j-1;
        print(chr(char),end=" ")
        j=j+1
    print()
    i=i+1

# Problem 3

i=1;
n=int(input("Enter the number "))
count=ord('A')
while(i<=n):
    j=1;
    while(j<=n):
        print(chr(count),end=" ")
        count=count+1
        j=j+1
    print()
    i=i+1
