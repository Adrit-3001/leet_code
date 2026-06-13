def solution(A, K):
    # Implement your solution here
    a_c = A[:]
    n = len(A)
    if n == 0: return A
    while K != 0:
        # print(a_c)
        for i in range(n):
            A[i] = a_c[i-1]
        a_c = A[:]
        K -= 1
    return A