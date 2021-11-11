#!/usr/bin/python3

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup():
    pass

for s in spam():
    clean_s = cleanup(s)
    print(f"s is >{s}< clean_s is >{clean_s}")

