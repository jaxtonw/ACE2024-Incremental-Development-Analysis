def midWord(midWordLength):)    
    midWordLength = 0
    if (len(self.__wordinator)) % 2 == 0:
        if (len(self.__wordinator) // 2) % 2 == 0:
            midWordLength = len(self.__wordinator) // 2
        else:
            midWordLength = len(self.__wordinator) // 2 + 1
    else:
        if (len(self.__wordinator) // 2) % 2 == 0:
            midWordLength = len(self.__wordinator) // 2 + 1
        else:
            midWordLength = len(self.__wordinator) // 2
    
    start = 0
    if len(self.__wordinator) == 7:
        start = len(self.__wordinator) // 4 + 1
    else:
        start = len(self.__wordinator) // 4

