# 2․ Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX:


# O(1)
n = 0
def RomanNum(number):
    romNum = ""
    if number // 1000 != 0:
        romNum += (number // 1000) * "M"
        number %= 1000
    if number // 100 != 0:
        if number // 100 < 4:
            romNum += (number // 100) * "C"
        elif number // 100 == 4:
            romNum += "CD"
        elif number // 100 == 5:
            romNum += "D"
        elif number // 100 < 9:
            romNum += "D" + ((number // 100) - 5) * "C"
        else:
            romNum += "CM"
        number %= 100
    if number // 10 != 0:
        if number // 10 < 4:
            romNum += (number // 10) * "X"
        elif number // 10 == 4:
            romNum += "XL"
        elif number // 10 == 5:
            romNum += "L"
        elif number // 10 < 9:
            romNum += "L" + ((number // 10) - 5) * "X"
        else:
            romNum += "XC"
        number %= 10
    if number // 1 != 0:
        if number // 1 < 4:
            romNum += (number // 1) * "I"
        elif number // 1 == 4:
            romNum += "IV"
        elif number // 1 == 5:
            romNum += "V"
        elif number // 1 < 9:
            romNum += "V" + ((number // 1) - 5) * "I"
        else:
            romNum += "IX"
        number %= 1
    return romNum
