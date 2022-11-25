# Kian Barker, Lab Assessment Part 1
# Software Development SDEV:4009
# 07/10/2022 - 05/11/2022 

# ABC module for abstract classes 
from abc import ABC, abstractmethod

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Game class use as a parent class to store the name of the game, cost to play, earning the game made, and year it was made
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

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

    # If the cost is below 0, set the default to 0
    def setCost(self, cost):
        if cost < 0: 
            print("Cost should be above 0,\nSetting it to the default value of 0")
            self.cost = 0      
        else :
            self.cost = cost
        
    def getCost(self):
        return self.cost

    # If the earnings is below 0, set the default to 0
    def setEarnings(self, earnings):      
        if earnings < 0: 
            print("Earnings should be above 0,\nSetting it to the default value of 0")
            self.earnings = 0      
        else :
            self.earnings = earnings

    def getEarnings(self):
        return self.earnings

    # If the year is between 1960 - 2022, set the default to 2000
    def setYear(self, year):
        if year < 1960 or year > 2022: 
            print("Year should be Between 1960 - 2020,\nSetting it to the default value of 2000")
            self.year = 2000      
        else :
            self.year = year

    def getYear(self):
        return self.year

    # abstract method 
    def onlineGame(self):
        pass


    # To compare two objects for equality 
    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Game to a different object than Game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)

    # Compare objects by their earnings 
    def __lt__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Game to not an song object")
        
        return self.earnings < value.earnings

    # Returns a printable string of the object
    def __str__(self):
       return (f"The name of the game is {self.title} \nThe cost of the game to play is {self.cost} euros\nHow much the game has earned is {self.earnings:,} euros\nThe year it was released was {self.year}")


# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# First person shooter class, pulls from the parent class and adds how many players for multiplayer and if it's an online game
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

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

    # If the game is online or not 
    def onlineGame(self):
        if self.online == True:
            print("This is an online game ")
        else:
            print("This is not an online game")

    # To compare two objects for equality 
    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Fps game to a different object than Fps game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)

    # To compare two objects for their earnings
    def __lt__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Game to not an song object")
        
        return self.earnings < value.earnings               

    # Returns a printable string of the object
    def __str__(self):
        return super().__str__() + f"\nIt is a multiplyer game with {self.multiplayer} players"  

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Role playing game class pulls from the parent class and adds if it is a solo game
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

class Rpg(Game):
    def __init__(self, title, cost, earnings, year, solo):
        super().__init__(title, cost, earnings, year)

        self.solo = solo

    # Declaring mutator (set) & accessor (get)
    def getSolo(self):
        return self.solo 

    def setSolo(self, x):
        self.solo = x

    # abstract method
    def onlineGame(self):
        pass


    # To compare two objects for equality 
    def __eq__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Rpg to a different object than Rpg game")
        return (self.title == value.title and
                self.cost == value.cost and
                self.earnings == value.earnings and
                self.year == value.year)

    # Compare objects by their earnings 
    def __lt__(self, value):
        if not isinstance(value, Game):
            raise ValueError("Can't compare Game to not an song object")
        
        return self.earnings < value.earnings

    # Returns a printable string of the object
    def __str__(self):
        return super().__str__() + f"\nIt can only play as a solo player " 

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Developer class that stores the name, salary the developer is on, if they have a team, and uses 1.1 aggregration with the Game class
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

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

    # setting the salary to default 0 if data is input incorrectly
    def setSalary(self, salary):
        if salary < 0: 
            print("Salary should be above 0, setting it to the default value of 0")
            self.salary = 0      
        else :
            self.salary = salary

    # Setting the team to default 0 if the data is input incorrectly 
    def setHasATeam(self, team):
        if team < 0 or team > 20: 
            print("Team should be between 0 - 20 , setting it to the default value of 0")
            self.hasATeam = 0      
        else :
            self.hasATeam = team

    def getHasATeam(self):
        return self.hasATeam

    # To compare two objects for equality 
    def __eq__(self, value):
        if not isinstance(value, Developer):
            raise ValueError("Can't compare Developer to a different object than Devoloper")
        return (self.name == value.name and
                self.salary == value.salary and
                self.hasATeam == value.hasATeam)

    # To compare two objects for by their salary
    def __lt__(self, value):
        if not isinstance(value, Developer):
            raise ValueError("Can't compare Game to not an song object")

        return self.salary < value.salary

    # Returns a printable string of the object
    def __str__(self):
        return f"The developer name is {self.name}\nThe salary made was {self.salary}\nThere is a team of {self.hasATeam} developers\n{self.Game}" 

# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Game service class that will store the games while allowing to add, remove, search, calculate cost and earnings and sorting the list of games 
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

class GameService:
    def __init__(self, name):
        self.name = name
        self.games = []
        self.maxNumOfGames = 10

    # Declaring mutator (set) & accessor (get)
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    # Adds a game to the gaming service
    def addGame(self, Game):
        if len(self.games) < self.maxNumOfGames:
            if Game not in self.games:
                self.games.append(Game)
            else:
                print("This game is already in the Game service")
        else:
            print("The gaming service is full")

    # Removes a game from the gaming service 
    def removeGame(self, Game):
        if Game in self.games:
            self.games.remove(Game)
        else:
            print("This is not in your Gaming service: " + Game.name)

    # Serach for a game in the gaming service 
    def searchForGame(self, Game):
        if Game in self.games:
            return True
        else:
            return False

    # Calculates the total cost of the gaming serice
    def calcGamingCost(self):
        totalCost = 0
        for x in self.games:
            totalCost += x.getCost()
        
        return "The total cost of all the games on this service: "+ str(totalCost)

    # Returns a list of the cost 
    def getListOfCost(self):
        costList = []

        for x in self.games:
            costList.append(x.getCost())

        return costList

    # Returns a list of the earnings of the games 
    def getListOfEarnings(self):
        earningList = []

        for x in self.games:
            earningList.append(x.getEarnings())

        return earningList

    # Returns a list of the year the games were created
    def getListOfYear(self):
        yearList = []

        for x in self.games:
            yearList.append(x.getYear())

        return yearList

        

    # sorts out games by highest Earnings
    def sortGameByHighestEarnings(self):    
        self.games.sort(reverse=True)

    # sorted list of earnings highest to lowest
    def sortedGameEarnings(self): 
        return sorted(self.games, reverse=True)

    # sorts game list by alphbetical 
    def sortByNameGame(self):    
        self.games.sort(key=lambda song: song.title)

    # sorted list in alphabetical 
    def sortedByName(self): 
        return sorted(self.games, key=lambda song: song.getTitle())

    # Returns a printable string of the object
    def __str__(self):
        tempString = ""

        for x in self.games:
            tempString += x.getTitle() + "\n"

        return f"The name of the gaming service is {self.name}\nThe list of games are:\n{tempString}"




# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Helper functions to sort the name of the games, find the modulus, return the name, get the game with the highest cost, and developer with the highest salary
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

def useSongNameToSort(song):
    return song.getTitle()

    # used to find a remainder 
def findModulus(num):
    return num%6

    # return the tittle of a game
def getGameName(name):
    return name.title

    # return the games greeter than 40
def findGameWithCost(game):
    return game.getCost() >= 40

    # return the list of developers that have a salary more than 70,000
def findDeveloperSalary(developer):
    return developer.getSalary() > 70000



# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Creating Gaming service, deveopler, and game objects
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

GameService_1 = GameService("First Gaming Service")
GameService_2 = GameService("Second Gaming Service")
GameService_3 = GameService("Third Gaming Service")


