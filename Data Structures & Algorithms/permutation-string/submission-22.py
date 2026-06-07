class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lett_s1 = {}

        for x in s1: 
            lett_s1[x] = 1 + lett_s1.get(x, 0)

        lett_s2 = {}
        l = 0
        for r in range(len(s2)): 
            lett_s2[s2[r]] = 1 + lett_s2.get(s2[r], 0)

            if r - l + 1 > len(s1):
                lett_s2[s2[l]] -=1
                if lett_s2[s2[l]] == 0: 
                    lett_s2.pop(s2[l])
                l += 1

            if lett_s2 == lett_s1: 
                return True


        return False 
                

