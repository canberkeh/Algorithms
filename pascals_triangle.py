def pascal(num):        
    if num > 1:
        p = [[1], [1, 1]] #ilk iki eleman belli olduğu için direkt yazıyoruz 
        for i in range(2, num): #ilk iki eleman belli olduğu için direkt yazıyoruz.
            a = [1]  # baş ve sona hep 1 geldiği için
            for j in range(1, i):   # baş ve son 1 olacak, bunun içerisine yeni sayılar eklenecek
                a.append(p[i-1][j-1] + p[i-1][j]) # her seferinde döngüdeki bir önceki elemanı ekleyecek
            a.append(1)  # sonuna 1 ekliyor
            p.append(a)
        return p
    elif num == 1:return [[1]]
print(pascal(5))