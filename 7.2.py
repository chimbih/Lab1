
fname = input("Enter file name: ")
fh = open(fname, 'r')
print(fh)
for line in fh:
    count=0
    total=0
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line.rstrip()[20:])
#print(float(line[20:]))

num = 0
tot = 0.0
while True:
    sval = input('Enter confidence: ')
    #fval = float(sval)
    #print(fval)
    if sval == 'done':
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
print(tot, num, tot/num)
print('Avg confidence: ', tot/num)


