Task Tracker CLI
URL: https://roadmap.sh/projects/task-tracker

Description
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

#Requirements

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

1. Use positional arguments in command line to accept user inputs.
2. Use a JSON file to store the tasks in the current directory.
3. The JSON file should be created if it does not exist.
#Task Properties Each task should have the following properties:

1. id: A unique identifier for the task
2. description: A short description of the task
3. status: The status of the task (todo, in-progress, done)
4. created_at: The date and time when the task was created
5. updated_at: The date and time when the task was last updated
6. Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.
Usage
# Adding a new task
python task_cli.py add "Buy groceries"

# Updating a task
python task_tracker_cli.py update 1 "Buy groceries and cook dinner"

# Deleting a task
python task_tracker_cli.py delete 1

# Mark a task as in progress
python task_tracker_cli.py mark-in-progress 1

# Mark a task as done
python task_tracker_cli.py mark-done 1

# List all tasks
python task_tracker_cli.py list

# List tasks by status
python3 task_tracker_cli list done
python3 task_tracker_cli list todo
python3 task_tracker_cli list in-progress
