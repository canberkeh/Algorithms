class Caesar():
#CS50X Caesar task in python
    def caesar_main(self):
        key = int(input("Key (number) : ")) # get key number
        caesar = input("Text : ") # get string
        new_caesar = "" #converted string
        for i in caesar: #loop in given string
            if i.isalpha():   # if i is alpha (a-z)
                ascii_offset = 65 if i.isupper() else 97 # set ascii for hexadecimal 
                ascii_number = ord(i) - ascii_offset  # 
                ci = (ascii_number + key) % 26 #if there is a string z, %26 returns it to the beginning so there wont be error for alphabetic numbers
                new_caesar = new_caesar + chr(ci + ascii_offset) # add converted chars to new_caesar
            elif i == " ":  #if there is a space, add it to new_caesar
                new_caesar = new_caesar + i 
            else:continue #if there is a number or numeric sign, pass! - if you dont want to pass just add --> new_caesar = new_caesar + i 
        print(new_caesar)
        return new_caesar
cs50 = Caesar()
cs50.caesar_main()