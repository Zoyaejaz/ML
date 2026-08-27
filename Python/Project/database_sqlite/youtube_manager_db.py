# Import the sqlite3 module
# sqlite3 is a built-in Python library used to work with SQLite databases
import sqlite3

# Connect to the SQLite database
# If 'youtube_videos.db' already exists, it will open that database
# If it does not exist, SQLite will automatically create it
conn=sqlite3.connect('youtube_videos.db')

# Create a cursor object
# The cursor is used to execute SQL commands on the database
cursor=conn.cursor()

# Execute an SQL command to create the videos table
# CREATE TABLE IF NOT EXISTS means:
# "Create this table only if it doesn't already exist"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
    id  INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    # fetchall() gets all the rows returned by the SQL query
    # Each row is returned as a tuple
    for row in cursor.fetchall():  
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))

    # Save the changes permanently to the database
    # Without commit(), the inserted data may not be saved
    conn.commit()

def update_video(video_id,new_name,new_time):
    # The ? symbols are placeholders
    # Their actual values are provided separately in (name, time)
    cursor.execute("UPDATE videos SET name =?, time=? WHERE id=?", (new_name,new_time,video_id) )
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id=?",(video_id,))
    conn.commit()

def main():
    # while True creates an infinite loop
    # The menu will continue appearing until we use "break"
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice=input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice =='2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter video ID to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter video ID to update: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid input")

# Close the database connection after the program finishes
# This releases the database resource
    conn.close()


if __name__=="__main__":
    main()
