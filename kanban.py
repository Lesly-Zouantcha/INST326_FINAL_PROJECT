# Lesly Zouantcha, Evan English, Joey Epstein, Ben Lam
              
import csv
                         
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
                                  
    def __str__(self):
        """This returns the task 
        Returns:
           Returns task as string
        """
        return f"{self.task}"
    
class Kanban:
    
    """ Takes in the users tasks and moves them through columns
    (to do, in progress, and done) depending at what stage they are in working
    on it. 
    Attributes:
       filename(str): path to csv file containing tasks
       id(int): id of task
       move_to(str): the column the user wants to move the task to 
    """
    def __init__(self):
        
        """This will iniliatize a list for the 3 columns in the kanban 
        Args:
        to_do(list): list of to do tasks
        in_progress(list): list of in progress tasks
        done(list): list of done tasks
        """
        self.to_do = []
        self.in_progress = []
        self.done = []
        
    def read_csv(self, filename):
        """reads tasks from a file, parses them  and adds them to kanban board
        Args:
          filename(str): name of file with tasks
        Side Effects:
          Adds the task from a file into a list calls tasks
          Returns the list
        """
        with open(filename,"r",encoding="utf-8") as f:
            for line in f:
                elements = line.split(",").strip('')
                task_id = elements[0]
                description = elments[1]
                due_date = elemenst[2] 
        return tasks.append(Task(self, task_id, description, due_date))
                      
        
    def add_work_item(self):
        """This method will be for implementing the work items that will be r
        equired by a boss in the to do column
        Side Effects:
           Adds content from the list of tasks into the to do column
           Returns the list
        """
        for i in tasks:
           self.to_do.append(i)
        return self.to_do

    def colm_movements(self,task_id, move_to):
        """This method will move tasks from one comlumn to the other
        Args:
          task_id(int): id of task
          move_to(str): column the user wants to move the task to
        Side Effects:
          Deletes tasks from a list
          Adds tasks to a list
        """
        if move_to.lower() == "in progress":
            self.in_progress.append(self.task[task_id])
            self.to_do.remove(self.task[task_id])
            
        if move_to.lower() == "done":
            self.done.append(self.task[task_id])
            self.in_progress.remove(self.task[task_id])
            

    def clear_board(self):
        """This method will allow the users to completely clear the board when 
        they want to start a new project
        Side Effects:
            Deletes every task in every column of the kanban board
        """
        
        for i in self.to_do:
            del i
        for i in self.in_progress:
            del i
        for i in self.done:
            del i

    def display_board(self):
        """Display the board in a dictionary with the key values “Backlog”, 
        “To-do”, “ “In Progress”, and “Done””
        Side Effects: 
            Print out Dictionary: keys will be backlog, to-do, in-progress, and done. The 
            tasks are the values in the dictionary where they are on the board.
        """
        board = {"to do": self.to_do, "in progress": self.in_progress, "done": self.done}
        
        print(board)
        
    def write_csv(self):
        """Displays the final board to a csv file
        Side Effects:
           Changes the value in the csv file 
        """
        with open('kanban_board.cvs', mode = 'w') as kanban_csv: 
            fields = ['to do', 'in progress',"done"]
            writer = csv.DictWriter(kanban_csv, fieldnames = fields) 
            writer.writeheader()
            writer.writerows(board)
                
     #Ask professor how to loop through each task and make their own row
                     
# USER INTERFACE
def main():
    """
    """
    print("Welcome to the kanban board! Lets begin!")

    task_input = str(input("Do you have a task to add to your board? Yes or No. (If you want to add a task using a csv enter 'csv') ")).lower

    if task_input == 'csv':
        user_filname = str(input("Enter the csv filename "))
        Kanban.read_csv(user_filename)
        
    tasks = []
    while task_input != 'no':
        user_task_id = int(input("Enter the task id "))
        user_description = str(input("Enter the task description "))
        user_due_date = str(input("Enter the task due date "))
        tasks.append(Task(user_task_id, user_description, user_due_date))
        print(tasks)
        task_input = str(input("Do you have another task to add to your board? Yes or No ")).lower
            
    user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, display board to csv, clear board, done ")).lower()

    while user_input != 'done':
        if user_input == "edit task":
            edit_task_id = int(input("Enter the task id you want to edit "))
            edit_description = str(input("Enter your edited description "))
            edit_due_date = str(input("Enter your edited due date "))
            Task.edit_task(edit_task_id, edit_description, edit_due_date)
            user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "move task":
            move_task_id = int(input("Enter the task id you want to move "))
            edit_movement = str(input("Enter the column you want to move the task to "))
            Kanban.colm_movements(move_task_id, edit_movement)
            user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "display board":
            Kanban.display_board()
            user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "display board to csv":
            Kanban.write_csv()
            user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "clear board":
            Kanban.clear_board()   
            user_input = str(input("What would you like to do next with your board? Options: edit task, move task, display board, clear board, done ")).lower()
  
if __name__ == '__main__':
    main()
    
#Need to create a main functionn so that our user interface works
#Need to fix the user interfce #Add write csv as one of the options #Add use input for other parameters
#Need to finish the write csv dictionary
    
