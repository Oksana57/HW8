import csv
import input_data
import sys

def prompt():
    
    print('Что вы хотите делать со списком сотрудников? ')
    menu_l=['посмотреть', 'дополнить', 'удалить', 'найти']
    for i, value in enumerate(menu_l, start=1):
        print(f'\t{i}, {value}')
    print()


def user_input():    
    n=int(input('выберете пункт меню: '))
    return n


def find_contact():
    Id=input('введите код Id')
    book1=input_data.read_person()
    for i in range(len(book1)):
        for j in range(len(book1[i])):
            if book1[i][0]==Id:
            # if number in book1[i]:
                return 'Такой сотрудник есть'
            else:
                return 'Такого сотрудника нет'
    return


# print(find_contact())


def add_person():
    person1 = input_data.person()
    return person1

# print(add_person())

def person_for_rewrite():
    key1 = ['ID', 'surname', 'name', 'phone', 'position', 'department']
    person_n = []
    person1 = input_data.read_person()

    # contact = [c_surname, c_name, c_phone, c_info]
    # dict1 = {key1[j]: contact1[j] for j in range(len(key1))}
    for i in range(len(person1)):
        for j in range(len(person1[i])):
            dict1 = {key1[j]: person1[i][j] for j in range(len(key1))}
        person_n.append(dict1)

    # return contact1
    return person_n

# print(person_for_rewrite())

def rewrite():
    book1 = person_for_rewrite()
    book2 = add_person()
    book_rewrite = []
    book_rewrite = book1+book2

    return book_rewrite

# print(rewrite())



def add_file():
    csv_file = 'data.csv'
    book = rewrite()
    dict1 = book
    csv_columns = ['ID', 'surname', 'name', 'phone', 'position', 'department']
    try:
        with open(csv_file, 'w') as file_c:
            writer=csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="-")
            writer.writeheader()
            for data in dict1:
                writer.writerow(data)
    except IOError:
        print('I/O error')
    return


# add_file()

def del_person():
    Id=str(input('введите код Id'))
    contact1=[]
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        cont2=csv.reader(file1, delimiter="-")
        count=0
        n=csv.field_size_limit(sys.maxsize)
        for row in cont2:
            if count==0:
            #     alist = ' '.join(row).split()
                count+=1
                continue 
            if 0<count<n:           
                contact1.append(row)               
            count+=1
        for i in range(len(contact1)):
            # for j in range(1):
            if Id == contact1[i][0]:
            
                break

        del contact1[i]
        # break
    return contact1
#
# contact2=del_person()
# print(contact2)

def personal_new():
    contact2=del_person()
    key1=['ID', 'surname', 'name', 'phone', 'position', 'department']
    dict2={}
    book=[]
    for i in range(len(contact2)):
        dict2 = {key1[j]: contact2[i][j] for j in range(len(key1))}
        book.append(dict2)   
    
    return book

# book=personal_new()
# print(book)

def new_version():
    book=personal_new()
    dict=book
    csv_columns = ['ID', 'surname', 'name', 'phone', 'position', 'department']
    csv_file='data.csv'
    try:
        with open(csv_file, 'w') as file_c:
            writer=csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="-")
            writer.writeheader()
            for data in dict:
                writer.writerow(data)
    except IOError:
        print('I/O error')  
    return

# new_version()