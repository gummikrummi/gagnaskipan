#modulus without using mathematical operators like *, / or % 
def modulus(num, div): 
    if num < div: 
        return num 
    else: 
        return modulus(num - div, div) 
print(modulus(13, 4)) 
print(modulus(12, 3)) 
print(modulus(14, 3))