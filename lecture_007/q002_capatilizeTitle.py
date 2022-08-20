class Solution:
    def isLowerCase(self,ch):
        return ch >= 'a' and ch <= 'z'

    def isUpperCase(self,ch):
        return ch >= 'A' and ch <= 'Z'

    def convertLargeCharacterSmall(self,ch):
        return chr(ord(ch) - ord('A') + ord('a'))
    
    def convertSmallCharacterLarge(self,ch):
        return chr(ord(ch) - ord('a') + ord('A'))



    def lower(self,str):
        l = len(str)
        ans = ""

        for i in range(l):
            if self.isUpperCase(str[i]):
                ans += self.convertLargeCharacterSmall(str[i])
            else:
                ans += str[i]

        return ans
    
    def capitalizeTitle(self, title: str) -> str:
        l = len(title)
        if l <= 2:
            return self.lower(title)
        
        words = title.split(" ")
        wordsLen = len(words)
        
        res = ""
        for i in range(wordsLen):
            word = words[i]
            if len(word) <= 2:
                res += self.lower(word)
            else:
                ch = word[0]
                if self.isLowerCase(ch):
                    res += self.convertSmallCharacterLarge(ch)
                else:
                    res += ch
                
                res += self.lower(word[1:len(word)])
                
            if i != wordsLen - 1:
                res += " "
            
        return res
                
                
        
        