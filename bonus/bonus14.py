from bonus.converters14 import convert
from bonus.parsers14 import parse
#from parsers14 import parse

feet_inches=input("enter feet and inches:")

parsed= parse(feet_inches)
result= convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet {parsed['inches']} inches is equal to {result}")

if result<1:
    print("kids cannot participate")
else:
    print("kid can participate")