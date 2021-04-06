# Arithmetic, Geometric and Harmonic means.
num_list = [5, 6, 9, 23]
num_len = len(num_list)
def arithmetic(*args):
    summary = 0
    for i in args:
        summary = summary + i
    result = summary / num_len
    print(round(result,2))
arithmetic(5, 6, 9, 23)

def geometric(*args):
    summary = 1
    for i in args:
        summary *= i
    result = summary ** (1/num_len)
    print(round(result, 2))
geometric(5, 6, 9, 23)

def harmonic(*args):
    summary = 0
    for i in args:
        summary += (1/i)
    a = lambda num_len, summary: num_len / summary # Lambda'yı a ya atayıp dışarıdan fonksiyona parametrelerini gönderip,
    print(round(a(num_len, summary),2))            # : sonra işlemi yaptırdı
harmonic(5, 6, 9, 23)