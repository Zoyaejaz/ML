n=[1,2,3]
m=n
print(m)
print(n)
print(m==n) # it will return true because both m and n are pointing to the same list(same reference point in a memory)
print(m is n) # it will return true because both m and n are pointing to the same list(same reference point in a memory)

m=[1,2,3]
print(m==n) # it will return true because both m and n have same values (but do not have same reference point in a memory)
print(m is n) # it will return false because both m and n do not have same reference point in a memory(as we have reassigned m to a new list in the 8th line)