#check whether the  gu=iven comment is spam or not
msg=input("Enter your text: ")
if("make a lot of money" in msg) or ("buy now" in msg) or ("subscribe this" in msg)  or("click this" in msg):
    print("The given text is a spam")
else:
    print("The given text is not spam")

#Program to find whether a given username contains less than 10 characters or not
username=input("Enter your username: ")
if(len(username)<10):
    print("It contains less than 10 characters.")
else:
    print("It does not contains less than 10 characters.")

#write a program to find whether the given post is talking about maths or not
post="Hello I am maths. Maths is a logical and interesting subject."
if("Maths" in post):
    print("yes it is  talking about maths.")
else:
    print("no it is not talking about maths.")