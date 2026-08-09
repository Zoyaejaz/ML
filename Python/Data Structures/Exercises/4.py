#Create an empty dict. allow 4 friends to enter their favourite lang as values and use keys as their names. Assume that the names are unique.
dict={}
for i in range(4):
    name=input("Enter your name: ")
    lang=input("Enter your favourite language: ")
    dict[name]=lang
print(dict)

#if names(keys) of 2 friends are same
#--->if it is same then the second entry will simply overwrite the first. it will write the unique keys only. and if we have same name 2 keys,then it will write the first one and ignore the second one

#if the languages of two friends are same.
#---->nothing happen it will perfectly works bcz the values can be same but the key should not be same