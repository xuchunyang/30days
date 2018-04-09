#!/usr/bin/env python

import sys
import shelve                   # 持久化 Python 对象，用字典操作，键为
                                # String，值为任意 Python 对象

# d = shelve.open('database.dat')
# d["username"] = "xuchunyang"
# d.close()

def store_person(db):
    pid = input("Enter unique ID number: ")
    person = {}
    person["name"] = input("Ener name: ")
    person["age"] = input("Ener age: ")
    db[pid] = person

def lookup_person(db):
    pid = input("Enter ID number: ")
    field = input("What would you like to know? (name, age) ")
    field = field.strip().lower()

    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print("The available command are:")
    print("store : Stores information about a person")
    print("lookup : Looks up a person from ID number")
    print("quit : Save changes and exit")
    print("? : Print this message")

def enter_command():
    cmd = input("Enter command (? for help) ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open("/tmp/database.dat")  # GNU DBM
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
    finally:
        database.close()

if __name__ == "__main__":
    main()
