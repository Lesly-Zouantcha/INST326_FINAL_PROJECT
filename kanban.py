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
        
    def edit_task(self, task_id, new_description, new_due_date):  
        """Edits a specific task
        Args:
            task_id(int): id of task 
        new_description(str): the new descripton of the task the user wants to edit
        new_due_date(str): the new due_date of the task the user wans to edit
        Side Effects:
            Changes the input statement 
        """
        self.description = new_description
        self.due_date = new_due_date
        self.task[task_id] = [self.description, self.due_date]
        print(self.task)
        return self.task  
                                  
    def __str__(self):
        """This returns the task 
        Returns:
           Returns task as string
        """
        return f"{self.task}"
    
    def __repr__(self):
        return str(self)
    
class Kanban():
    
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
        
    def read_file(self, file_path):
        """reads tasks from a file, parses them  and adds them to kanban board
        Args:
          filename(str): name of file with tasks
        Side Effects:
          Adds the task from a file into a list calls tasks
          Returns the list
        """
        with open(file_path,"r",encoding="utf-8") as f:
            for line in f:
                elements = line.strip('\n').split(",")
                task_id = elements[0]
                description = elements[1]
                due_date = elements[2]             
                column=elements[3]


                if column== "to do":
                    self.to_do.append(Task(task_id, description, due_date))
                if column== "in progress":
                    self.in_progress.append(Task(task_id, description, due_date))
                if column== "done":
                    self.done.append(Task(task_id, description, due_date))
                      
        
    def add_work_item(self, task_list):
        """This method will be for implementing the work items that will be r
        equired by a boss in the to do column
        Side Effects:
           Adds content from the list of tasks into the to do column
           Returns the list
        """
        for i in task_list:
           self.to_do.append(i)
        return self.to_do

    def colm_movements(self, task_id, move_to):    
        """This method will move tasks from one comlumn to the other
        Args:
          task_id(int): id of task
          move_to(str): column the user wants to move the task to
        Side Effects:
          Deletes tasks from a list
          Adds tasks to a list
        """
        found_task = None  
        
     
        for task in self.to_do:
            if task.task_id == task_id:
                found_task = task
                self.to_do.remove(found_task)
        
        if found_task == None: 
            for task in self.in_progress:
                if task.task_id == task_id:
                    found_task = task
                    self.in_progress.remove(found_task)
        
        if found_task == None: 
            for task in self.done:
                if task.task_id == task_id:
                    found_task = task
                    self.done.remove(found_task) 

                   
        if found_task != None:
        
            if move_to.lower() == "to do":
                self.to_do.append(found_task)
        
            if move_to.lower() == "in progress":
                self.in_progress.append(found_task)
            
            if move_to.lower() == "done":
                self.done.append(found_task)       

            

    def clear_board(self):
        """This method will allow the users to completely clear the board when 
        they want to start a new project
        Side Effects:
            Deletes every task in every column of the kanban board
        """
        
        for i in self.to_do:
            self.to_do.remove(i)
            return self.to_do
        for i in self.in_progress:
            self.in_progress.remove(i)
            return self.in_progress
        for i in self.done:
            self.done.remove(i)
            return self.done
            

    def display_board(self):
        """Display the board in a dictionary with the key values “Backlog”, 
        “To-do”, “ “In Progress”, and “Done””
        Side Effects: 
            Print out Dictionary: keys will be backlog, to-do, in-progress, and done. The 
            tasks are the values in the dictionary where they are on the board.
        """
        col1 = {"to do": self.to_do}
        col2={"in progress": self.in_progress} 
        col3={"done": self.done}
        
        print(f"\n{col1}\n\n{col2}\n\n{col3}\n")
                     
# USER INTERFACE
def main():
    """
    """
    kanban = Kanban()
    print("Welcome to the kanban board! Lets begin!")

    task_input = str(input("Do you have a task to add to your board? Yes or No. "
                           "(If you want to add a task using a file enter 'file') ")).lower()
    
    if task_input == 'file':
        user_filename = str(input("Enter the file filename "))
        kanban.read_file(user_filename)
         
    tasks = []
    while task_input not in ["no", "file"]:
        user_task_id = str(input("Enter the task id "))
        user_description = str(input("Enter the task description "))
        user_due_date = str(input("Enter the task due date "))
        tasks.append(Task(user_task_id, user_description, user_due_date))
        print(f"Tasks: {tasks}")
        task_input = str(input("Do you have another task to add to your board? Yes or No ")).lower()
    
    kanban.add_work_item(tasks)  
         
    user_input = str(input("What would you like to do next with your board? " 
                           "Options: edit task, move task, display board, "
                            "clear board, done ")).lower()

    while user_input != 'done':
        if user_input == "edit task":
            edit_task_id = str(input("Enter the task id you want to edit "))
            edit_description = str(input("Enter your edited description "))
            edit_due_date = str(input("Enter your edited due date "))
            for i in kanban.to_do:
                if i.task_id == edit_task_id:
                    i.edit_task(edit_task_id, edit_description, edit_due_date)
            for i in kanban.in_progress:
                if i.task_id == edit_task_id:
                    i.edit_task(edit_task_id, edit_description, edit_due_date)
            for i in kanban.done:
                if i.task_id == edit_task_id:
                    i.edit_task(edit_task_id, edit_description, edit_due_date)
            user_input = str(input("What would you like to do next with your board? "
                                   "Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "move task":
            move_task_id = str(input("Enter the task id you want to move "))
            edit_movement = str(input("Enter the column you want to move the task to "))
            kanban.colm_movements(move_task_id, edit_movement)
            user_input = str(input("What would you like to do next with your board? "
                                    "Options: edit task, move task, display board, clear board, done ")).lower()
            
        elif user_input == "display board":
            kanban.display_board()
            user_input = str(input("What would you like to do next with your board? " 
                                "Options: edit task, move task, display board, clear board, done ")).lower()
            
            
        elif user_input == "clear board":
            kanban.clear_board()   
            user_input = str(input("What would you like to do next with your board? Options: "
                 "edit task, move task, display board, clear board, done ")).lower()
  
if __name__ == '__main__':
    main()
    
    
    


    
