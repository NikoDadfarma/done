with open("firstFile.txt","r") as firstFile:
    text =firstFile.read()
    lines=text.split('\n')
    lenght=len(lines)
    maxx=0
    for i in range(lenght):
        x=''.join(lines[i])
        if len(x)>maxx:
            newList=x.split(" ")
            maxx=len(x)
            indexx=i
    print('max line: ',lines[indexx])
    print('len line:',maxx)
    print('how many word',len(newList))
    
            