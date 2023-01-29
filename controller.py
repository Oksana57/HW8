import input_data
import model

def start():
    input_data.save_person()
    model.prompt()
    n=model.user_input()
    if n==1:
        print(input_data.read_person())
    elif n==2:
        model.add_file()
    elif n==3:
        model.new_version()    
    elif n==4:
        print(model.find_contact())

# start()