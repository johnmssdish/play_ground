class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        len_pattern = len(pattern)
        list_s = s.split(' ')
        len_s = len(list_s)
        if len_pattern != len_s:
            return False
        
        pattern_to_s_dict = {}
        s_value_set = set()
        for i in range(len_s):
            if pattern[i] not in pattern_to_s_dict:
                if list_s[i] in s_value_set:
                    return False
                pattern_to_s_dict[pattern[i]] = list_s[i]
                s_value_set.add(list_s[i])
            if list_s[i] != pattern_to_s_dict[pattern[i]]:
                return False
        return True