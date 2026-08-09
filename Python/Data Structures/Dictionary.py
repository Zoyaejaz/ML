# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)


# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

#Accessing key-value in dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks','stream':'engineering'}

# Accessing an element using key
print(d['name'])

#To update the value of a key in dictionary we can use the key and assign the new value to it
d['name']="Zoya"  #we can add new key-value pair in the dictionary by using new key and assigning value to it
print(d)

#using pop() method to delete a key-value pair from the dictionary,here we have to pass the key as an argument to pop() method and it will delete the key-value pair and return the value of the deleted key
print(d.pop(1))
print(d)


#using popitem() method to delete the last key-value pair from the dictionary and return it as a tuple
print(d.popitem())
print(d)

#it will give us the number of key-value pairs in the dictionary
print(len(d))

# Accessing a element using get
print(d.get(3))

#METHODS
a={"name":"Zoya","from":"India", "marks":[92,98,96]}
print(a.items())  #returns a list of (key,value) tuples

print(a.keys())  #return a list containing dictionary's keys

a.update({"food":"Cake"}) #updates the dictionary with supplied key-value pairs
print(a)

print(a.get("name")) #returns a value of the specified keys



#writing multiple dictionary in one dictionary
tea_shop={
    "chai":{"Masala":"spicy","Ginger":"Zesty"},
    "tea":{"Green":"Mild","Black":"Strong"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Masala"])

#Dictionary comprehension
squares={x:x**2 for x in range(5)}
print(squares)


#to put the same default value for all the keys in dictionary we can use fromkeys() method
keys=["Masala","Ginger","Lemon"]
default="delicious"
d=dict.fromkeys(keys,default)
print(d)
d=dict.fromkeys(keys,keys)
print(d)