game_1 = Rpg("Chrono Trigger", 15, 26500000, 1995, "1 Plater")
game_2 = Rpg("Final Fantasy 7", 20, 1300000000, 1997, "1 Player")
game_3 = Rpg("Baldur's Gate 2: Shadows of Amn", 10, 92000000, 2000, "1 Plater")
game_4 = Rpg("Pokemon Yellow", 20, 1200000000, 1998, "1 Player")
game_5 = Rpg("World at Warcraft", 40, 2600000000, 2004, "1 Plater")
game_6 = Rpg("Planescape: Torment", 15, 9000000, 1999, "1 Player")
game_7 = Rpg("Diablo 2", 10, 48000000, 2000, "1 Plater")
game_8 = Rpg("The Witcher 3: Wild Hunt", 60, 150000000, 2015, "1 Player")
game_9 = Rpg("Dark Souls", 50, 63000000, 2011, "1 Plater")
game_10 = Rpg("Persona 4 Golden", 35, 30000000, 2012, "1 Player")

game_11 = Fps("Destiny 2", 60, 200000000, 2017, "2-4 Player", False)
game_12 = Fps("Call of Duty: Warzone ", 80, 30000000000, 2020, "2-4 Player", True)
game_13 = Fps("Doom Eternal", 40, 450000000, 2020, "2-4 Player", False)
game_14 = Fps("Half-Life: Alyx", 20, 200000000, 2017, "2-4 Player", False)
game_15 = Fps("Halo: The Master Chief Collection", 20, 30000000, 2014, "2-4 Players", True)
game_16 = Fps("Tom Clancy's Rainbow Six Siege", 40, 200000000, 2015, "2-4 Player", True)
game_17 = Fps("Titanfall 2", 25, 64000000, 2016, "2-4 Player", True)
game_18 = Fps("Black Mesa", 20, 31000000, 2015, "2-4 Player", True)
game_19 = Fps("Superhot", 15, 12000000, 2014, "1 Player", False)
game_20 = Fps("Metro Exodus", 30, 58000000, 2019, "2-4 Player", True)

developer_1 = Developer("Square", 70000, 8, game_1)
developer_2 = Developer("Square Enix", 50000, 4, game_2)
developer_3 = Developer("BioWare", 60000, 2, game_3)
developer_4 = Developer("Game Freak", 35000, 4, game_4)
developer_5 = Developer("Blizzard Entertainment", 100000, 8, game_5)
developer_6 = Developer("Black Isle Studios", 45000, 6, game_6)
developer_7 = Developer("Blizzard North", 80000, 8, game_7)
developer_8 = Developer("CD Project RED", 120000, 10, game_8)
developer_9 = Developer("FromSoftware", 1100000, 5, game_9)
developer_10 = Developer("Atlus", 60000, 2, game_10)

developer_11 = Developer("Bungie", 90000, 4, game_11)
developer_12 = Developer("Infinite Ward", 150000, 18, game_12)
developer_13 = Developer("ID Software", 80000, 10, game_13)
developer_14 = Developer("Value", 50000, 10, game_14)
developer_15 = Developer("343 Industries", 60000, 2, game_15)
developer_16 = Developer("Ubisoft", 100000, 19, game_16)
developer_17 = Developer("Respawn Entertainment", 70000, 10, game_17)
developer_18 = Developer("Crowbar Collection", 60000, 6, game_18)
developer_19 = Developer("SUPERHOT Team", 500000, 12, game_19)
developer_20 = Developer("4A Games", 90000, 12, game_20)


# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Testing game objects, data integridy
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

# Print the object as it is
print("***************This is to check the object as it was stored***************\n")
print(game_1)

# Test data integridy
print("\n***************This is to check the data inegrity***************\n")
game_1.setCost(-10)
game_1.setEarnings(-26500000)
game_1.setYear(1900)

# Change the object using the mutator methods
game_1.setTitle("Chrono Trigger 2: The adventure")
game_1.setCost(10)
game_1.setEarnings(16500000)
game_1.setYear(2002)

