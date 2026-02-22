"""
10. Блек-джек

Костя так и не смог завязать с азартными играми. 
Но перед тем как в очередной раз всё проиграть, он решил как следует подготовиться. 
И написать программу, на которой он будет тренироваться играть в блек-джек.

Блек-джек также известен как 21. 
Суть игры проста: 
- нужно или набрать ровно 21 очко, или набрать очков больше, чем в руках у дилера, но ни в коем случае не больше 21. 
- Если игрок собирает больше 21, он «сгорает». 
- В случае ничьей игрок и дилер остаются при своих.

- Карты имеют такие «ценовые» значения:
  -- от двойки до десятки — от 2 до 10 соответственно;
  -- у туза 1 или 11 (11 пока общая сумма не больше 21, далее 1);
  -- у «картинок» (король, дама, валет) — 10.

- Напишите программу, которая вначале случайным образом выдаёт пользователю и компьютеру по две карты 
  и затем запрашивает у пользователя действие: взять карту или остановиться. 
- На экран должна выдаваться информация о руке пользователя. 
- После того как игрок останавливается, выведите на экран победителя.

Реализуйте игру с 3 колодами.
"""
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.unic = {"Hearts": f"\033[91m{chr(9829)}\033[0m", "Diamonds": f"\033[96m{chr(9830)}\033[0m",
                     "Clubs": f"\033[98m{chr(9827)}\033[0m", "Spades": f"\033[90m{chr(9824)}\033[0m"}

    def __repr__(self):
        return f"{self.unic[self.suit]}{self.value}"


class Deck:
    def __init__(self, start=2, shuffle=True):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self.cards = [Card(s, v) for v in values[start-2:] for s in suits]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, k):
        return [self.cards.pop() for _ in range(k)]


class Player:
    count = 0
    def __init__(self, name):
        self.name = name
        Player.count += 1
        self.id = Player.count


class BlackJack:
    def __init__(self, count_deck=3):
        self.players = []
        self.d = Deck(shuffle=False)
        for _ in range(count_deck - 1):
            self.d.cards.extend(Deck(shuffle=False).cards)
        self.d.shuffle()

    def add_player(self, name):
        p = Player(name)
        self.players.append(p)
        print(f"{name} connected to game (id={p.id}).")

    def remove_player(self, id):
        for p in self.players:
            if p.id == id:
                self.players.remove(p)
                print(f"{p.name} go to sleep ZZZzzz...")

    def score(self, lst):
        sc = 0
        count_A = 0
        for c in lst:
            if c.value == "A":
                count_A += 1
            elif c.value in ("J", "Q", "K"):
                sc += 10
            else:
                sc += int(c.value)
        if count_A - 1 > 0:
            sc += count_A - 1
        if count_A > 0:
            if sc <= 10:
                sc += 11
            else:
                sc += 1
        return sc

    def round(self):
        dealer = self.d.deal(2)
        print("dealer cards:", dealer, "score =", self.score(dealer))
        while self.score(dealer) < 17:
            dealer.append(self.d.deal(1)[0])
            print("dealer cards:", dealer, "score =", self.score(dealer))
        if self.score(dealer) > 21:
            print("Dealer loose, game over")
            print("Players win!!!")
            return
        player_cards = {p.name: self.d.deal(2) for p in self.players}
        for name, cards in player_cards.items():
            print(f"{name}'s cards: {cards}, score = {self.score(cards)}")
            while True:
                com = input("Do you want an another card (Y / N): ").lower().strip()
                if com == "n":
                    break
                elif com == "y":
                    cards.append(self.d.deal(1)[0])
                    print(f"{name}'s cards: {cards}, score = {self.score(cards)}")
                else:
                    print("Invalid command.")
                if self.score(cards) > 21:
                    print(f'{name} lost the game, score > 21')
                    break
        global winner_score
        global winner_name
        winner_score = 0
        winner_name = ''
        tie = False
        for name, cards in player_cards.items():
            if self.score(cards) > 21:
                continue
            if winner_score < self.score(cards):
                winner_name = name
                winner_score = self.score(cards)
        print(winner_name, winner_score)
        if winner_score < self.score(dealer):
            winner_name = "DEALER"
            winner_score = self.score(dealer)
        elif winner_score == self.score(dealer):
            tie = True

        if tie:
            print(f'{winner_name} and DEALER ended game tie. Their score = {winner_score}')
        else:
            print(f'{winner_name} won, score = {winner_score}')


    def game(self):
        my_dict = {}
        while True:
            self.round()
            if winner_name in my_dict:
                my_dict[winner_name] += 1
            else:
                my_dict[winner_name] = 1
            con = input("If you want play more write C else E " )
            if con.lower() == "e":
                print(my_dict)
                return
    


# g = BlackJack()
# g.add_player("Varduhi")
# g.add_player("Artur")
# g.game()



"""• Create a Computation class with a default constructor (without parameters)
allowing to perform various calculations on integers numbers.
• Create a method called factorial() which allows to calculate the factorial of an
integer.
• Create a method called sum() allowing to calculate the sum of the first n
integers 1 + 2 + 3 + .. + n.
• Create a method called is_prime() allowing to test the primality of a given
integer.
• Create a method called all_is_prime() allowing to display all prime integer
numbers from 2 to n.
• Create a table_mult() method which creates and displays the multiplication
table of a given integer (from 1 to 10).
• Then create an all_tables_mult() method to display all the integer
multiplication tables (from 1 to 10)."""

class Computation:
    def factorial(self, number):
        res = 1
        for i in range(1, number + 1):
            res *= i
        return res
    
    def sum(self, number):
        res = 0
        for i in range(1, number + 1):
            res += i
        return res
    
    def is_prime(self, number):
        if number < 2:
            return False
        elif number == 2:
            return True
        else:
            for i in range(2, int(number / 2) + 1):
                if number % i == 0:
                    return False
        return True
    
    def all_is_prime(self, number):
        primes = []
        for i in range(1, number + 1):
            if Computation.is_prime(self, i):
                primes.append(i)
        return primes

    def mult_table(self, number):
        for i in range(1, 11):
            print(f'{number} x {i} = {number * i}')

    def all_mult_table(self):
        for i in range(1, 11):
            Computation.mult_table(self, i)
            print()


obj1 = Computation()


# print(obj1.factorial(1558))
# print()
# print(obj1.sum(100))
# print()
# print(obj1.is_prime(7))
# print()
# print(obj1.all_is_prime(100))
# print()
# obj1.mult_table(7)
# print()
# obj1.all_mult_table()
