
#convert to string and reverse, then turn back into int
def reverseBits(n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)

#using actual bit manipulations
def reverseBits(n: int) -> int:
        result = 0
        for i in range(32):
            n_binary_rep = f"{n:032b}"
            result = (result << 1) | (n & 1)
            binary_rep = f"{result:032b}"
            n >>= 1
        return result

n = 43261596
result = reverseBits(n)
print(result)