def happy(n):
    n_list = []
    count = 0
    n_sum = 0
    while True:
        for i in str(n):
            n_list.append(int(i))
        for j in n_list:
            n_sum = n_sum + j ** 2
        n_list = []
        n = n_sum
        n_sum = 0
        count += 1
        print(n)
        if n == 1:
            break
        if count > 10:
            break
    return n == 1
happy(10)