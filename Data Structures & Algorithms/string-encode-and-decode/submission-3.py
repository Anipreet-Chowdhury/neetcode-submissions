class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += "\r" + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        split = s.split("\r")
        print(split)
        return split[1:]
        # i = 0
        # while i < len(s):
        #     j = i
        #     while s[j] != "#":
        #         j += 1
        #     length = int(s[i:j])
        #     res.append(s[j+1:j+1+length])
        #     i = j+1+length
        # print(res)
        # return res


