# 5. Ռեստորանային ամրագրումներ

#    Սույն առաջադրանքում դուք պետք է նախագծեք ռեստորանային ցանցի կառավարման համակարգը:

#    - Restaurant անունով Python class-ը պետք է ունենա 
#      -- երկու մեթոդ՝ make_reservation և order_food,
#      -- երկու ատրիբուտ՝ ռեստորանի անունը և սեղանների քանակը։

#    - Այնուհետև դուք պետք է ստեղծեք մեկ այլ class՝ FastFoodRestaurant, որը ժառանգում է Restaurant կլասից 
#      և փոփոխում է make_reservation մեթոդը՝ միշտ տպելով՝ We do not take reservations.։

#    - Restaurant-ը ունի սահմանափակ թվով սեղաններ։

#    - make_reservation մեթոդը պետք է ունենա 3 պարամետր՝ 
#      -- անձի անունը, 
#      -- ամրագրվող սեղանների թիվը,
#      -- ամսաթիվը՝ yyyy-mm-dd ձևաչափով:

#      Յուրաքանչյուր ամրագրումը կատարվում է ամբողջ օրվա համար:

#      make_reservation մեթոդը պետք է կարգավորի սա և տպի No seats available, եթե պահանջվող օրվա համար ազատ սեղաններ չկան:
   
#    - Եթե ամրագրումը կատարվում է, make_reservation մեթոդը պետք է տպի 
#      Reservation made for <name> at <date> ձևաչափով հաղորդագրություն։

#    - order_food մեթոդը պետք է ընդունի կամայական քանակի արգումենտներ 
#      և տպի նամակ՝ հետևյալ ձևաչափով՝ Order with <item1>, <item2>, ..., <item_n> placed!։

class Restaurant:
    def __init__(self, name, table_quantity):
        self.name = name
        self.table_quantity = table_quantity
        self.reserve = {}

    def make_reservation(self, name, number, date):
        if self.reserve.get(str(date), 0) == self.table_quantity:
            print(f'No seats available on {date}.')
        elif self.reserve.get(str(date), 0) + number > self.table_quantity:
            print(f'No {number} seats available on {date}.')
        else:
            print(f'Reservation made for {name} at {date}․')
            self.reserve[str(date)] = self.reserve.get(str(date), 0) + number
    
    def order_food(self):
        order_list = []
        while(True):
            order = input("Please input name of food you want order or write end to end the list. ")
            if order.lower() == "end":
                print(", ".join(order_list))
                return
            else: 
                order_list.append(order)
        

class FastFoodRestaurant(Restaurant):
    def __init__(self, name, table_quantity = 0):
        self.name = name

    def make_reservation(self, *args,):
        print("We do not take reservations.")

    


restaurant = Restaurant('Paradise', 5)
restaurant.make_reservation('Anna', 2, '2024-05-06')

restaurant.make_reservation('Ashot', 3, '2024-05-07')
restaurant.make_reservation('Mary', 1, '2024-05-07')
restaurant.make_reservation('Lilit', 2, '2024-05-07')

fast_food = FastFoodRestaurant('Burger World')
fast_food.make_reservation('John', 2, '2023-10-24')
fast_food.order_food()

