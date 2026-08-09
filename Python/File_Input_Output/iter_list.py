#for list
myList=[1,2,3,4]
I=iter(myList)
print(iter(myList) is I)  #it will return false because every time we call iter() it creates a new iterator object and assigns it to I, so the previous iterator object is lost and we cannot access it anymore. Therefore, when we compare iter(myList) with I, it will return false because they are two different objects in memory.
print(I)
print(I.__next__())
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())  #after this the list gets fully iterated and it will give us an error as StopIteration because there is no more element to iterate in the list
print(I)



