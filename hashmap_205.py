# I improved:
# other:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t_mapping = {}

        for char_s, char_t in zip(s, t):
            # Check mapping from s to t
            if char_s in s_to_t_mapping:
                if s_to_t_mapping[char_s] != char_t:
                    return False
            else:
                if char_t in set(s_to_t_mapping.values()):
                    return False
                s_to_t_mapping[char_s] = char_t

        return True


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         s_len = len(s)
#         s_dict = {}
#         t_dict = {}
#         for i in range(s_len):
#             if s[i] not in s_dict:
#                 s_dict[s[i]] = [0,[i]]
#                 # print(s_dict)
#             else:
#                 # print(s_dict)
#                 s_dict[s[i]][0] += 1
#                 s_dict[s[i]][1].append(i)
#             if t[i] not in t_dict:
#                 t_dict[t[i]] = [0,[i]]
#             else:
#                 t_dict[t[i]][0] += 1
#                 t_dict[t[i]][1].append(i)
#         print(tuple(s_dict.values()))
#         print(tuple(t_dict.values()))
#         return tuple(s_dict.values()) == tuple(t_dict.values())

# # other:
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         s_to_t_mapping = {}
#         t_to_s_mapping = {}

#         for char_s, char_t in zip(s, t):
#             # Check mapping from s to t
#             if char_s in s_to_t_mapping:
#                 if s_to_t_mapping[char_s] != char_t:
#                     return False
#             else:
#                 s_to_t_mapping[char_s] = char_t

#             # Check mapping from t to s
#             if char_t in t_to_s_mapping:
#                 if t_to_s_mapping[char_t] != char_s:
#                     return False
#             else:
#                 t_to_s_mapping[char_t] = char_s

#         return True
