class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            freq_table1 = {}
            freq_table2 = {}
            for i in range(len(t)):
                if s[i] in freq_table1:
                    freq_table1[s[i]]+=1
                else:
                    freq_table1[s[i]]=1
                if t[i] in freq_table2:
                    freq_table2[t[i]]+=1
                else:
                    freq_table2[t[i]]=1
            if freq_table1 == freq_table2:
                return True
            else:
                return False
        
          
        