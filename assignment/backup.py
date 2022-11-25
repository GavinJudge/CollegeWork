# Kian Barker, Assignment  
# 07/10/2022


from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, title, cost, earnings, year):
        self.title = title
        self.setCost(cost)
        self.setEarnings(earnings)
        self.setYear(year)

    # Declaring mutator (set) & accessor (get)
    def setTitle(self, name):
        self.title = name

    def getTitle(self):
        return self.title

    def setCost(self, cost):
        if cost < 0: 
            print("Cost should be above 0,\nSetting it to the default value of 0")
            self.cost = 0      
        else :
            self.cost = cost
        
    def getCost(self):
        return self.cost

    def setEarnings(self, earnings):      
        if earnings < 0: 
            print("Earnings should be above 0,\nSetting it to the default value of 0")
            self.earnings = 0      
        else :
            self.earnings = earnings


    def getEarnings(self):
        return self.earnings

    def setYear(self, year):
        if year < 1960 or year > 2022: 
            print("Year should be Between 1960 - 2020,\nSetting it to the default value of 2000")
            self.year = 2000      
        else :
            self.year = year

    def getYear(self):
        return self.year

    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Game to a different object than Game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)

    def __str__(self):
       return f"The name of the game is {self.title} \nThe cost of the game to play is {self.cost} euros\nHow much the game has earned is {self.earnings}\nThe year it was released was {self.year}" 


class Fps(Game):
    def __init__(self, title, cost, earnings, year, multiplayer):
        super().__init__(title, cost, earnings, year)

        self.multiplayer = multiplayer

    # Declaring mutator (set) & accessor (get)
    def getMultiplayers(self):
        return self.multiplayer

    def setMultiplayers(self, number):
        self.multiplayer = number

    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Fps game to a different object than Fps game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)
                

    def __str__(self):
        return super().__str__() + f"\nIt is a multiplyer game with {self.multiplayer} players"  


class Rpg(Game):
    def __init__(self, title, cost, earnings, year, solo):
        super().__init__(title, cost, earnings, year)

        self.solo = solo

    # Declaring mutator (set) & accessor (get)
    def getSolo(self):
        return self.solo 

    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Rpg to a different object than Rpg game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)

    def __str__(self):
        return super().__str__() + f"\nIt can only play as a solo player " 

class Developer:
    def __init__(self, name, salary, hasATeam, game):
        self.name = name
        self.salary = salary
        self.hasATeam = hasATeam
        self.Game = game
    
    # Declaring mutator (set) & accessor (get)
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

    def setHasATeam(self, team):
        self.hasATeam = team

    def getHasATeam(self):
        return self.hasATeam

    def __str__(self):
        return f"The developer name is {self.name}\nThe salary made was {self.salary}\nThere is a team of {self.hasATeam} developers\n{self.Game}" 
    
class GameService:
    def __init__(self, name):
        self.name = name
        self.games = []
        self.maxNumOfGames = 20

    # Declaring mutator (set) & accessor (get)
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def addGame(self, Game):
        if len(self.games) < self.maxNumOfGames:
            if Game not in self.games:
                self.games.append(Game)
            else:
                print("This game is already in the Game service")
        else:
            print("The gaming service is full")

    def removeGame(self, Game):
        if Game in self.games:
            self.games.remove(Game)
        else:
            print("This is not in your Gaming service: " + Game.name)

    def searchForGame(self, Game):
        if Game in self.games:
            return True
        else:
            return False
   

    def __str__(self):
        tempString = ""

        for x in self.games:
            tempString += x.getTitle() + "\n"

        return f"The name of the gaming service is {self.name}\nThe list of games are.\n{tempString}"


game1 = Game("GTA", 30, 7348678568349, 1992)
game2 = Game("COD", 50, 22000000, 2002)

game6 = Game("GTA", 30, 1000000, 1992)


game3 = Fps("Overwatch", 10, 555555555, 2018, "2-4")
game4 = Rpg("Assains creed", 40, 33333333, 2015, "1 player")
game5 = Rpg("Test game", 20, 3333, 2018, "1 player")
#print(game1)
#print(game4)



game3.setTitle("GTA 5")
game3.setCost(-50)
game3.setEarnings(-9999999)
game3.setYear(19)
#print(game1.getCost())
#print(game1.getYear())
#print(game1.getEarnings())
#print(game1.getTitle())
print(game1)
#print(game2)



'''
developer1 = Developer("Kian Barker", 100000, 4, game1)

#print(developer1)

gameService1 = GameService("First Gaming system")
gameService1.addGame(game1)
gameService1.addGame(game2)
#gameService1.addGame(game2)
gameService1.addGame(game3)
gameService1.addGame(game4)
gameService1.addGame(game5)
gameService1.removeGame(game5)
print(gameService1)


print(gameService1.searchForGame(game1))

print(game1 == game2)
print(game1 == game6)
'''
