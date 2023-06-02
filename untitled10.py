def calculator(first,secound,operatorr):
    x=None
    if operatorr=='+':
        plus=first+secound
        x=plus
    elif operatorr=='-':
        sub=first-secound
        x=sub
    return x
    

def main():
    inputt=input().split(' ')
    firstNum=inputt[0]
    operator=inputt[1]
    secoundNum=inputt[2]
    
    try :
        firstNumToFloat=float(firstNum)
        secoundNumToFloat=float(secoundNum)
        if not len(inputt)==3 and (operator=='+' or operator=='-'):
            raise TypeError('input error')
        if not isinstance(firstNumToFloat and secoundNumToFloat
                          , float) :
            raise ValueError('not float first number')
        print(calculator(firstNum, secoundNum, operator))
    except TypeError as fE:
        print(fE)
    except ValueError as vE:
        print(vE)

if __name__ == "__main__":
    main()
print('hello world')