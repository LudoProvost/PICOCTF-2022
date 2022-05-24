import string

s = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288"
a = s.split(" ")
a = [int(i)%37 for i in a]

ALPHABET = string.ascii_uppercase + string.digits + '_'

flag = ""
for i in a:
    flag += ALPHABET[i]
print(f'picoCTF{{{flag}}}')