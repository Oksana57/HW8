
import csv
import sys

id=0

def get_ID():
    global id
    id+=1
    return id

def save_ID():
     global id
     with open ('id.txt', 'w', encoding='UTF-8') as file:
        file.write(str(id))

def get_from_file():
    global id
    with open ('id.txt', 'r', encoding='UTF-8') as file:
        file.read(int(id))

# get_ID()
# save_ID()
