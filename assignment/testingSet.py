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
            print("Cost should be above 0, setting it to the default value of 0")
            self.cost = 0      
        else :
            self.cost = cost
        
    def getCost(self):
        return self.cost

    def setEarnings(self, earnings):      
        if earnings < 0: 
            print("earnings should be above 0, setting it to the default value of 0")
            self.earnings = 0      
        else :
            self.earnings = earnings


    def getEarnings(self):
        return self.earnings

    def setYear(self, year):
        if year < 1960 or year > 2022: 
            print("Year should be Between 1960 - 2020, setting it to the default value of 2000")
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
    def __init__(self, title, cost, earnings, year, multiplayer, online):
        super().__init__(title, cost, earnings, year)

        self.multiplayer = multiplayer
        self.online = online 

    # Declaring mutator (set) & accessor (get)
    def getMultiplayers(self):
        return self.multiplayer

    def setMultiplayers(self, number):
        self.multiplayer = number

    def onlineGame(self):
        if self.online == True:
            print("This is an online game ")
        else:
            print("This is not an online game")


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

    @abstractmethod 
    def onlineGame(self):
        pass

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
        self.setSalary(salary)
        self.setHasATeam(hasATeam)
        self.Game = game
    
    # Declaring mutator (set) & accessor (get)
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        #self.salary = salary
        if salary < 0: 
            print("Salary should be above 0, setting it to the default value of 0")
            self.salary = 0      
        else :
            self.salary = salary

    def setHasATeam(self, team):
        #self.hasATeam = team
        if team < 0 or team > 10: 
            print("Team should be between 0 - 10 , setting it to the default value of 0")
            self.hasATeam = 0      
        else :
            self.hasATeam = team

    def getHasATeam(self):
        return self.hasATeam

    def __str__(self):
        return f"The developer name is {self.name}\nThe salary made was {self.salary}\nThere is a team of {self.hasATeam} developers\n{self.Game}" 

game1 = Game("GTA", 99, 7348678568349, 1992)

game1.setTitle("GTA 5")
game1.setCost(50)
game1.setEarnings(999999)
game1.setYear(1998)
#print(game1.getCost())
#print(game1.getYear())
#print(game1.getEarnings())
#print(game1.getTitle())
#print(game1)
#print(game2)



developer1 = Developer("Kian Barker", 100000, 4, game1)

developer1.setSalary(9)
developer1.setHasATeam(1)

#print(developer1)

game3 = Fps("Overwatch", 10, 555555555, 2018, "2-4", True)


#print(game3)

game3.onlineGame()




