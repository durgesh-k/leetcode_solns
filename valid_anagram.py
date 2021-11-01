class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[]
        s1[:0]=s
        t1=[]
        t1[:0]=t
        if len(s)!=len(t):
            return False
        for i in s:
            try:
                if t1.index(i)>=0:
                    s1.remove(i)
                    t1.remove(i)
            except:
                print('Error')
        if len(s1)==0 and len(t1)==0:
            return True
        else:
            return False