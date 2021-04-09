def triplet_prime(num):
    checklist = []
    finallist = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            checklist.append(i)
    for i in checklist:
        if (i in checklist) and (i+2 in checklist) and (i+6 in checklist):
            finallist.append([i, i+2, i+6])
    return finallist
print(triplet_prime(23))