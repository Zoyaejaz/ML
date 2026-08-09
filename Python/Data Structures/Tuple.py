#Tuple is an ordered immutable data type
tup1=()
tup2=('Geeks','For')
print("\nTuple  with the use of  String. ", tup2)  #The creation of a Python tuple without the use of parentheses is known as Tuple Packing. 

#access tupe items
tup1=(1,2,3,4,5)
print(tup1[0])
print(tup1[-1])
print(len(tup1))
print(type(tup1))

#empty  tuple
a=()
#tuple with only one element needs a comma
a=(1,)
#tuple with more than one element
a=(1,7,2)

#tuple methods
print(tup1.count(1))
print(tup1.index(3))

tea=("Herbal","Green","Black","Herbal")
print(tea.count("Herbal"))