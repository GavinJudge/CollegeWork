#This Program is for Lab Assessment 1
#
#It will be a streaming service which uses a parent class, and has two child classes which have inheritance
#
#Author: Gavin Judge
#
#Module: Software Development

from abc import ABC, abstractmethod
from shutil import move
#from turtle import title #using the abc module to creaate abstract classes and methods

class StreamingServiceItem:
    def __init__(self , title, duration):
        self.title = title
        self.duration = duration

    def setTitle(self, title):
        self.title = title
    
    def getTitle(self):
        return self.title

    def setDuration(self, duration):
        self.duration = duration
    
    def getDuration(self):
        return self.duration

    def __str__(self):
        return "Title: " +self.title+ " Duration: " +str(self.duration)

class TvShow(StreamingServiceItem):
    def __init__(self, title, duration, season, episode):
        super().__init__(title, duration)

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
    
    def __str___(self):
        return super().__str__() + "Season: " +self.season+ " Episode: " + self.episode

class Movie(StreamingServiceItem):
    def __init__(self, title, duration, isSequel):
        super().__init__(title, duration)

        self.isSequel = isSequel

    def setIsSequel(self, isSequel):
        self.isSequel = isSequel

    def getIsSequel(self):
        return self.isSequel

    def __str__(self):
        return "Number of movies in franchise: " +self.isSequel

#item1 = StreamingServiceItem("Breaking Bad", 87)
item1Bio = TvShow("Breaking bad", 87, 5, 100)


print(item1Bio)
#print(TvShow.getTitle, TvShow.getDuration, TvShow.getSeason, TvShow.getEpisode)