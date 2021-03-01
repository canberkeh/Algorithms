'''
American Express = 15 haneli, 34, 37 ile başlar. 
MasterCard = 16 haneli, 51,52,53,54,55 ile başlar.
Visa = 13 // 16 haneli, 4 ile başlar.
'''
def credit_luhn(num):
    counter, check = 0, num
    while check>1:
        if (check < 100 and check > 10):
            first_two = int(check)   #ilk iki sayısına göre kart kontrolü.
        check = check / 10 #check' i 0 dan kücük olana kadar 10'a bölerek length'i bul. (counter'ın length'i kart numarası hane sayısını verecek.).
        counter = counter + 1 #her seferinde sayacı artır.
    if ((counter != 13) and (counter != 15) and (counter !=16)):print("INVALID CARD") #başta kontrol
    else: # luhn algoritması
        a, b, c = 0, 0, 0 #a altı çizililer için, b altı cizili olmayanlar icin #c de b ye destek için
        while num > 0:
            a = int(a + (num % 10))
            num = int(num / 10)
            if num > 0:
                c = int((num % 10) * 2)
                b = int(b + c / 10)
                b = int(b + c % 10)
                num = int(num / 10)
        kalan = int((a + b) % 10)
        if kalan != 0:print("INVALID")
        elif kalan == 0: # kart kontrolleri 
            if ((counter == 15) and ((first_two == 34) or (first_two == 37))):print("AMEX")
            elif ((counter == 16) and ((first_two >= 51 and first_two <=55))):print("Mastercard")
            elif (((counter == 13) or (counter == 16)) and ((first_two / 10 == 4))):print("Visa ")
            else:print("INVALID")
credit_luhn(4003600000000014) # visa true