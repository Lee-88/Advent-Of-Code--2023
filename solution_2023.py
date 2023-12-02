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
#--------------Part 2
import re
f = open("ELFLIST.txt", "r")
total = 0
for li in f:
    elfdata = li.replace("one", "o1e")
    elfdata = elfdata.replace("two", "t2o")
    elfdata = elfdata.replace("three", "t3e")
    elfdata = elfdata.replace("four", "f4r")
    elfdata = elfdata.replace("five", "f5e")
    elfdata = elfdata.replace("six", "s6x")
    elfdata = elfdata.replace("seven", "s7n")
    elfdata = elfdata.replace("eight", "e8t")
    elfdata = elfdata.replace("nine", "n9e")
    elfdata = re.sub("[^1-9]", "", elfdata)
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
