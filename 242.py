def isAnagram(s: str, t: str) -> bool:
    str1 = list(s)
    str2 = list(t)

    str1.sort()
    str2.sort()

    if str1 == str2:
        return True
    return False
    
    
print(isAnagram('anagra','nagaram'))