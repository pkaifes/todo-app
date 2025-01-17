# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:12:15 2024

@author: frost
"""
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Retrieves to-do list from default file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        #todos_local = [todo.strip() for todo in todos_local]
    return todos_local


def write_todos(todo_list, filepath=FILEPATH):
    """save to-do list to default file"""
    #save and close to datasource
    #todo_list = "\n".join(todo_list)
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list)



if __name__ == "__main__":
    #If this file is ran, __name__ == "__main__"
    #If this file is ran from main.py, __name__ = functions
    print("Hello From Functions!")