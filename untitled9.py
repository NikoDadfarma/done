
def capitalize_last_name(name:str)->str:
    nameList=name.split(' ')
    firstname=nameList[0].title()
    lastname=nameList[1].upper()
    newstr=''.join([firstname,lastname])
    return newstr

        
    

def main():
    firstInput=4
    try:
        if not isinstance(firstInput, str):
            raise TypeError('run input') 
            
        print(capitalize_last_name(firstInput))
    except TypeError as tE:
        print(tE)
    
        
            
    
if __name__ == "__main__":
    main()
    