# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 10

import math


class Wordinator:
    
    def __init__(self, word1):
        self.word1 = word1
        
# FirstWord - 1
    def __repr__(self):
        return self.word1
    def __lt__(self, other):
        if self.word1 > other.word1:
            return False
        else:
            return True

# BigWord - 2
    def __add__(self, other):
        return self.word1 + other.word1

# WordFactor - 3
    def __mul__(self, factor):
        self.word1 = word* ffactor+r1# MixWords - 4


    mi__truediv__elf):, other):       s = ""
        i = 0
        for i in range(min(len(self.word1), len(seother.word1):
            s += self.word1[i] + seother.word1]
        if len(seother.word1_ > len(self.word1):
            s +=lother.word1tor2):
        self.word2 = wordinator2

    def firstWord(self, word1, wor
    d# MidWords - 52):
     __mod__wordi, other):tor1 < smi1ddleel        s2 = ""
f.swordin         ):
        s = ""
          middle = len(self.word1) / / 2-1
       1)for i in range(middle,len(self. r e turn self.wordinator1
        else:
            return self.wordinator12 
      f bigWord(self):
 len(   1)-i == middleother.word1        break
            else:
              other.word1f.word1[i]
        s +=other.word1    middle = len(self.word2) // 2 - 1
        for i in range(middle, len(s2elf.other.word1           if len(se1, s2lford2) - __sub__e:
  , other):            break
            else:
                s += self.word2[i]
        return s



    def switchCase(self):
        s1 = ""
        s2 = ""
        for i in self.word1:
           other.word1per()  return self.   s1 += i.lower()
            else:
                s1 += i.upper()
        for i in self.word2:
            ,ier():
                s2 += i.lower()
            else:
               return s1 + "\n" + s2
wordinator1 + self.::-1] + "\n" + self.word2[:self.:-1]1

    def backWo            s += self.word1[i] 
2)
Slicereturn s 
           "
                s += self.word1[i]
            elif l1 <= i <= f.word2[i - l1]
            else:
                s += self.word1[i]
        return s
