class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = list()

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)

    # TODO debug
    def simplifyPath_2(self, path: str) -> str:
        size = len(path)
        names = path.split("/")
        stack = list()
        x = 0

        def read_word(num) -> str:
            strs = ""
            while num < size:
                num += 1
                if num >= size:
                    return strs
                if path[num] == "/":
                    return strs
                else:
                    strs += path[num]
                num += 1

        for i in range(size - 1):
            if path[i] == "/":

                temp = read_word(i)
                print(temp)
                if temp == "..":
                    if stack:
                        stack.pop()
                elif temp and temp != ".":
                    stack.append(temp)

        return "/" + "/".join(stack)


solution = Solution()
path = "/a//b////c/d//././/.."
s = solution.simplifyPath(path)
print(s)
