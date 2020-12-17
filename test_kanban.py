# Lesly Zouantcha, Evan English, Joey Epstein, Ben Lam

from kanban import Task, Kanban
import pytest

#test Task init method
def test_Task_init():
    """ Test the __init__() method of the Task class. """
    t1 = Task(1, "Write Test Script", "12/12")
    assert t1.task_id == 1
    assert t1.description == "Write Test Script"
    assert t1.due_date == "12/12"
    assert t1.task == {1 : ["Write Test Script", "12/12"]}
    
    t2 = Task(2, "Create Docstrings", "12/13")
    assert t2.task_id == 2
    assert t2.description == "Create Docstrings"
    assert t2.due_date == "12/13"
    assert t2.task == {2: ["Create Docstrings", "12/13"]}
    
    t3 = Task(3, "Fix Errors", "12/14")
    assert t3.task_id == 3
    assert t3.description == "Fix Errors"
    assert t3.due_date == "12/14"
    assert t3.task == {3: ["Fix Errors", "12/14"]}
    
    t4 = Task(4, "Write Report", "12/15")
    assert t4.task_id == 4
    assert t4.description == "Write Report"
    assert t4.due_date == "12/15"
    assert t4.task == {4 : ["Write Report", "12/15"]}

#test Kanban colm movement method
def test_colm_movements_todo_done():
    """ Test the clom_movements() method of the Kanban class. """
    to_do = [Task(1, 'eat', "1/2")]
    kanban = Kanban()
    kanban.to_do = to_do

    kanban.colm_movements(1, 'done')
    assert len(kanban.to_do) == 0  
    assert len(kanban.done) == 1
    
def test_colm_movements_inprogress_done():
    """ Test the clom_movements() method of the Kanban class. """
    in_progress = [Task(2, 'shower', "1/3")]
    kanban = Kanban()
    kanban.in_progress = in_progress

    kanban.colm_movements(2, 'done')
    assert len(kanban.in_progress) == 0  
    assert len(kanban.done) == 1
    
def test_colm_movements_done_todo():
    """ Test the clom_movements() method of the Kanban class. """
    done = [Task(3, 'docstrings', "1/4")]
    kanban = Kanban()
    kanban.done = done

    kanban.colm_movements(3, 'to do')
    assert len(kanban.done) == 0  
    assert len(kanban.to_do) == 1    
    
def test_colm_movements_done_inprogress():
    """ Test the clom_movements() method of the Kanban class. """
    done = [Task(4, 'run', "1/5")]
    kanban = Kanban()
    kanban.done = done

    kanban.colm_movements(4, 'in progress')
    assert len(kanban.done) == 0  
    assert len(kanban.in_progress) == 1   
    
def test_colm_movements_todo_inprogress():
    """ Test the clom_movements() method of the Kanban class. """
    to_do = [Task(5, 'homework', "1/6")]
    kanban = Kanban()
    kanban.to_do = to_do

    kanban.colm_movements(5, 'in progress')
    assert len(kanban.to_do) == 0  
    assert len(kanban.in_progress) == 1  
    
def test_colm_movements_inprogress_todo():
    """ Test the clom_movements() method of the Kanban class. """
    in_progress = [Task(6, 'code', "1/7")]
    kanban = Kanban()
    kanban.in_progress = in_progress

    kanban.colm_movements(6, 'to do')
    assert len(kanban.in_progress) == 0  
    assert len(kanban.to_do) == 1   
    
#test Task edit_task method
def test_edit_task():
    """ Test the edit_task() method of the Task class. """
    task1 = Task(1, "Write Test Script", "12/12")
    edit1 = task1.edit_task(1, "Write a new test script","12/20/2020" )
    assert edit1[1] == ["Write a new test script","12/20/2020"]

    task2 = Task(2, "Call my mom on her birthday", "1/1/2021")
    edit2 = task2.edit_task(2,"Call my mom on her birthday to tell her I am coming home!", "1/22/2021" )
    assert edit2[2] == ["Call my mom on her birthday to tell her I am coming home!", "1/22/2021"]

    task3 = Task(3, "Go to Doctors Appointment", "5/22/2021")
    edit3 = task3.edit_task(3,"Go to new Doctors appointment", "6/1/2021")
    assert edit3[3] == ["Go to new Doctors appointment", "6/1/2021"]

    task4 = Task(4, "Register for classes", "12/12/2021")
    edit4 = task4.edit_task(4, "Register for General Education (GenEd) classes","12/12/2021")
    assert edit4[4] == ["Register for General Education (GenEd) classes","12/12/2021"]


#test Kanban clear board method
def test_clear_board():
    """ Test the clear_board() method of the Kanban class. """
    kanBan = Kanban()
    kanBan.clear_board()
    assert len(kanBan.to_do) == 0  
    assert len(kanBan.in_progress) == 0  
    assert len(kanBan.done) == 0  