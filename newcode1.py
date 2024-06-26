'''filenames=['a.txt','b.txt','c.txt']
for filename in filenames:
    file=open(filename,'r')
    content= file.read()
    print(content)'''

'''numbers = [10.1, 12.3, 14.7]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)'''



import glob
myfiles=glob.glob("file/*.txt")
for filepath in myfiles:
    with open (filepath,"r") as file:
        print(file.read())
print(myfiles)


