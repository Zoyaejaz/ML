f=open("File_Input_Output/email.txt","r")
email=f.read()
f.close()
print(email)

""" Line 1: f = open("email.txt", "r")

->Calls Python’s open() to open the file named "email.txt".
->The "r" means open in read mode (you won’t write to it).
->open() returns a file object and that object is stored in the variable f.
->If the file doesn’t exist, Python raises FileNotFoundError.

Line 2: email = f.read()

->Calls the read() method on the file object f.
->read() reads the entire file contents and returns them as a string. That string is stored in the variable email.
->If the file is very large, read() can use a lot of memory; for big files prefer reading line-by-line or in chunks.

Line 3: f.close()

->Closes the file object f and frees the system resource (file descriptor).
->After closing, using f.read() or other I/O on f will raise an error (I/O operation on closed file).
->Closing is important to avoid resource leaks and to ensure data is flushed (for writes).

Tip: It’s safer to open files with a with statement so Python closes them automatically when you’re done."""