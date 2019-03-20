arr=[]
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        inum = int(num)
        arr.append(inum)

    except:
        print("Invalid input")

def smallest(arr) :
    small = None
    for i in arr:
        if small is None :
            small = i
        elif i < small :
        	small = i
    return small


def largest(arr) :
    large = None
    for j in arr:
        if large is None:
            large = j
        elif j > large:
        	large = j
    return large


print("Maximum is", largest(arr))
print("Minimum is", smallest(arr))
