#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tasks = [
    {'name' : 'Write email to Jan', 'completed' : True},
    {'name' : 'Sweep front porch', 'completed' : True},
    {'name' : 'Call mom', 'completed' : False}
]

def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))
    

def add_task():
    task_text = input('Please add a task: ')
    new_task = {'name': task_text, 'completed': False}
    tasks.append(new_task)

    
def remove_task():
    list_tasks()
    to_be_removed = int(input('Input the number of the task to be removed '))
    tasks.remove(tasks[to_be_removed])
    

def task_completed():
    list_tasks()
    marked_complete = int(input('Input the number of the task to mark as complete '))
    tasks[marked_complete]['completed'] = True
    
    
menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    
    if decision == '1':
        list_tasks()

    elif decision == '2':
        add_task()
        
    elif decision == '3':
        remove_task()
        
    elif decision == '4':
        task_completed()
    
    elif decision == '5':
        program_is_running = False
        
    else:
        print('please choose a valid option')



# In[ ]:




