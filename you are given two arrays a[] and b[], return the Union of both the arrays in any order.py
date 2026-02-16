class Solution:
    def findUnion(self, a, b):
        seen = {}
        result = []

        for x in a:
            if x not in seen:
                seen[x] = True
                result.append(x)

        for x in b:
            if x not in seen:
                seen[x] = True
                result.append(x)

        return result
