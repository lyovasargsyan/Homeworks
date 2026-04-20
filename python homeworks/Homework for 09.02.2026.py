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
        pin = input("\033[92mPlease write your pin code: \033[0m")
        while BankUser.count < 2:
            if self.__pin_code == pin:
                BankUser.count = 0
                return True
            else:
                pin = input("\033[93mPlease input valid code: \033[0m")
                BankUser.count += 1
        return False


    def get_name_surname(self):
        print(f'\033[94m{self._name} {self._surname}\033[0m')
        
    def get_carnum_money(self):
        if BankUser.count != 2:
            if self.valid_pin():
                print(f'\033[96mCard number is: {self.__card_num}\033[0m')
                print(f'\033[96mMoney on card: {self.__money_on_card}\033[m')
            else:
                print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")
        else:
            print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")
        
    def cash_in(self):
        if BankUser.count != 2:
            if self.valid_pin():
                cashin_size = int(input("\033[92mNow cash in money\n\033[0m"))
                self.__money_on_card += cashin_size
                print(f'\033[96mMoney on card: {self.__money_on_card}\033[m')
            else:
                print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")
        else:
            print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")


    def cash_out(self):
        if BankUser.count != 2:    
            if self.valid_pin():
                cashout_size = int(input("\033[92mNow cash out money\n\033[0m"))
                if self.__money_on_card - cashout_size >= 0:
                    self.__money_on_card -= cashout_size
                    print(f'\033[96mMoney on card: {self.__money_on_card}\033[m')
            else:
                print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")
        else:
            print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\033[0m")

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
            print("\033[95mEmail sent successfully!\033[0m")
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

        ver_code = int(input("\033[93mPlease input code sent to your Email\033[0m "))
        while True:
            if ver_code == verification_code:
                BankUser.count = 0
                print("\033[92mYour card is unblocked:):)\033[0m")
                return 0
            else:
                ver_code = int(input("\033[92mPlease input right code sent to your Email\n \033[0m"))

    
    def function_chooser(self):
        my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
        while(True):
            if my_function.lower() == "end":
                print("\033[92mThank you! You chose end.\033[0m")
                return
            elif my_function.lower() == "cash in":
                BankUser.cash_in(self)
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
            elif my_function.lower() == "cash out":
                BankUser.cash_out(self)
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
            elif my_function.lower() == "get card number and money size on card":
                BankUser.get_carnum_money(self)
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0mcS")
            elif my_function.lower() == "get name and surname":
                BankUser.get_name_surname(self)
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
            elif my_function.lower() == "card status":
                if BankUser.count == 2:
                    print("\033[91mYour card is Blocked!! Apply bank to unblock your card.\n\033[0m")
                else:
                    print(f"\033[92mYour card is not Bloked. You still have {(2 - BankUser.count) + 1} chance to write your pin code.\n\033[0m")
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
            elif my_function.lower() == "unblock card":
                if BankUser.count == 2:
                    BankUser.unblock_card(self)
                    my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
                else:
                    print("\033[93mYou card is not bloked\033[0m")
                    my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")
            else:
                print("\033[97mPlease input valid function name. You can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\n\033[0m")
                my_function = input("\033[92mNow you can \033[95mcash in, cash out, get card number and money size on card, get name and surname, card status.\033[0m \033[92m\nWrite the name function you want use or write END to end use the program.\n\033[0m")


                
    
obj1 = BankUser("Lyova", "Sargsyan", 17, "lyovasargsyan2008@gmail.com", "4083 0900 1009 3816", 5000, "6565")
obj1.function_chooser()




