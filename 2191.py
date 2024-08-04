def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
    def gen(n: int) -> int:
        m = 1
        output = 0
        if n == 0:
            return mapping[n]
        while n > 0:
            r = n%10
            output += m * mapping[r]
            m *= 10
            n //= 10
        return output


    output_list = [ (n, gen(n)) for n in nums]
    print(output_list)
    ans = [n[0] for n in sorted(output_list, key = lambda i: i[1])]

    return ans
        
        
print(sortJumbled( [9,8,7,6,5,4,3,2,1,0] , [0,1,2,3,4,5,6,7,8,9]))