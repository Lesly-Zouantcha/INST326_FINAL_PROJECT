# Lesly Zouantcha, Evan English, Joey Epstein, Ben Lam

class Task:
    """Takes in users tasks and gets the id, decription and due date of it
    Attributes:
       id(int): id of task 
       description(str): description of what the task is 
       due_date(str): date that the task is due
    """
    def __init__(self,id, description, due_date, column, action = None):
        """Tasks in the task information and assigns attributes
        """
        self.id = id
        self.description = description
        self.due_date = due_date
        self.column = column
        self.action = action
        self.task = (self.id, self.description, self.due_date, self.column)
        
        
    def edit_task(self,edit_id, description, due_date):
        """Edits a specific task
        Args:
            id(int): id of task 
       description(str): description of what the task is
       Side Effects:
            Changes the input statement 
        """
        if self.action == 'edit':
            if edit_id == self.id:
                Task(self,id, description, due_date, column, action = None)
              #WORK ON THIS  
                         
            
    def delete_task(self,id):
        """Deletes a specific task
        Args:
            id(int): id of task 
        """
        if self.action == 'delete':
            if delete_id in self.task:
                del self.task    
            
    def __str__(self):
        """This returns the task 
        """
        return f"{self.task}"
    
    
class Kanban:
    """ Takes in the users tasks and moves them through columns
    (to do, in progress, and done) depending at what stage they are in working
     on it. 
    Attributes:
       task(str): the task that the user needs to do #THIS DOESNT MAKE SENSE
       board(dict): dictionary with all the tasks on the board 
    """
    
	def __init__(self):
        """This will Initialize the Dictionary {“To do”: List of tasks in to do,
         “In Progress”: List of tasks in in progress section, “Done” : List of 
         tasks in done section} 
        Args:
        task(str):Task(str): the job to be done and the the key values in the dictionary
        """
        self.to_do = []
        self.in_progress = []
        self.done = []
        self.board = {"to do": self.to_do, "in progress": self.in_progress, "done": self.done}
        
    def read_csv(self, filename):
        """reads tasks from a file, parses them  and adds them to kanban board
        Args:
          filename(str): name of file with tasks
        """
        with open(filename,"r",encoding="utf-8") as f:
            #= get_words(f.read())
            #self.tf[filename] = Counter(words)
            #self.df.update(set(words))
    #FIX THIS
        
    def add_work_item(self):
        """This method will be for implementing the work items that will be r
        equired by a boss
        Args:
            task(str):Task(str): the job to be done and the the key values in 
            the dictionary
        """
        #ADD TASKS TO LIST
        

    def colm_movements(self,id, move_to):
        """This method will move tasks from one comlumn to the other
        Args:
        Side Effects:
        """
        

    def clear_board(self):
        """This method will allow the users to completely clear the board when 
        they want to start a new project"""

    def display_board(self):
        """Display the board in a dictionary with the key values “Backlog”, 
        “To-do”, “ “In Progress”, and “Done””
        Returns: 
            Dictionary: keys will be backlog, to-do, in-progress, and done. The 
            tasks are the values in the dictionary where they are on the board.
        """
        
def main():
    
#method read in the board from a file
#method write the board out to a file

#Define task class. Each class can have an idea, decription, date. Can have methods to edit description
#Talk with group about user interface, prompt, 