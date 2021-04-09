def roman_to_int(s):
    dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    r_list = [dic[i] for i in s] # for i in s --> append in r_list []
    num = 0 
    for j in range(len(r_list)-1): # not to go out of index.
        if r_list[j] < r_list[j+1]: 
            num -= r_list[j] #if j element is less than j+1 --> -
        else:
            num += r_list[j]
    num += r_list[-1] #add the last element
    return num
print(roman_to_int("XI"))