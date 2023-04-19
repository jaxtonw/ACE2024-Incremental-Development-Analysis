class Blobber:
    
    def __init__(self):
        self.__name = True
        self.__color = True
        self.__radius = True
        self.__height = True
        
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
    
    def feedBlobber(self):
        return True    
        
    def blobberSpeak(self):
        print("My name is " + str(self.__name) + ", and I am" + str(self.__color) + "\n"
              "My current happiness level is" + str(self.__radius) + "%")
        
    def vitalsOk(self):
        if self.radius >= 90 and self.__radius <= 110:
            return True
        else:
            return False
        
    
    def __init__(self):
        self.__name = True
        self.__color = True
        self.__radius = True
        self.__height = True
        
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
    
    def feedBlobber(self):
        return True    
        
    def blobberSpeak(self):
        print("My name is " + str(self.__name) + ", and I am" + str(self.__color) + "\n"
              "My current happiness level is" + str(self.__radius) + "%")
        
    def vitalsOk(self):
        if self.radius >= 90 and self.__radius <= 110:
            return True
        else:
            return False
        
