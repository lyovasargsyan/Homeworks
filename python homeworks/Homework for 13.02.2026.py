# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա 
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։

class MyShows:
    def __init__(self,  serial_name, place, year_of_first_serial, actors_name_surname, number_seria=1, rate=None):
        if isinstance(serial_name, str):
            self.__serial_name = serial_name
        else:
            print("Serial name type is wrong")
        if isinstance(place, str):
            self.__place = place
        else:
            print("place type is wrong")
        if isinstance(year_of_first_serial, int):
            self.__year_of_first_serial = year_of_first_serial
        else:
            print("Year of first serial type is wrong")
        if isinstance(number_seria, int):
            self.__number_seria  = number_seria
        else:
            print("Number type is wrong")
        if isinstance(rate, int) and rate >= 1 and rate <= 10:
            self.__rate = rate
        else:
            print("Rate type is wrong")
        if isinstance(actors_name_surname, list) and all(isinstance(str, i) for i in actors_name_surname):
            self.__actors_name_surname = actors_name_surname
        else:
            print("Actors name surname type is wrong")

    @property
    def serial_name_(self):
        print('Get serial name', end=' ')
        return self.__serial_name
    
    @property
    def place_(self):
        print('Get place:', end=' ')
        return self.__place
    
    @property
    def year_of_first_serial_(self):
        print('Get year of first serial:', end=' ')
        return self.__year_of_first_serial
    
    @property
    def number_seria_(self):
        print('Get number seria:', end=' ')
        return self.__number_seria
    
    @property
    def rate_(self):
        print('Get rate:', end=' ')
        return self.__rate 

    @property
    def actors_name_surname_(self):
        print('Get actors name surname:', end=' ')
        return self.__actors_name_surname

    @number_seria_.setter
    def number_seria_(self, value):
        print(f'Set number seria: {value}')
        self.__number_seria = value

    @rate_.setter
    def rate_(self, value):
        print(f'Set rate: {value}')
        self.__rate = value

    @rate_.deleter
    def rate_(self):
        print("Delete rate")
        self.__rate = None
    
    def add_actor_name(self, name_surname):
        if isinstance(name_surname, str):
            self.__actors_name_surname.append(name_surname)
        else:
            print("Name or surname type is wrong")

    def del_actor_name(self, name_surname):
        if name_surname in self.__actors_name_surname:
            self.__actors_name_surname.remove(name_surname)
        else: 
            print("There is no actor with that name surname")

    def get_full_info(self):
        return (
            f"Name: {self.__serial_name}\n"
            f"Platform: {self.__place}\n"
            f"Year: {self.__year_of_first_serial}\n"
            f"Reached: {self.__number_seria}\n"
            f"Rating: {self.__rate}\n"
            f"Actors: {', '.join(self.__actors_name_surname)}"
        )


