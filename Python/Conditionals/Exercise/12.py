#Password strength checker
password=input("Enter your password: ")
if(len(password)<6):
    print("The password is weak")
elif len(password)<=10:
    print("The password is medium")
else:
    print("The password is strong")