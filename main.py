# -*- coding: utf-8 -*-
"""
#123524C9A0DC4337488A9A5B50C878
Created on Fri Nov  1 13:06:22 2024
@author: Pkaifes
"""
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %y %H:%M:%S")
Intro_Text = """
Welcome to ToDo Tasks
options: add, show, edit, complete, exit
example: add do the dishes
"""
print("It is: ", now)
print(Intro_Text)


application_run = True


#read from datasource
with open("todos.txt","r") as file:
      todos = file.readlines()

file.close()
todos = [todo.strip() for todo in todos]



#Active Applications
while True:
    user_action = input("type an option: ")
    user_action = user_action.strip()
    
   
        
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        todos.append(todo)
        
        write_todos(todos)
        
    elif user_action.startswith("show"):
        for i, item in enumerate(todos):
            print(f"{i+1}: {item.title()}")
            
    elif user_action.startswith("edit"):
        try:
            edit_num = int(user_action[5:])
            replacement = input("Enter edit: ")
            todos[edit_num-1] = replacement
            
            write_todos(todos)
        except ValueError:
            print("Your command is not valid, try: edit [number]")
            continue
    
    elif user_action.startswith("complete"):
        try:
            complete_num = int(user_action[9:])
            todos.pop(complete_num-1)
            
            write_todos(todos)
        except ValueError:
            print("Your command is not valid, try: edit [number]")
            continue
        
    elif user_action.startswith("exit"):
        print("Bye!")
        break
    
    else:
        print("Unknown command")
        

