import re
import time
import pandas as pd


file= open('data', 'r')
output_file= open('new_data', 'r')


#Findall example  . return all results
'''
for line in file:
   for word in re.findall('Prasad', line):
       print(line)
'''

#seach example  > will return only occurrence
#Match strings examples

#pattern= "^S[a-z]*"                                    #Word Sun
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
'''
for line in file:
    if re.match(pattern, line):
        print(f"Pattern Found!!")
        time.sleep(1)
        match= re.sub(pattern, "Mon", line)
        output_file.write(match)
        print(f"String Replaced!!: {match}")


#Search a log from a file with time range.
'''

def log_pat(pattern, name):
    match=pattern
    for line in name:
        if re.search(match, line):
            print(line)

#log_pat("Sun Jul 11 13:3[2-5]", file)


#slicing
'''
x="Hello World"
print(x[::-1])

y="Hello World"
z=y.split(" ")
print(z[::-1])
'''

# Match mobile numbers; Data 1

'''
pattern= "([\d]{1,3})\-?([\d]{1,3})\-([\d]{1,4})"     #([\d]{1,3}) > first set, with digit, 1 to 3 digits. #{1,3} digits between 1 to 3 times . #+\-? >optional "-"

for line in output_file:
    if re.search(pattern, line):
        print(line)
'''

# Data 2 Mobile number 1

'''
pattern= "^(\+?[\d]{1,3}[- ]?)?([\d]{10}$)"      #"+" optional matching
for line in output_file:
    if re.search(pattern, line):
        print(line)

'''

#print 10th line.

''''
count=0

for i in output_file:
    if count==9:
        print(i)
    else:
        count= count+1
'''



file.close()
output_file.close()

