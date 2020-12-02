import sys 
from argparse import ArgumentParser

class Task:
    """Takes in users tasks and gets the id, decription and due date of it
    Attributes:
       task_id(int): id of task 
       description(str): description of what the task is 
       due_date(str): date that the task is due
       new_description(str): the new descripton of the task the user wants to edit
       new_due_date(str): the new due_date of the task the user wans to edit
    """
    def __init__(self,task_id,description,due_date):
        """Tasks in the task information and assigns attributes
        """
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.task = {self.task_id: [self.description, self.due_date]}
        
    def edit_task(self,task_id, new_description, new_due_date):
        """Edits a specific task
        Args:
            task_id(int): id of task 
        new_description(str): the new descripton of the task the user wants to edit
        new_due_date(str): the new due_date of the task the user wans to edit
        Side Effects:
            Changes the input statement 
        """
        self.task[task_id] = [new_description, new_due_date]
        return self.task
                                  
    def __str__(self):
        """This returns the task 
        Returns:
           Returns task as string
        """
        return f"{self.task}"
    
def main(task_id, description, due_date, edit_option = None):
    """ Takes in users task informationa and turn it into a dictionary. It also 
    edits a task if nessesary
    Args:
        task_id(int): id of task 
        description(str): description of what the task is 
        due_date(str): date that the task is due
        edit(str): yes or no if want to edit the task
    """
    task_input = Task(task_id, description, due_date)
    edit = task_input.edit_task(task_id,description,due_date)
    if edit_option == "yes":
        print(f"Edited task: {edit}")
    else:
        print(f"Task: {task_input}")
    
    
def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("task_id", help="id of task")
    parser.add_argument("description", help="task description")
    parser.add_argument("due_date", help="due date of task")
    parser.add_argument("-e", "--edit_option", default="*", help="enter 'yes' if want to edit task")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.task_id, args.description, args.due_date, args.edit_option)