# Test the accessor methods
print("\n***************This is to check the accessor methods***************\n")
print("The cost of this game is: "+ str(game_1.getCost()))
print("How much this game has earned: "+ str(game_1.getEarnings()))
print("The year it was released was: "+ str(game_1.getYear()))
print("The name of the game is "+ game_1.getTitle())

# Test object after mutator method changed the data
print("\n***************This is to check the object after changes implemented***************")
print("\n" + str(game_1))


# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Testing Fps online, comparing objects to each other
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

print("\n*************** This is to check which Fps games are3 online ***************")
game_11.onlineGame()
game_12.onlineGame()
game_13.onlineGame()
game_14.onlineGame()
game_15.onlineGame()
game_16.onlineGame()
game_17.onlineGame()
game_18.onlineGame()
game_19.onlineGame()
game_20.onlineGame()

print("\n*************** This is the type of classes  ***************")

print(type(game_1))
print(type(game_11))
print(type(developer_1))
print(type(GameService_1))

print("\n*************** This is to compare objects ***************")

print(game_1 == game_2)
print(game_1 < game_2)
print(game_3 == game_4)
print(game_3 < game_4)
print(game_11 == game_12)
print(game_13 < game_15)
print(game_15 < game_17)
print(game_18 < game_14)
print(developer_11 < developer_12)
print(developer_3 < developer_4)
print(developer_7 < developer_5)



# --------------------------------------------------------------------------------------------------------------------------------------------------------#
# Testing the functionalty of the gaming service 
# --------------------------------------------------------------------------------------------------------------------------------------------------------#

# Adding games to First Gaming Service 
GameService_1.addGame(game_1)
GameService_1.addGame(game_3)
GameService_1.addGame(game_5)
GameService_1.addGame(game_7)
GameService_1.addGame(game_9)
GameService_1.addGame(game_11)
GameService_1.addGame(game_13)
GameService_1.addGame(game_15)
GameService_1.addGame(game_17)
GameService_1.addGame(game_19)

GameService_2.addGame(game_2)
GameService_2.addGame(game_4)
GameService_2.addGame(game_6)
GameService_2.addGame(game_8)
GameService_2.addGame(game_10)
GameService_2.addGame(game_12)
GameService_2.addGame(game_14)
GameService_2.addGame(game_16)
GameService_2.addGame(game_18)
GameService_2.addGame(game_20)

GameService_3.addGame(game_1)
GameService_3.addGame(game_7)
GameService_3.addGame(game_6)
GameService_3.addGame(game_9)
GameService_3.addGame(game_10)
GameService_3.addGame(game_15)
GameService_3.addGame(game_2)
GameService_3.addGame(game_19)
GameService_3.addGame(game_11)
GameService_3.addGame(game_5)


print("\n*************** This is First Gaming Service ***************")
print(GameService_1)


print("\n*************** This is Second Gaming Service ***************")
print(GameService_2)

print("\n*************** This is Third ***************")
print(GameService_3)

print("\n*************** Adding to a Service that is already full ***************")
GameService_1.addGame(game_2)

print("\n*************** Remove a game from a service ***************")
print("The full game service\n")
print(GameService_1)

print("Gaming Service with Chrono Trigger 2: The Adventure is removed\n")
GameService_1.removeGame(game_1)
print(GameService_1)

GameService_1.addGame(game_1)

print("\n*************** Search for a game ***************")
print("Is " + str(game_3.getTitle()) + " in this gaming Service: " + str(GameService_1.searchForGame(game_3)))
print("Is " + str(game_2.getTitle()) + " in this gaming Service: " + str(GameService_1.searchForGame(game_2)))


print("\n*************** Calculate the total cost for all games ***************")
print("Total cost of First Gaming Service")
print(GameService_1.calcGamingCost())

print("\nTotal cost of Second Gaming Service")
print(GameService_2.calcGamingCost())

