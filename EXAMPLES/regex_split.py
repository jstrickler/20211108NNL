#!/usr/bin/env python

import re

rx_wordsep = re.compile(r"[^a-z]+", re.I)  # <1>

s1 = '''There are 10 kinds of people in a Binary world, I hear" -- Geek talk'''

# re.split(pattern, text)
words = rx_wordsep.split(s1)  # <2>
print(words)

s2 = "a,b,c, d, e,f,g"
values = re.split(r",\s*", s2)
print(values)


