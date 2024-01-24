N = int(input()) 
mass = []
if 1 <= N <= 10000:
    for i in range(N):
        a = int(input())
        if abs(a) < 10 ** 5:
            mass.append(a) 
print(mass[::-1])