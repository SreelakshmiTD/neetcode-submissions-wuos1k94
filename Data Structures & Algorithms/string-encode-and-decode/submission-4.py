class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for inter_s in strs:
            s = s + '$/' + inter_s
        return s
    def decode(self, s: str) -> List[str]:
        res = s.split('$/')
        return res[1:]
