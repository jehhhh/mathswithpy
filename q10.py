A = [i for i in range(2, 21, 2)]
B = [i for i in range(6, 50, 6)]
R1 = []
for a in A:
    for b in B:
        if (b % a) == 0:
            R1.append((a, b))
R2 = []
for a in A:
    for b in B:
        if (a + b) % 10 == 0:
            R2.append((a, b))

intersection = []
for r1 in R1:
    for r2 in R2:
        if r1 == r2:
            intersection.append(r1)

print(len(intersection))

R3 = []
for b in B:
    for x in R1:
        for y in R2:
            if x[1] == y[1] == b and x[0] in A and y[0] in A:
                R3.append((x[0], y[0]))
print(len(R3))
unique = []
for i in R3:
    if i not in unique:
        unique.append(i)
print(unique, len(unique))
