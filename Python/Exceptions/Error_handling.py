file =open('youtube.txt','w')
try:
    file.write('hello')
finally:
    file.close()

#either we write the above code or we can write the lower code which is more efficient and better to use
with open('youtube.txt','w') as file:
    file.write('hello')