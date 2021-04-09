def isUgly(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        if (n % 5 == 0):
            n //= 5
        elif (n % 3 == 0):
            n //= 3
        elif (n % 2 == 0):
            n //= 2
        else:
            return False
        return isUgly(n)
print(isUgly(15))
        