

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    found_uncompleted = []
#    for task in list:
#        if task["completed"] == False:
    found_uncompleted = get_tasks_by_status(list,False)
    
    return(found_uncompleted)

## Get a list of completed tasks
def get_completed_tasks(list):
    found_completed = []
 #   for task in list:
 #       if task["completed"] == True:
    found_completed = get_tasks_by_status(list,True)
    
    return(found_completed)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    found_time = []
    for task in list:
        if task["time_taken"] >= time:
            found_time.append(task)
    return(found_time)


## Find a task with a given description
def get_task_with_description(list, description):
     found_desc = []
     for task in list:
        if description.upper() in task["description"].upper():
            found_desc.append(task)
     return(found_desc)

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    found_status = []
    for task in list:
        if task["completed"] == status:
            found_status.append(task)
    return(found_status)

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)




