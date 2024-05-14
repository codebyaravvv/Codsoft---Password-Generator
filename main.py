import random
import string
s1=string.ascii_letters
#print(s1)
s2=string.digits
#print(s2)
s3=string.punctuation
#print(s3)
plen=int(input("Enter the length of your password should be?\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
random.shuffle(s)
print("".join(s[0:plen]))

