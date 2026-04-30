class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0: 
            return ""
        s=""
        for char in strs:  
            s += (f"{len(char)},")

        s += "'#'"
        for word in strs:
            s += (word)
        

        return s

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
        x = s.split("'#'")
        dummy = x[0].split(",")
        lengths = []
        word_array = []
        starting = 0
        for ifg in dummy: 
            if ifg.isdigit():
                word_array.append(x[1][starting: starting + int(ifg): 1])
                starting += int(ifg)

        return word_array