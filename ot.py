def swapnumbers(a:int,b:int)->[int]:
    
        a = a+b 
        b=a-b 
        a=a-b 
        
        return [a,b]

print(swapnumbers(31,4))