from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        for i, f in enumerate(formula):
            if f == '(' or f == ')':
                stack.append([f, 1])
            elif f >= '0' and f <= '9':
                if i > 0 and formula[i-1] >= '0' and formula[i-1] <= '9':
                    continue
                j = i + 1
                while j < len(formula) and formula[j] >= '0' and formula[j] <= '9':
                    j += 1
                count = int(formula[i: j])
                    
                if stack[-1][0] == ')':
                    stack.pop()
                    temp_list = []
                    while stack[-1][0] != '(':
                        last = stack.pop()
                        last[1] *= count
                        temp_list.append(last)
                    stack.pop()
                    stack.extend(temp_list)
                else:
                    stack[-1][1] = count
                    
            elif f >= 'A' and f <= 'Z':
                stack.append([f, 1])
            elif f >= 'a' and f <= 'z':
                stack[-1][0] = f"{stack[-1][0]}{f}"
                
        count_map = defaultdict(int)
        for i, e in stack:
            if i != ')' and i != '(':
                 count_map[i] += e
        
        print(count_map)
        count_list = list(count_map.items())

        count_list.sort()
        return ''.join([f"{ele}{count if count > 1 else ''}" for ele, count in count_list])
        


print(Solution().countOfAtoms("Mg(H2O)N"))