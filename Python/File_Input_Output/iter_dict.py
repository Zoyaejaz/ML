#for dictionary
myDict={"a":1,"b":2,"c":3}
D=iter(myDict)
print(D)
print(D.__next__())
print(D.__next__())
print(D.__next__())
print(D.__next__())  #after this the dictionary gets fully iterated and it will give us an error as StopIteration because there is no more element to iterate in the dictionary
print(D)