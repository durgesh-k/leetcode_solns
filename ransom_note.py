class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        newStr=[]
        magazineList=[]
        ransomList=[]
        magazineList[:0]=magazine
        ransomList[:0]=ransomNote
        if len(ransomNote)>len(magazine) or len(ransomNote)==0 or len(magazine)==0:
            return False
        for i in ransomList:
            try:
                if magazineList.index(i)>=0:
                    newStr.append(i)
                    magazineList.remove(i)
            except ValueError:
                print(newStr)
        if newStr==ransomList:
            return True
        else:
            return False
        