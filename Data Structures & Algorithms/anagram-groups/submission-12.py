class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_list = {}
        for index, word in enumerate(strs):
            if tuple(sorted(word)) in check_list: 
                check_list[tuple((sorted(word)))].append(word)
            else: 
                check_list[tuple((sorted(word)))] = [word]

            #if dict_list[index] in check_list.values():
          #      check_list[index] = check_list[index].append(dict_list[index])
         #   else: 
          #      check_list[index] = [dict_list[index]]


        return list(check_list.values())

