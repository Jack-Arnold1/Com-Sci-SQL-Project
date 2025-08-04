# main .py file :)

import sqlite3

conn = sqlite3.connect('musicstore.db')
cursor = conn.cursor()
# --- TABLE CREATING ---
# Table for staff members 
cursor.execute('''CREATE IF NOT EXISTS TABLE staff (phoneNumber INTEGER PRIMARY KEY, name string NOT NULL, ''')

# Table for customers
cursor.execute('''CREATE IF NOT EXISTS TABLE customer (phoneNumber INTEGER PRIMARY KEY, name string NOT NULL, ''')
def main():
    print("""
    Welcome to Countdown Rehearsal Studio!
    What would you like to do?"""
    )
    print("""
    1) Book a Session
    2) Cancel a Session
    3)
    4)
    5) Exit Program
        """
    )
    if choice == 1:
        1
    if choice == 2:
        1
    if choice == 3:
        1
    if choice == 4:
        1
    if choice == 5:
        print("Thank you for using the program!!! Bye!!!!")