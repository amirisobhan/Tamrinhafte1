A = [12, 4, 9, 20]

minimum = A[0]

for i in range(1, len(A)):
    if A[i] < minimum:
        minimum = A[i]

print("Min =", minimum)
