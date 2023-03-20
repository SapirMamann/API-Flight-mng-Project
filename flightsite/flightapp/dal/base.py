from abc import ABC, abstractmethod

class BaseDAL(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def get_by_id():
        pass
    
    @abstractmethod
    def update_by_id(): 
        pass
    
    @abstractmethod
    def delete():
        pass