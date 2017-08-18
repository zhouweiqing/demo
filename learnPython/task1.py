import os
from copy import *

"""
>>> tell me dog age: 4
real age is 32

"""

def dog_age():
    dog_age = int(input("tell me dog age: "))
    real_age = 0
    
    if dog_age == 1:
        real_age = 16
    elif dog_age == 2:
        real_age = 22
    elif dog_age > 2:
        real_age = 22 + 5 * (dog_age - 2)
        
    print("real age is " + str(real_age))

char_morse = {'A': '.-', 'B':'-...'}
morse_char = {}
for char in char_morse:
    morse_char[char_morse[char]] = char

def txt2morse(txt):
    """ change text to morse code
    """
    morse_code = ""
    for char in txt:
        if char == " ":
            morse_code += "  "
        else:
            morse_code += char_morse[char] + " "
    return morse_code

def morse2txt(txt):
    """ change morse code to char
    """
    char_code = ""
    for mword in txt.split(" "):
        char_code += morse_char[mword]
    return char_code

print(txt2morse("ABA B"))
print(morse2txt(".- .-"))

def flatten(lst):
    """ expand nested list to plain list
    """
    flatten_list = []
    for elm in lst:
        if type(elm) is list or type(elm) is tuple:
            flatten_list.extend(flatten(elm))
        elif type(elm) is dict:
            flatten_list.extend(flatten(elm.items()))
        else:
            flatten_list.append(elm)
    return flatten_list
            
print(flatten([1,2,[1,2], "abc", {'a':1, 'b':2}]))

fh = open("bundeslaender.txt")
fh.readline()
for line in fh:
    land, size_of_land, *rem = line.split()
#    print(line)

class robot():
    def __init__(self):
        self.name = 'robot'
        self._name_ = 'private name'

    def __str__(self):
        return self.name + 'str'
    
    @staticmethod
    def hi(self):
        print("hi " + self.name)

x = robot()
x.name = 'xyz'
print(x._name_)
print(x)
robot.hi()


#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
