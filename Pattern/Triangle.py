# Problem 1

# i=1;
# n=int(input("Enter the number "))
# count=1;
# while(i<=n):
#     j=1;
#     while(j<=i):
#         print(count,end=" ")
#         count=count+1
#         j=j+1
#     print()
#     i=i+1

# Problem 2

# i=1;
# n=int(input("Enter the number "))
# while(i<=n):
#     j=1;
#     while(j<=n):
#         char=ord('A')+j-1;
#         print(chr(char),end=" ")
#         j=j+1
#     print()
#     i=i+1

# Problem 3

# i=1;
# n=int(input("Enter the number "))
# count=ord('A')
# while(i<=n):
#     j=1;
#     while(j<=n):
#         print(chr(count),end=" ")
#         count=count+1
#         j=j+1
#     print()
#     i=i+1


# Problem 4
# i = 1
# n = int(input("Enter the number "))
# while i <= n:
#     j = 1
#     ch = ord('A') + i - 1
#     while j <= i:
#         print(chr(ch), end=" ")
#         j = j+1
#         ch = ch+1
#     print()
#     i = i+1


# Problem 5
# i = 1
# n = int(input("Enter the number "))
# while i <= n:
#     j = 1
#     ch = ord('A') + n-i
#     # 65 + 4 -1 -->69 -1 ==> 68 --> D
#     while j <= i:
#         print(chr(ch), end="")
#         j = j+1
#         ch = ch+1
#     print()
#     i = i+1

# Problem 6
i = 1
n = int(input("Enter the number"))
while i <= n:
    space = n-i
    while space:
        print(" ", end="")
        space = space-1
    j = 1
    while j <= i:
        print("*", end="")
        j = j+1
    print()
    i = i+1
