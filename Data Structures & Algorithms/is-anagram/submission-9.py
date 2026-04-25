class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}

        for num_s, num_t in zip(s, t):
            if num_s in s_dict:
                s_dict[num_s] += 1
            else: 
                s_dict[num_s] = 1

            if num_t in t_dict:
                t_dict[num_t] += 1
            else: 
                t_dict[num_t] = 1


        return (t_dict == s_dict)



            
        