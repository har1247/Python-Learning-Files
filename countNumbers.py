import re
filename = input("Enter a file name")
fh = open(filename)
numbers = list()


for i in fh:
    i = i.rstrip()
    tmp = re.findall('[0-9]+',i)
    k=0
    if tmp != []:
        for j in tmp:
            num = int(tmp[k])
            numbers.append(num)
            k = k+1
print(sum(numbers))
