def solution(N):
    # Implement your solution here
    binary = bin(N)[2:]

    gap = 0
    curr = 0

    for bit in binary:
        if bit == '1':
            gap = max(gap, curr)
            curr = 0
        else: curr += 1
    return gap