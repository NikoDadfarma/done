inputt=input()
try :
    tryInt=True
    f = int(inputt)
    
except ValueError as inputtVe:
    tryInt=False
    print(inputtVe)
    
finally:
    if tryInt:
        print('input was successfully converted')
    else:
        print('input was not successfully converted')
   
        
        

