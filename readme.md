# TaskTraker CLI

python program for keeping track of tasks

## Operations

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

## How to Run

from terminal `python <filepath>`

## Examples

#### Adding a new task

task-cli add "Buy groceries"

#### Updating and deleting tasks

task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

#### Marking a task as in progress or done

task-cli mark-in-progress 1
task-cli mark-done 1

#### Listing all tasks

task-cli list

#### Listing tasks by status

task-cli list done
task-cli list todo
task-cli list in-progress