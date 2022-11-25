#This Program is for Lab Assessment 1
#
#
#Author: Gavin Judge
#
#
#Module: Software Development

from abc import ABC, abstractmethod
from ast import Num
from shutil import move
from turtle import title #using the abc module to creaate abstract classes and methods
import tkinter as TK

class StreamingServiceItem(ABC):
    def __init__(self , title, duration, starRating):
        self.title = title
        self.duration = duration
        self.starRating = starRating

    def setTitle(self, title):
        self.title = title
    
    def getTitle(self):
        return self.title

    def setDuration(self, duration):
        self.duration = duration
    
    def getDuration(self):
        return self.duration

    def setStarRating(self, starRating):      
        if starRating < 0 : #lab2 - data integrity check for value of e
            print("earnings should be above 0, setting it to the default value of 0")
            self.starRating = 0      
        else :
            self.starRating = 0

    def getStarRating(self):
        return self.starRating

    def __str__(self):
        return "Title: " +self.title+ "\nDuration: " +str(self.duration)+ "\nStar Rating: "+str(self.starRating)+ "\n"

class TvShow(StreamingServiceItem):
    def __init__(self, title, duration, starRating, episode):
        super().__init__(title, duration, starRating)
        self.Episode = episode
        self.maxNofItems = 10
        self.seasonList = []

    def __eq__(self, value):
        if not isinstance(value, TvShow):
                raise ValueError("Cant compare TV Show to non TV Show")

        return (self.title == value.title and 
                self.duration == value.duration and
                self.starRating == value.starRating)

    def addEpisode(self, episode):
        self.seasonList.append(episode)

    
    def addEpisode(self, episode):
        if len(self.seasonList) < self.maxNofItems:
            if episode not in self.seasonList: #Lab 4: Part3 - check if a particular Song object is not in the songs list
                self.seasonList.append(episode) #Lab 4: Part3 - call the inbuilt append method for the list
            else:
                print("Customer is already in the list")
        else: 
            print("Customer list is full") 
        
    def __call__(self, episode):
        self.episode = episode

    def getNumOfEpisodes(self):
        result = 0
        for ep in self.seasonList:
            result += ep.episodeCount   
        return result

    def searchForTVShow(self, Episode):
        if Episode in self.seasonList:
            return True
        else:
            return False
    
    def __str__(self):
        return super().__str__() + str(self.episode)

class Episode:
    def __init__(self, season, episode):
        self.season = season
        self.episode = episode

    def setSeason(self, season):
        self.season = season
    
    def getSeason(self):
        return self.season

    def setEpisode(self, episode):
        self.episode = episode

    def getEpisode(self):
        return self.episode

    def __str__(self):
        return "Season: " +str(self.season)+ "\nEpisode: " +str(self.episode)+ "\n"

class Movie(StreamingServiceItem):
    def __init__(self, title, duration, starRating, isSequel):
        super().__init__(title, duration, starRating)

        self.isSequel = isSequel

    def __eq__(self, value):
        if not isinstance(value, Movie):
                raise ValueError("Cant compare Movie to Non Movie type")

        return (self.title == value.title and 
                self.duration == value.duration and
                self.starRating == value.starRating)

    def setIsSequel(self, isSequel):
        self.isSequel = isSequel

    def __str__(self):
        return super().__str__() + "Other Movies in Franchise: " +self.isSequel

class Director: #lab4: Part1 - adding a Song class to show an aggregation relationship between it and the Artist class 
    
    def __init__(self, name, noOfGrammy):
        self.name = name
        self.noOfGrammy = noOfGrammy

    def setDirectorName(self, name):
        self.name = name

    def getDirectorName(self):
        return self.name

    def setNoOfGrammy(self, noOfGrammy):
        self.noOfGrammy = noOfGrammy
    
    def __str__(self):
        return "Director: " +self.name+ "\nNumber of Grammys: " +str(self.noOfGrammy) 

class AccountInfo:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def setUsername(self, username):
        self.username = username
    
    def getUsername(self):
        return self.username
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def __str__(self):
       return "Username: " +self.username+ "\nEmail: " +self.email

