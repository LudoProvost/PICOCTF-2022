import string

s = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"
a = s.split(" ")
# a = [(int(i)%41)-1 for i in a]
a = [pow(int(i), -1, 41)-1 for i in a]

ALPHABET = string.ascii_uppercase + string.digits + '_'

flag = ""
for i in a:
    flag += ALPHABET[i]
print(f'picoCTF{{{flag}}}')