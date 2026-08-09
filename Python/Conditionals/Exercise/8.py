#fruit ripeness checker
fruit="banana"
color=input("Enter the colour of the fruit: ")
if(fruit=="banana"):
    if(color=="green"):
        print("The fruit " +fruit + " is unripe")
    elif(color=="yellow"):
        print("The fruit" +fruit + " is ripe")
    elif(color=="brown"):
        print("The fruit " +fruit + " is overripe")
    else:
        print("Invalid colour entered")