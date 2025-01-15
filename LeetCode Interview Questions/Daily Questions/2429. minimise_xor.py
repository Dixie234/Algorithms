import math

#num1 has more bits than num2
#num1 = 1001110 num2= 0001010
#num1_bits = 4 num2_bits = 2
#when there is a 1 in num1, match it, until you run out of 1's, then pad with 0's
#result = 1001000

#num1 has less bits than num2
#num1 = 0001010 num2= 1001110
#num1_bits = 2 num2_bits = 4
#when there is a 1 in num1, match it, use any leftover 1's on the lowest 0's possible
#result = 0001111

#use bin(num) function to get binary representation of a number
def minimizeXor(num1: int, num2: int) -> int:
    nums2_bits = f'{num2:b}'.count("1")
    nums1_binary = f'{num1:032b}'
    nums1_bits = nums1_binary.count("1")
    result = [0] * 32
    if nums1_bits == nums2_bits:
        return num1
    elif nums1_bits > nums2_bits:
        index = 0
        while nums2_bits > 0:
            if nums1_binary[index] == "1":
                result[index] = 1
                nums2_bits -= 1
            index += 1
    else:
        for i in range(len(result)):
            if nums1_binary[i] == "1":
                result[i] = 1
                nums2_bits -= 1
        index = -1
        while nums2_bits > 0:
            if result[index] == 0:
                result[index] = 1
                nums2_bits -= 1
            index -= 1
    return sum([(2 ** i) * bit for i, bit in enumerate(result[::-1])])
            
                    
num1 = 78          
num2 = 10
result = minimizeXor(num1, num2)
print(result)

