# 3․ Գրել ֆունկցիա, որը․
#    - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
#      (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
#    օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
#            output = ["aba", "vcd", "aba"],
           
#            input = ["aba", "aa", "z", "advc", "vcd", "aba"]
#            output = ["advc"],


#O(n) 
def filterWords(lst):
    maxLenght = 0
    newlst = []
    for words in lst:
        if len(words) >= maxLenght:
            maxLenght = len(words)
    for word in lst:
        if len(word) == maxLenght:
            newlst.append(word)
    return newlst

