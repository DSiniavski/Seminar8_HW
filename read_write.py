def write_file(data):
    with open('db.csv','a',encoding ='utf-8') as file:
        file.writelines(data)
          
def read_file():
    with open('db.csv','r',encoding ='utf-8') as file:
        return file.readlines()
    

    