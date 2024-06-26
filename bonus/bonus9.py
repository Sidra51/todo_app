'''password=input("enter new password:")
result=[]
if len(password)>=8:
    result.append(True)
else :
    result.append(False)
digit=False
for i in password:
     if i.isdigit():
         digit=True
result.append(digit)
uppercase=False
for i in password:
    if i.isupper():
        uppercase=True
result.append(uppercase)


print(result)
print(all(result))
if all(result) == True:
    print("strong password")
else :
    print("weak password")'''


password=input("enter new password:")
result={}
if len(password)>=8:
    result["length"]=True
else :
    result["length"]=False
digit=False
for i in password:
     if i.isdigit():
         digit=True
result["digits"]=digit
uppercase=False
for i in password:
    if i.isupper():
        uppercase=True
result["upper_case"]=uppercase


print(result.values())
print (all(result))
if all(result.values()) == True:
    print("strong password")
else :
    print("weak password")