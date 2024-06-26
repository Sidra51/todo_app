'''feet_inches=input("enter feet and inches:")
def convert(feet_inches):
    parts=feet_inches.split(" ")
    feet=float(parts[0])
    inches=float(parts[1])
    meters= feet * 0.3048 + inches * 0.0254
    return f"feet is {feet} and inches is {inches} is equal to {meters} is meters"
print(convert(feet_inches))'''


feet_inches=input("enter feet and inches:")
def convert(feet_inches):
    parts=feet_inches.split(" ")
    feet=float(parts[0])
    inches=float(parts[1])
    meters= feet * 0.3048 + inches * 0.0254
    return meters
result=convert(feet_inches)
if result<1:
    print("kids cannot participate")
else:
    print("kid can participate")