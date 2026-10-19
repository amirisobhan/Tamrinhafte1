A = [4, 7, 2, 9]
sum = 0

for i in range(len(A)):
    if A[i] % 2 == 0:
        sum = sum + A[i]

print("Sum =", sum)
