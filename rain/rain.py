import time,random

items = [unichr(i) for i in range(0x30a1,0x30ff + 1)]
for i in range(1,11):
    items.append(str(i))
    items.append(" "*i)

def rain(row,column):
     for i in range(row):
             s = ''
             for j in range(column):
                     ri = random.randrange(len(items))
                     s += items[ri]
             print(s)
             time.sleep(0.05)            
