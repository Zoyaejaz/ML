#List uniqueness Checker
list=["apple","banana","orange","apple","mango"]
for item in list:
    if(list.count(item)>1):
        print(f"{item} is not unique in list")
        break
    else:
        print("There is no duplicate in the list")
        break

#or we can also do it by using set
list=["apple","banana","orange","apple","mango"]
unique=set()
for item in list:
    if item in unique:
        print("Duplicate: ",item)
        break
    else:
        unique.add(item)
