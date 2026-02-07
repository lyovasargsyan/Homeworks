# 1․ Գրել BankUser class, որը․
#    - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, էլեկտրոնային փոստը, քարտը, գումարը քարտի վրա, pin կոդը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
#      -- անունը և ազգանունը - տառերից բաղկացած,
#      -- տարիքը - բնական թիվ,
#      -- էլեկտրոնային փոստ - տեքստ (գրեք նվազագույն պայմաններ էլեկտրոնային փոստի ճշտությունը ստուգելու համար),
#      -- քարտի համարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
#                        քարտի համարի ճշտությունը ստուգեք Լունայի ալգորիտմի միջոցով 
#                      (https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D1%83%D0%BD%D0%B0)
#      -- գումարը - դրական թիվ,
#      -- pin կոդը - 4 թվանշանից բաղկացած տեքստ,
#    - անունը, ազգանունը, տարիքը և էլեկտրոնային փոստը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
#    - քարտի համարը, գումարը և pin կոդը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
#    - կունենա մեթոդ, որը կվերադարձնի մարդու անունը և ազգանունը,
#    - կունենա մեթոդ, որը կվերադարձնի քարտի համարը և գումարը, բայց միայն ճիշտ pin կոդը հավաքելուց հետո,
#    - կունենա մեթոդ, որը կավելացնի գումար հաշվին, բայց միայն ճիշտ pin կոդը հավաքելուց հետո,
#    - կունենա մեթոդ, որը կհանի գումար հաշվից, բայց միայն ճիշտ pin կոդը հավաքելուց հետո,
#      հաշվի առեք, որ գումարը բացասական չի կարող լինել,
#    - 3 անգամ սխալ pin կոդը հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված,
#    - կունենա մեթոդ, որի միջոցով կվերականգնվի հասանելիությունը 6-անիշ թիվ մուտքագրելու դեպքում, որը կուղարկվի էլ․ փոստին (կարող եք օգտագործել smtplib գրադարանը պատահական 6-անիշ թիվ գեներացնելու և էլ․ փոստին ուղարկելու համար)։
# cdpv xihw wbze guez
import re
import smtplib
from email.message import EmailMessage
import random



class BankUser:
    @classmethod
    def real_card(cls, card_number):
        cls.card_number = card_number
        total = 0
        cls.card_number = cls.card_number.split()
        number = ""
        for i in cls.card_number:
            number += i
        cls.card_number = number     
        digits = list(map(int, cls.card_number))
        digits.reverse()

        for i in range(len(digits)):
            if i % 2 == 1:
                doubled = digits[i] * 2
                if doubled > 9:
                    doubled = doubled - 9
                total += doubled
            else:
                total += digits[i]
        return total % 10 == 0


    @classmethod
    def valid_type_card_num(cls, card_number):
        cls.card_number = card_number
        pattern = r'\d{4} *\d{4} *\d{4} *\d{4}' 
        return bool(re.fullmatch(pattern, cls.card_number))


    def __init__(self, name, surname, age, email, card_num, money_on_card, pin_code):
        if name.isalpha(): 
            self._name = name
        else: 
            raise ValueError("Provided name is wrong! Name can have only letters.")

        if surname.isalpha():
            self._surname = surname
        else:
            raise ValueError("Provided surname is wrong! Surame can have only letters.")
        
        
        if age == int(age):
            self._age = age
        else:
            raise ValueError("Provided age is wrong! Age needs to be Natural number.")
        
        if "@" in email and "." in email:
            self._email = email
        else:
            raise ValueError("Provided Email is wrong! Email needs to be have @ and .")
        
        if self.valid_type_card_num(card_num) and self.real_card(card_num):
            self.__card_num = card_num
        else:
            raise ValueError("Provided card number is wrong! Enter valid card number")
                
        if money_on_card >=0:
            self.__money_on_card = money_on_card
        else:
            raise ValueError("Provided money on card is wrong! Money on card can not be negative number")
        
        if len(pin_code) >= 4 and int(pin_code) >= 0:
            self.__pin_code = pin_code
        else:
            raise ValueError("Provided pin code is wrong! Pin code needs to have at least 4 digit")
        
    count = 0

    def valid_pin(self):
        pin = input("Please write your pin code: ")
        while BankUser.count < 2:
            if self.__pin_code == pin:
                BankUser.count = 0
                return True
            else:
                pin = input("Please input valid code: ")
                BankUser.count += 1
        return False


    def ret_name_surname(self):
        print(self._name, self._surname)
        
    def ret_carnum_money(self):
        if BankUser.count != 2:
            if self.valid_pin():
                print("Card number is: ", self.__card_num)
                print("Money on card: ", self.__money_on_card)
            else:
                print("Your card is Blocked!! Apply bank to unblock your card.")
        else:
            print("Your card is Blocked!! Apply bank to unblock your card.")
        
    def add_money(self):
        if BankUser.count != 2:
            if self.valid_pin():
                cashin_size = int(input("Now cash in money\n"))
                self.__money_on_card += cashin_size
                print("Money on card:", self.__money_on_card)
            else:
                print("Your card is Blocked!! Apply bank to unblock your card.")
        else:
            print("Your card is Blocked!! Apply bank to unblock your card.")


    def cash_out(self):
        if BankUser.count != 2:    
            if self.valid_pin():
                cashout_size = int(input("Now cash out money\n"))
                if self.__money_on_card - cashout_size >= 0:
                    self.__money_on_card -= cashout_size
                    print("Money on card:", self.__money_on_card)
            else:
                print("Your card is Blocked!! Apply bank to unblock your card.")
        else:
            print("Your card is Blocked!! Apply bank to unblock your card.")

    def unblock_card(self):
        email_address = "lyovasargsyan2008@gmail.com"
        email_password = "cdpv xihw wbze guez" 

        msg = EmailMessage()
        msg['Subject'] = "Unblocking code for your bank card"
        msg['From'] = email_address
        msg['To'] = self._email
        verification_code = random.randint(100000, 999999)
        msg.set_content(f'Hello! For unblock your card in app input this number: {verification_code}')

        try:
            # Gmail SMTP server settings
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")

        ver_code = int(input("Please input code sent to your Email"))
        while True:
            if ver_code == verification_code:
                BankUser.count = 0
                print("Your card is unblocked:):)")
                return 0
            else:
                ver_code = int(input("Please input right code sent to your Email\n"))


                
        



obj1 = BankUser("Lyova", "Sargsyan", 17, "karensargsyan74@gmail.com", "4083 0900 1009 3816", 5000, "6565")
obj1.ret_name_surname()
obj1.ret_carnum_money()
# obj1.add_money()
obj1.unblock_card()
obj1.cash_out()





