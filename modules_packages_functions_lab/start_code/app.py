
from Modules.task_list import add_to_list, get_completed_tasks, get_task_with_description, get_task_with_description, get_task_with_description, get_tasks_by_status, get_tasks_taking_at_least, get_uncompleted_tasks
from Modules.output import print_list, print_menu, print_task
from Data.task_list import tasks
from Modules.input import get_description


while (True):
    print_menu()
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = get_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")