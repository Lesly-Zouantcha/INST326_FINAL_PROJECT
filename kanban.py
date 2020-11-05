# Lesly Zouantcha, Evan English, Joey Epstein, Ben Lam

class Kanban:
    """ Takes in the users tasks and moves them through columns(to do, in progress, and done) depending at what stage they are in working on it. 
    Attributes:
       task(str): the task that the user needs to do 
       board(dict): dictionary with all the tasks on the board 
    """
    
	def __init__(self, task):
    """This will Initialize the Dictionary {“To do”: List of tasks in to do, “In Progress”: List of tasks in in progress section, “Done” : List of tasks in done section} 
    Args:
        task(str):Task(str): the job to be done and the the key values in the dictionary
    """

    def add_work_item(self, task):
    """This method will be for implementing the work items that will be required by a boss
    Args:
        task(str):Task(str): the job to be done and the the key values in the dictionary
    """

    def backlog_to_todo(self, task):
    """This method will move tasks from the backlog column to the todo column
    Args:
       task(str):Task(str): the job to be done and the the key values in the dictionary
    """

    def todo_to_inprogress(self, task):
    """ This method will move tasks from the todo column to the in progress  column
    Args:
       task(str): the job to be done and the the key values in the dictionary
    """
            
    def inprogress_to_done(self, task):
    """This method will move tasks from the ‘inprogress’ column to the ‘done’ column
    Args:
       task(str): the job to be done and the the key values in the dictionary
    """

    def edit_work_item(self, task, edit_task)
    """This method will allow the users to edit the work item already on the board if need be.
    Arg:
        Task(str): the job to be done and the the key values in the dictionary
        Edit_task(str): the new task that was revised from the old task  
    """

    def clear_board(self):
    """This method will allow the users to completely clear the board when they want to start a new project"""

    def display_board(self):
    """Display the board in a dictionary with the key values “Backlog”, “To-do”, “ “In Progress”, and “Done””
    Returns: 
        Dictionary: keys will be backlog, to-do, in-progress, and done. The tasks are the values in the dictionary where they are on the board.
    """
