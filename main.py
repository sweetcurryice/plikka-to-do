import functions
import time

currTime = time.strftime("%b %d, %Y %H:%M:%S ")
print("The time now is :", currTime)
while True:
    user_input = input("add / show / edit / finish / exit ?\n")
    user_input = user_input.strip()
    todos = []



    if user_input.startswith('add'):
        todo = user_input[4:] + "\n"

        todos = functions.readfile()
        
        
        todos.append(todo)
        functions.writefile(todos)

        
    elif user_input.startswith('show'):
        todos = functions.readfile()

        new_todos = [item.strip('\n') for item in todos]
        functions.display_todo(new_todos)
    
    elif user_input.startswith('edit'):
        try:
            idx_no = int(user_input[5:])
            idx_no = idx_no - 1
            
            todos = functions.readfile()

            new_todo = input("enter the new todo: ")
            todos[idx_no] = new_todo + '\n'

            functions.writefile(todos)

            print("okay Done!\nhere are the results:")
            new_todos = [item.strip('\n') for item in todos]
            functions.display_todo(new_todos)

        except ValueError:
            print("The Command is not valid")


    elif user_input.startswith('finish'):
        try:
            idx_no = int(user_input[7:])

            todos = functions.readfile()

            todos.pop(idx_no-1)

            functions.writefile(todos)
            new_todos = [item.strip('\n') for item in todos]
            functions.display_todo(new_todos)
        except IndexError:
            print(f"invalid! The last element is {len(todos)}, please type a number within {len(todos)}.")
        except ValueError:
            print("The command is invalid")

    
    elif user_input.startswith('exit'):
        break
    
    else: 
        print("the command is not valid")