import random, hashlib
from func import find_path

root = '/home/pi/httpapi/files for upload/'

str1 = '1234567890'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
ls = list(str1+str2+str3)

for i in range(15):
    random.shuffle(ls)
    inside = ''.join([random.choice(ls) for x in range(10)])
    random.shuffle(ls)
    name = ''.join([random.choice(ls) for x in range(7)])
    path = root+name
    file = open(path, 'w')
    file.write(inside)
    
