import csv
print("hello")
fo=open("abc.txt","r")
s=fo.read(100)
# fo.write("This is the first line")
print(s)
fo.close()

with open('/home/muppuri/Downloads/S&P500_Stock_Data (1).csv','r') as f:
    readCsv = csv.reader(f,delimiter=",")
    stock= list(readCsv)
print(stock[0])
selected=[]
for row in stock[1:6]:
    selected.append(row)
print(selected)

#read binary file
import pickle
with open("file.dat","rb") as f:
    while True:
        try:
            row=pickle.load(f)
            print(row)
        except EOFError:
            break
#copy one file contents to another file (binary)
import pickle 
f1=open("data.dat","rb")
f2=open("new.dat","wb")
while True:
    try:
        row=pickle.load(f1)
        pickle.dump(row,f2)
    except EOFError:
        break
f1.close()
f2.close()

#update any row if any condition satisified
with open("employee.dat",'rb+') as f:
    while True:
        try:
            record_pos=f.tell
            row=pickle.load(f)
            if(row[0] == 'E002'):
                row[2] = 50000
                f.seek(record_pos,0)
                pickle.dump(row,f)
        except EOFError:
            break
            
#write binary file
import pickle
with open("file.dat","wb") as f:
    while True:
        op=int(input("enter 1 to add data, 0 to quit"))
        if op==1:
            name=input("Endter name")
            rollno=int(input("Enter roll number"))
            pickle.dump((name,rollno),f)
        elif op==0:
            break
