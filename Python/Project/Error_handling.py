file=open('youtube.txt','w')

try:
    file.write("Zoya Ejaz")
finally:
    file.close()       #in try and finallly we have to close the file by our own

# either we can prefer the above try and finally syntax or below syntax  to open the file,read and write the file.

with open('youtube.txt','w') as file:  #using with will automatically close the file after work
    file.write("hello i am Zoya")