// >>>ord('a')
// 97
// >>> ord('b')
// 98
// >>> ord('c')
// 99
-------------
// >>> chr(48)
// 0
// chr(49)
// 1
// chr(97)
// a

def formatStrToInt(target):
    for i in range(len(target)):
        temp=ord(target[i])
        print temp,
    return
formatStrToInt("abcdefghijk")
 
结果如下：
======================= RESTART =======================
97 98 99 100 101 102 103 104 105 106 107
