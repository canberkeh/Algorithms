'''
hi how are you
 X  X  X  X  X
ihh woa ery uo
'''
def bc(text):
    n = len(text)
    new_text = ""
    if n % 2 == 0:
        for i in range(n):
            if i%2 == 0:
                new_text = new_text+ text[i+1] + text[i]
    else:
        new_text = ""
        text = text + " "
        n = len(text)
        for i in range(n):
            if i%2==0:
                new_text = new_text + text[i+1] + text[i]
    print(new_text)
bc("hi how are you")
###############################################################################################
'''
Ascii number + 9
'''

def plus_9(text):
    new_text = ""
    for i in text:
        i = ord(i)
        i = chr(i+9)
        new_text = new_text + i
    print(new_text)
    solve_9(new_text)

def solve_9(new_text):
    original_text = ""
    for i in new_text:
        i = ord(i)
        i = chr(i-9)
        original_text = original_text + i
    print(original_text)
plus_9("berke")