class Customer: #Lab 4: Part3 - Zero to many (0:M) aggregation relationship between Playlist and Song classes - Playlist contains a list of Songs     
    def __init__(self, accountInfo=None):
        self.accountInfo = accountInfo
        self.maxNofItems = 10
        self.customerList = [] #Lab 4: Part3 - a Playlist can contain 0 or many Song objects in the songs list

    def addCustomer(self, accountInfo): 
        if len(self.customerList) < self.maxNofItems:
            if accountInfo not in self.customerList: #Lab 4: Part3 - check if a particular Song object is not in the songs list
                self.customerList.append(accountInfo) #Lab 4: Part3 - call the inbuilt append method for the list
            else:
                print("Customer is already in the list")
        else: 
            print("Customer list is full")

    def removeCustomer(self, accountInfo): 
        if accountInfo in self.customerList: #Lab 4: Part3 - check if a particular Song object is in the songs list
            self.customerList.remove(accountInfo) #Lab 4: Part3 - call the inbuilt remove method for the songs list
        else:
            print(AccountInfo.username + " is not in playlist")    
            
    def searchForCustomer(self, accountInfo):
        if accountInfo in self.customerList:
            return True
        else:
            return False

    def __str__(self):
        returnString = ''
        for accountInfo in self.customerList:
            returnString +=  accountInfo.username+ ", " +accountInfo.email+ '; '
        return "list of customers: " +returnString



    ###
    '''  
    #def calcPlaylistDuration(self): #Lab4: Part4 - calculating the duration of the Playlist based on the length of the Song objects it contains
     #   plDuration = 0
      #  for s in self.favourites: #Lab 4: Part4 - loop through each item in the songs list
       #     plDuration += s.getLength()  
        #return plDuration
    #def __str__(self):
   #    return "Username: " + self.username + "\nEmail : " +self.email+ "\n"
   
    #def __str__(self):
     #   returnString = ''
      #  for s in self.customerList:
       #     returnString +=  s.customer + '; '
        #return "list of customers: " +returnString
    '''
#--------------------Create Episodes for Breaking Bad season 1 ------------------------------------#

episode1 = Episode(1, 1)
tvShow1 = TvShow("Breaking Bad", 87, 5, episode1)
director1 = Director("Michael Bay", 7)

tvShow1.addEpisode(1)

print(director1)
print(tvShow1)
print(tvShow1.getNumOfEpisodes())

#print(tvShow1)
'''
episode2 = Episode(1,2)
tvShow2 = TvShow("Breaking Bad", 87, 5, episode2)
#print(tvShow2)

episode3 = Episode(1,3)
tvShow3 = TvShow("Breaking Bad", 87, 5, episode3)
#print(tvShow2)

episode4 = Episode(1,4)
tvShow4 = TvShow("Breaking Bad", 87, 5, episode4)
#print(tvShow4)

episode5 = Episode(1,5)
tvShow5 = TvShow("Breaking Bad", 87, 5, episode5)
#print(tvShow5)

episode6 = Episode(1,6)
tvShow6 = TvShow("Breaking Bad", 87, 5, episode6)
#print(tvShow6)

episode7 = Episode(1,7)
tvShow7 = TvShow("Breaking Bad", 87, 5, episode7)
#print(tvShow7)

episode8 = Episode(1,8)
tvShow8 = TvShow("Breaking Bad", 87, 5, episode8)
#print(tvShow7)

episode9 = Episode(1,9)
tvShow9 = TvShow("Breaking Bad", 87, 5, episode9)
#print(tvShow9)

episode10 = Episode(1,10)
tvShow10 = TvShow("Breaking Bad", 87, 5, episode10)
#print(tvShow10)
'''
#--------------------Finished Episodes for Breaking Bad season 1 ------------------------------------#
#--------------------create Customers ------------------------------------#
'''
customerDetails1 = AccountInfo("GavinJudge", "gavinjudge@gmail.com")
customer1 = Customer(customerDetails1)

customer1.addCustomer(customerDetails1)

customerDetails2= AccountInfo("KeithJudge", "keithjudge@gmail.com")
customer2 = Customer(customerDetails2)

customer2.addCustomer(customerDetails2)
'''
#print(customer1)
#print(customer2)



'''
#movie1 = Movie("The Invicibles", 95, 4, "No")
#print(movie1)

#director1 = Director("Michael Bay", 6)
#print(director1)

#customer1 = Customer("gavinjudge", "gavinjudge@gmail.com")
#print(customer1)

#customer2 = Customer("keithjudge", "keithjudge@gmail.com")
#print(customer2)

#print(Customer.searchForCustomer)

#customer1.addCustomer
#customer2.addCustomer

#test1 = Episodes("season 1", 60, item1)
#print(test1)
'''
"""
print(breakingBad)
print("")
print(theInvicibles)
print("")
print(breakingBad == breakingBad)
""" 










