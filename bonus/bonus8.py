date=input("enter todays date:")
mood=input("rate your mood today out of 10:\n")
thoughts=input("write your  thoughts here:\n")
with open(f"../journal/{date}.txt",'w') as file:
     file.write(mood+ 2 * "\n")
     file.write(thoughts)