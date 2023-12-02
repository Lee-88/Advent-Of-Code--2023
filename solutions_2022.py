#    .-""-.
#   /,..___\   My Completed Advent Of Code Solutions for 2022
#  () {_____}
#    (/-@-@-\)
#    {`-=^=-'}
#    {  `-'  } "Ho, Ho, Ho!"
#     {     }
#      `---'
#D4 p1
f = open("ELFLIST.txt", "r")
total = 0
def checkElves (a,b,c,d):
    global total
    if ((a <= c and d <= b) or (c <= a and b <= d)):
            total += 1
for li in f:
    elfdata = li.split(",")
    a, b = map(int, elfdata[0].split('-'))
    c, d = map(int, elfdata[1].split('-'))
    checkElves (a,b,c,d)
f.close()
print(total)
##--------------------------------------------
#D4 p2
f = open("ELFLIST.txt", "r")
total = 0
def checkElves (a,b,c,d):
    global total
    if ( c >= a and c <= b) or (a >= c and  a <= d):
            total += 1
for li in f:
    elfdata = li.split(",")
    a, b = map(int, elfdata[0].split('-')) 
    c, d = map(int, elfdata[1].split('-'))
    checkElves (a,b,c,d)
f.close()
print(total)
##--------------------------------------------
#d5 P1
import re
f = open("day5.txt", "r")
c1 = ['R','N','F','V','L','J','S','M']
c2 = ['P','N','D','Z','F','J','W','H']
c3 = ['W','R','C','D','G']
c4 = ['N','B','S']
c5 = ['M','Z','W','P','C','B','F','N']
c6 = ['P','R','M','W']
c7 = ['R','T','N','G','L','S','W']
c8 = ['Q','T','H','F','N','B','V']
c9 = ['L','M','H','Z','N','F']
def move(m,f,t):
    for i in range(m):
        print(t)
        t.append(f.pop())
def moveMulti(m,f,t):
    temp = []
    for i in range(m):
        temp.append(f.pop())
    move(m, temp, t)
def getLayer():
    top = ""
    for i in range(9):
        top += eval('c%s[-1]' % str(i+1))
    return top
for li in f:
    command = re.findall(r'\d+', li) 
    m, f, t = map(int, command)
    print(  "Move " +str(m) + " from " + str(f) +" to "+ str(t))
    #part 1 
    #move(m, eval('c%s' % f), eval('c%s' % t))
    #part 2
    moveMulti(m, eval('c%s' % f), eval('c%s' % t))
getLayer()
##--------------------------------------------
#D6 P1
f = open("day6.txt", "r")
signal = f.read()
mem_buff = set()
bits = 0
connected = False
def check():
    for x in range(4):
        global connected
        mem_buff.add(signal[bits+x])
        if len(mem_buff)==4:
            connected = True
            print(bits+4)
for i in range(len(signal)-4):
    if  connected is not True:
        bits+=1
        check()
        mem_buff.clear()
##--------------------------------------------
#D6 P2
f = open("day6.txt", "r")
signal = f.read()
mem_buff = set()
bits = 0
connected = False
def check():
    for x in range(14):
        global connected
        mem_buff.add(signal[bits+x])
        if len(mem_buff)==14:
            connected = True
            print(bits+14)
for i in range(len(signal)-14):
    if  connected is not True:
        bits+=1
        check()
        mem_buff.clear()
##--------------------------------------------
