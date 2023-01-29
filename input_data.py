import id
import csv
import sys
# import import_export



def add_depart():
    depart_list=[]
    while True:
        for i in range(1,1000):
            depart=input('Введите название отдела: ') 
            depart_list.append(depart)
            print('хотите ввести еще? введите "да" или "нет": ')
            answer=input()

            if answer=='да':
             
                continue
               
            elif answer=='нет':

                break
        
        return depart_list
    
# print(add_depart())


def depart():
    alist=add_depart()
    dict1={}
    depart_list=[]
    for i in range(len(alist)):
    # for i, value in enumerate(alist, start=1):
        dict1={i+1: alist[i]}
        depart_list.append(dict1)
    #     print(f'\t{i}, {value}')
    # print()
    return depart_list

# print(depart())


def save_depart():
    depart_list=depart()
    try:
        with open('department.csv', 'w', encoding="UTF-8") as file:
            for i in range(len(depart_list)):

                file.write(f'{depart_list[i]}\n')
    except IOError:
        print('I/O error')  
    return

# save_depart()


def read_depart():
    depart=[]
    with open('department.csv', 'r', encoding="UTF-8") as file:
            n = csv.reader(file, delimiter="\n")
            for row in n:
                for i in range(len(row)):
                    row=str(row[i]).replace('{', '').replace('}', '')
                    depart.append(row)
    print(depart)


def person():
    book=[]
    # dict2={}
    while True:
        for i in range(1,1000):
            id_p = id.get_ID()
            c_surname=input('Введите фамилию сотрудника: ')
            c_name=input('Введите имя сотрудника: ')
            c_phone=input('Введите телефон: ')
            c_info=input('Введите должность: ')
            read_depart()
            c_depart=input('Выберите код отдела из списка')
            key1=['ID', 'surname', 'name', 'phone', 'position', 'department']
            contact=[id_p, c_surname, c_name, c_phone, c_info, c_depart]
            dict1 = {key1[j]: contact[j] for j in range(len(key1))} 
            # book.append(contact)
            book.append(dict1)
            print('хотите ввести еще? введите "да" или "нет": ')
            answer=input()

            if answer=='да':
             
                continue
               
            elif answer=='нет':

                break
        # id.save_ID()
        return book
    
# print(person())    


def save_person():
    book2=person()
    csv_columns = ['ID', 'surname', 'name', 'phone', 'position', 'department']
    dict = book2
    csv_file = 'data.csv'
    try:
        with open(csv_file, 'w') as file_c:
            writer = csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="-")
            writer.writeheader()
            for data in dict:
                writer.writerow(data)
    except IOError:
        print('I/O error')  
    return

# save_person()

def read_person():
    person=[]
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
                person.append(row)               
            count+=1
        
    # print(person)
    return person

# print(read_person())