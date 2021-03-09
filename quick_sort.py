def partition(arr,low,high):  #parçalama
    i = ( low-1 ) #başlangıçta -1 --- eğer -1 yazmazsan ilk elemanı kontrol etmez
    pivot = arr[high]     # dizinin sonundaki elemanı alacak
    for j in range(low , high):  #low'dan 
        if arr[j] <= pivot: #array'ın looptaki elemanı pivottan küçük oldukça devam:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)# pi = i + 1 gelecek
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        return arr

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) #(arr, 0 , HIGH) High olacak değer, len'in -1 ini alacagız (out of range vermemesi için)
quickSort(arr, 0, n-1) 
print(quickSort(arr, 0, n-1))