#Counting positive numbers
nums=[1,-2,3,-4,5,6,-7,-8,9,10]
count=0
for i in nums:
    if(i>0):
        print(i)
        count+=1
print("Total positive numbers:",count)
