import re
import time

file= open('data', 'r')

#Findall example  . return all results
'''
for line in file:
   for word in re.findall('Prasad', line):
       print(line)
'''

#seach example  > will return only occurrence
#Match strings examples

pattern= "^S[a-z]*"                                    #Word Sun
#pattern= "[\w]+@[\w]+\.[\w]"                          # Email
#pattern= "[\W]+@[\w]+\.[\w]"                           # email with first name is not word.
#pattern= "\+[\d]{0,3} [\d]"                             #"\+" Start with +, "+[\d]{0,3}" 0-3 digits, space * digits

#search String
'''
for line in file:
    if re.search(pattern, line):
        print (f"Pattern found: {line}")
'''

#Replace String

for line in file:
    if re.match(pattern, line):
        print(f"Pattern Found!!")
        time.sleep(1)
        match= re.sub(pattern, "Mon", line)
        print(f"String Replaced!!: {match}")


#Search a log from a file with time range.
'''
def log_pat(pattern, name):
    match=pattern
    for line in name:
        if re.search(match, line):
            print(line)

log_pat("Sun Jul 11 13:3[2-5]", file)


file.close()
'''

#slicing
'''
x="Hello World"
print(x[::-1])

y="Hello World"
z=y.split(" ")
print(z[::-1])
'''