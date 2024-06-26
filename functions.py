'''def get_todos(filepath="todos1.txt"):
    #for reading file
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg,filepath="todos1.txt"):
    #for writing file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
print("heyyyy")
if __name__=="__main__":
    print("hello fro function")
    print(get_todos())'''


'''def get_todos(filepath="todos1.txt"):
    with open(filepath,'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local
def write_todos(todos_arg,filepath="todos1.txt"):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
if __name__=="__main__":
    print("helllo")
    print(get_todos())'''


''' so here by assigning file with diff name can help in timesaving if we need to chnage the name just we need to chmge line 27
insted of going in gettodos and write todos function'''
FILEPATH="todos1.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("helllo")
    print(get_todos())

