def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while num > 0: # girilen sayı 0 dan büyük oldukça ; 
        for _ in range(num // val[i]): # örn 12 için sadece X - 10 değerlerinde calısacak. RANGE(1) olursa döngü çalışır !
            roman_num += syb[i] # eğer tam bölünürse, symbol ü roman_num a ata
            num -= val[i] # num'dan val[i]'yi çıkararak döngüye devam et
        i += 1 # counter'ı arttır.
    return roman_num
print(int_to_Roman(123))

