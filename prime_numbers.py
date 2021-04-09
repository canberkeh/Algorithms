# def prime_numbers0(num):
#     for i in range(500, num): #start at 3
#         prime = 1 
#         for j in range(2, i): #start at 2, untill i
#             if i % j == 0: 
#                 prime = 0
#         if prime != 0:
#             print(i)
# prime_numbers0(100)

#--------------------------------------------------------------
def prime_numbers1(num):
    sum, sieve = [], ([True] * num)
    for i in range(2, num): 
        if sieve[i]:
            sum.append(i)
            for i in range(i * i, num, i):
                sieve[i] = False
    print(sum)
prime_numbers1(100)
'''
→ sieve dizisine n kadar True ekliyor.
→İlk bulduğu sayı 2
→ 2’nin katlarına False atıyor.
→ Aynı şekilde 3, 5, 7… ‘yi asal olarak ekledikten sonra katlarına False atıyor.
Böylece asal olmayanlara False atanıyor. Geriye de True yani asal sayılar kalıyor.
'''

# --------------------------------------------
# def prime_numbers2(start, end):
#     for i in range(start, end+1): 
#         if i>1: 
#             for j in range(2,i): 
#                 if(i % j==0): 
#                     break
#             else: 
#                 print(i)
# prime_numbers2(500, 599)
