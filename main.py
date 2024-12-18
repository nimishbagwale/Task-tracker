import datetime

global_id = 1

def load_last_id():
    global global_id
    try:
        with open("last_id.txt", "r") as f:
            global_id = int(f.read().strip()) + 1 
    except FileNotFoundError:
        pass

def save_current_id():
    with open("last_id.txt", "w") as f:
        f.write(str(global_id - 1))

def find_the_task(prompt):
    task = ""
    flag = 0
    for i in prompt:
        if i == '"' :
            flag += 1
            continue
        if(flag == 1):
            task += i
    return task

def find_id(prompt):
    return (prompt.split())[1]

class Task:
    def __init__(self, user_input):
        self.id_ = global_id  # Use the global ID
        self.description_ = find_the_task(user_input)
        self.status = "todo"
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.task_entry = {
            "id" : self.id_,
            "description" : self.description_,
            "status" : self.status,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
        }

    def mark(self, arg):
        id_ = find_id(arg)
        status = (arg.replace("mark-", "")).replace(f" {id_}", "")
        self.update("status", id_, status)

    def add(self, content):
        global global_id 
        self.description_ = content
        with open("dat.txt", "a+") as file:
            for i in self.task_entry.keys():
                file.write(f"{i} : {self.task_entry[i]} , ")
            file.write("\n")
        global_id += 1

    def update(self, opt, id_, content):
        with open("dat.txt", "r") as file:
            data = file.readlines()
        for line in data:
            line_parts = line.split(",")
            if id_ == line_parts[0].split(" : ")[1].strip():
                if opt == "task":
                    index = data.index(line)
                    line_parts[1] = f"description : {content}"
                    line = ", ".join(line_parts)
                    data[index] = line
                    break
                elif opt == "status":
                    index = data.index(line)
                    line_parts[2] = f" status : {content}"
                    line = ",".join(line_parts)
                    data[index] = line
                    break
        with open("dat.txt", "w") as file:
            for i in data:
                file.writelines(i)

    def delete(self, id_):
        with open("dat.txt", "r") as file:
            data = file.readlines()
        for line in data:
            line_parts = line.split(",")
            if id_ == line_parts[0].split(" : ")[1].strip():
                data.remove(line)
                break
        with open("dat.txt", "w") as file:
            for i in data:
                file.writelines(i)

    def list(self):
        with open("dat.txt", "r+") as file:
            data = file.readlines()
            for i in data:
                print((((i.split(","))[1]).split(":"))[1])

def main():
    load_last_id()
    user_input = input().lower()
    prompt = Task(user_input)
    if "add" in user_input:
        prompt.add(find_the_task(user_input))
        save_current_id()
        main()
    elif "update" in user_input:
        prompt.update("task", find_id(user_input), find_the_task(user_input))
        main()
    elif "delete" in user_input:
        prompt.delete(find_id(user_input))
        main()
    elif "list" in user_input:
        prompt.list()
        main()
    elif "mark" in user_input:
        prompt.mark(user_input)
        main()
    elif "exit" in user_input:
        return
    else:
        print(f"Invalid command entered !! Try again .....")
        main()

print("\n======= add / list / delete / update / mark / exit ======= ")
main()
