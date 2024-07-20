from collections import deque


class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        point = 0
        i, j = 0, 0
        while i < len(s):
            if s[i] == 'a' or s[i] == 'b':
                while j+1 < len(s) and (s[j+1] == 'a' or s[j+1] == 'b'):
                    j+=1
                point += self.process(s[i:j+1], x, y)                
                i = j + 1
            else:
                i+= 1
                j = i
        return point
    
    def process(self, s, x, y) -> int:
        print(s, x, y)
        stack = deque()
        point = 0
        a, b = 'a', 'b'
        if (x > y):
           a, b = b, a 
           x, y = y, x

        for c in s:
            if c == a and (len(stack) > 0 and stack[-1] == b):
                    stack.pop()
                    point += y
                    print(f"add y point{y}")
            else:
                 stack.append(c)
        while stack: 
            last = stack.pop()
            if last == b and len(stack) > 0 and stack[-1] == a:
                stack.pop()
                point += x
                print(f"add x point{x}")
            elif last == b and len(stack) > 0 and stack[-1] == b:
                back = [1, 0]
                while stack and stack[-1] == b:
                    back[0] += 1
                    stack.pop()
                while stack and stack[-1] == a:
                    back[1] += 1
                    stack.pop()
                point += (x * min(back[0], back[1]))    
                print(f"add x point{x}")
        return point



ans = Solution().maximumGain("aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha", 1926, 4320)
print(ans)

# bbb