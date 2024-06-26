try:
    width=float(input("enter rectangular width:"))
    length=float(input("enter rectangular length:"))
    if width==length:
        #print("we dont accept squares,bye bye")
        #exit()
        exit("we dont accept squares,bye bye")
    area=length*width
    print(area)
except ValueError:
    print("enter number in words,thankyou")