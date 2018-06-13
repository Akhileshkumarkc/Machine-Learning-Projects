def isPermutation(string1, string2):
    stringlist1 = []
    stringlist2 = []
    for word1 in string1:
        stringlist1.append(word1)
    for word2 in string2:
        stringlist2.append(word2)
    number=0
    for item in stringlist1:
        if item in stringlist2:
            number+=1
            stringlist2.remove(item)
        else:
            return False
    for i in range(number):
        stringlist1.pop(0)


    if ((len(stringlist1)==0) & (len(stringlist2) == 0)):
        return True
    return False

print(isPermutation('abc','cba'))
print(isPermutation('abc','cbe'))
print(isPermutation('abcd','cba'))
print(isPermutation('abcd','cbad'))
print(isPermutation('aaaa','aaab'))
print(isPermutation('',''))
print(isPermutation('','a'))
print(isPermutation('a',''))