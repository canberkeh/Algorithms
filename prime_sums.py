'''
Verilen sayıya kadar olan asal sayılardan, toplamı verilen sayıya eşit olanları döner
'''

class PrimeSum():
    def primesummary(self, prime_list, num):
        result = []
        for i in range(len(prime_list)):
            for j in range(len(prime_list)):
                if i == j:continue
                if prime_list[i] + prime_list[j] == num:
                    result.append([prime_list[i], prime_list[j]])
        print(result)

    def prime_numbers(self, num):
        sieve = ([True] * num)
        prime_list = []
        for i in range(2, num):
            if sieve[i]:
                prime_list.append(i)
                for i in range(i * i, num, i):
                    sieve[i] = False
        self.primesummary(prime_list, num)
classrun = PrimeSum()
classrun.prime_numbers(15)