print("\nTotal cost of Third Gaming Service")
print(GameService_3.calcGamingCost())


print("\n*************** Print highest number, lowest number and sum of the cost, earning and return the average year ***************")

print("This is the highest cost for a game: " + str(max(GameService_1.getListOfCost())))
print("This is the lowest cost for a game: " + str(min(GameService_1.getListOfCost())))
print("This is the cost for all the games " + str(sum(GameService_1.getListOfCost())))

maxEarnings = (max(GameService_1.getListOfEarnings()))
lowEarnings = (min(GameService_1.getListOfEarnings()))
totalEarnings = (sum(GameService_1.getListOfEarnings()))

print(f"\nThis is the highest earnings for a game: {maxEarnings:,} in {GameService_1.getName()}")
print(f"This is the lowest earnings for a game: {lowEarnings:,} in {GameService_1.getName()}")
print(f"This is the earnings for all the games: {totalEarnings:,} in {GameService_1.getName()}")


listOfYears = GameService_1.getListOfYear()
averageYear = int(sum(listOfYears) / len(listOfYears))
print("\nThe average year for the games in " + str(GameService_1.getName()) + "is: " + str(averageYear))

# ----------------------------------------------------------------------------------------------------------------------------

print("\nSorted list of the gaming service by highest earnings")
print("This is the "+ GameService_2.getName() + "List before been sorted \n" +  str(GameService_2))

print("Sorted list of the highest earnings\n")
for s in GameService_2.sortedGameEarnings():
    print(s.title)

print("\nThe " + GameService_2.getName() + "list has not changed order as sorted was implemented\n" + str(GameService_2))

print("\nSort the gaming service by highest earnings")
print("Print " + str(GameService_2.getName() + " before using sort method\n"))
print(GameService_2)
GameService_2.sortGameByHighestEarnings()
print(GameService_2.getName() + "has now be sorted from highest to lowest earnings ")
print(GameService_2)


print("Sorted list of the alphabetical order\n")
for s in GameService_3.sortedByName():
    print(s.title)

print("\nThe " + GameService_3.getName() + "list has not changed order as sorted was implemented\n" + str(GameService_3))

print("\nSort the gaming service by alphabetical order")
print("Print " + str(GameService_3.getName() + " before using sort method\n"))
print(GameService_3)
GameService_3.sortByNameGame()
print(GameService_3.getName() + "has now be sorted by alphabetical order and will stay that way")
print(GameService_3)


print("Finding the largest rainder in the list of cost ")
largest_remainder = max(GameService_1.getListOfCost(), key=findModulus)
print("The number with largest remainder when divided by 4 is:", largest_remainder)

print("\nReturning the names in the gaming service using helper function ")
result=list(map(getGameName, GameService_1.games)) 
print(result)

print("\nReturning the names in the gaming service using built-in lambda ")
result=list(map(lambda s : s.title, GameService_1.games)) 
print(result)

print("\nReturn all the games on the list that cost equal to or move that 40 euro using the helper function ")
greatSongNameList = list(map(getGameName, list(filter(findGameWithCost, GameService_1.games))))
print(greatSongNameList)

print("\nReturn all the games on the list that cost equal to or move that 40 euro using the built-in lanbda ")
greatSongNameList = list(map(getGameName, list(filter(lambda s : s.getCost() >= 40, GameService_1.games))))
print(greatSongNameList)

deveolperList = [developer_1, developer_2, developer_3, developer_4, developer_5, developer_6, developer_7, developer_8, developer_9, developer_10,
                 developer_11, developer_12, developer_13, developer_14, developer_15, developer_16, developer_17, developer_18, developer_19, developer_20]


listOfHighEarners = list(filter(findDeveloperSalary, deveolperList))
print("\nThose earnings above 70000 are :")
for artist in listOfHighEarners :
    print(artist.name)




