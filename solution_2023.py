#    .-""-.
#   /,..___\  Advent Of Code Solutions 2023
#  () {_____}
#    (/-@-@-\)
#    {`-=^=-'}
#    {  `-'  } "Ho, Ho, Ho!"
#     {     }
#      `---'
##--------------------------------------------
#DAY 1
import re
f = open("ELFLIST.txt", "r")
total = 0
for li in f:
    elfdata = re.sub("[^0-9]", "", li)
    num1 = elfdata[0]
    num2 = elfdata[-1]
    total += int(num1+num2)
f.close()
print(total)
##--------------------------------------------
#DAY 2

##--------------------------------------------
#Day 3

##--------------------------------------------
