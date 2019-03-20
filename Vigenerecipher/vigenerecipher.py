keys = input("Enter your encryption key")
filename =  input("What file do you want to encrypt?")
print(filename)
def getmsg(filename):
    s=""
    fn = open(filename)
    for line in fn:
        line = line.upper()
        for ch in line:
            if ord(ch) >= 65 and ord(ch) <=90 or ch.isdigit():
                s=s+ch
    print(s)
    return s

def placer(msg,keys):
    keyPlacer=""
    j=0
    for i in msg:
        if j>=len(keys):
            j=0
        if i.isdigit():
            keyPlacer = keyPlacer + " "
        keyPlacer = keyPlacer + keys[j]
        j=j+1
    return keyPlacer


def shifting(msg,keyGenerator):
    securemsg=""
    j=0
    for i in msg:
        if i.isdigit():
            securemsg = securemsg + i
            j=j+1
            continue
        c = (ord(msg[j]) + ord(keyGenerator[j])) - 65
        if c>90:
            c = (c-90) + 64
        securemsg = securemsg + chr(c)
        j=j+1
    print(securemsg)
    return securemsg


def writingFile(encryptmsg,filename):
    efile = "e"+filename
    fn = open(efile,"w+")
    for i in encryptmsg:
        fn.write(i);
    fn.close()
    print("Encrypted file has been saved")


msg = getmsg(filename)
keyGenerator=placer(msg,keys)
encryptedmsg = shifting(msg,keyGenerator)
writingFile(encryptedmsg,filename)
