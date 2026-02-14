# 3. Գրեք հետևյալ կլասները.

#    - Ստեղծեք Car class, որը ներկայացնում է մեքենա, որը կարելի է կայանել ավտոկայանատեղիում:
#      Car class-ը ստեղծման ժամանակ պետք է տրամադրվի car_id ատրիբուտով: 
#      Բոլոր հետագա գործողությունները պետք է հաշվի առնեն car_id-ն։

#    - Ստեղծեք ParkingLot class, որը կառավարում է մեքենաների կայանումը: 
#      Այս class-ը մի քանի գործառույթներ ունի. 
#      -- այն պետք է օգնի կայանել մեքենան, 
#      -- բաց թողնել մեքենան 
#      -- և հաղորդել ազատ մնացած տեղերի քանակը:

#      ParkingLot class-ը պետք է ունենա հետևյալ ատրիբուտները և մեթոդները.

#      -- total_spots ատրիբուտ - ավտոկայանատեղիում կայանատեղերի ընդհանուր թիվը, 
#                                որը պետք է տրամադրվի կայանատեղիի օբյեկտի ստեղծման ժամանակ,
#      -- park(car) մեթոդ - կայանում է մեքենան (Car) ավտոկայանատեղիում: 
#         Եթե ավտոկայանատեղին ամբողջությամբ զբաղված է, այն պետք է տպի՝ Parking lot is full։
#      -- release(car) մեթոդ - ավտոմեքենան (Car) բաց է թողնում ավտոկայանատեղից։ 
#         Եթե մեքենան կայանատեղիում չէ, պետք է տպի` Car not found in the parking lot։
# 	Եթե մեքենան կայանատեղիում է, պետք է հարցնի մեքենայի վարորդից input-ի միջոցով թե քանի ժամ է մեքենան գտնվել ավտոկայանատեղիում 
#         և գանձի համապատասխան վճարը (1 ժամ - 500 դրամ)։
#      -- spots_left() մեթոդ - վերադարձնում է կայանատեղիում առկա կայանման տեղերի քանակը:
#      -- cash_register() մեթոդ - վերադարձնում է գանձված վճարների գումարը կայանված ավտոմեքենաներից։

class Car:
    cars = 0

    def __init__(self):
        Car.cars += 1
        self.id = Car.cars

car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()
car5 = Car()
car6 = Car()
car7 = Car()


class Parkinglot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.money = 0
        self.cars = []

    def park(self, car):
        if len(self.cars) == self.total_spots:
            print("There is no free spots in parking.")
        else:
            self.cars.append(car.id)
            print(f"Car parked. There is {self.total_spots - len(self.cars)} free spots yet.")


    def release_car(self, car):
        if car.id in self.cars:
            time = int(input('Please write how many ours your car was parked in parking. '))
            print(f'You need pay {time *  500}... Money was paid...')
            self.money += time * 500
            print(f"{car.id} car released form parking.")
            self.cars.remove(car.id)
        else:
            print(f'{car.id} car is not parked in parking.')

    def spots_left(self):
        print(f"There is {self.total_spots - len(self.cars)} free spots yet.")
        

    def cash_register(self):
        print(f'You have {self.money}')



p = Parkinglot(5)

p.park(car1)
p.park(car2)
p.park(car3)
p.park(car4)
p.park(car5)
p.park(car6)
p.park(car7)

p.release_car(car4)
p.release_car(car5)
p.release_car(car6)

p.spots_left()
p.cash_register()
