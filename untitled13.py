import os
path=r"C:\Users\Lenovo\Desktop\maktab\BootCamp\2_week\tamrin"
os.chdir(path)
def read_files(file_new):
    with open(file_new,'r') as file:
        content=file.read()
        return content

    
    
newlist=[]
for file in os.listdir():
    if file.endswith('.txt'):
        file_new=f"{path}/{file}"
        newlist.append(file_new.split(' '))
with open("file2.txt","w") as file:
    for item in newlist:
        file.write(read_files(item))

lastList=[]
newOtherList=(read_files('file2.txt'))
for i in range(len(newOtherList)):
    
    for j in range(len(newOtherList)):
        if newOtherList[i]==newOtherList[j]:
            lastList.append(newOtherList[j])
print(lastList)
    
