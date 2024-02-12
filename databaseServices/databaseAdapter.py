from abc import ABC, abstractmethod

class DatabaseAdapter:
    @abstractmethod
    def saveOne(self,database,sql,data) ->int:
        pass
    @abstractmethod
    def saveMany(self,database,sql,data):
        pass
    @abstractmethod
    def getOne(self,database,sql):
        pass
    @abstractmethod
    def getMany(self,database,sql):
        pass
