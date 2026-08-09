# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)

#Operations on sets
s={1,8,2,3}
print(len(s)) #returns length of the set

s.remove(8) #updates the set s and removes 8 from it 
print(s)

s.pop() #removes an arbitrary element from set and returns the element removed
print(s)

s.clear() #entities the set
print(s)

s1={1,2,3,4}
s1.union({8,11}) #returns the new set with all items from both sets


s1.intersection({8,11}) #returns a set which contains only items in bth sets

one={1,2,3,4}
#to find intersection of sets
print(one & {1,3})
#to find union of sets
print(one | {1,3,7})
print(one-{1,2,3,4})
print(type(one-{1,2,3,4}))
print(type({}))  #empty paranthese is always dictionary . and empty set i.e. set() is always set
#that's why we denote empty set as set() and not as {}