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
        for ifg in dummy: 
            if ifg.isdigit():
                lengths.append(int(ifg))
        word_array = []
        starting = 0
        print(lengths)
        for l in lengths: 
            word_array.append(x[1][starting: starting + l: 1])
            starting += l

        return word_array