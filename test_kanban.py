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
    to_do = [Task(1, 'eat', "1/2")]
    kanban = Kanban()
    kanban.to_do = to_do

    kanban.colm_movements(1, 'done')
    assert len(kanban.to_do) == 0  
    assert len(kanban.done) == 1
    
def test_colm_movements_inprogress_done():
    in_progress = [Task(2, 'shower', "1/3")]
    kanban = Kanban()
    kanban.in_progress = in_progress

    kanban.colm_movements(2, 'done')
    assert len(kanban.in_progress) == 0  
    assert len(kanban.done) == 1
    
def test_colm_movements_done_todo():
    done = [Task(3, 'docstrings', "1/4")]
    kanban = Kanban()
    kanban.done = done

    kanban.colm_movements(3, 'to do')
    assert len(kanban.done) == 0  
    assert len(kanban.to_do) == 1    
    
def test_colm_movements_done_inprogress():
    done = [Task(4, 'run', "1/5")]
    kanban = Kanban()
    kanban.done = done

    kanban.colm_movements(4, 'in progress')
    assert len(kanban.done) == 0  
    assert len(kanban.in_progress) == 1   
    
def test_colm_movements_todo_inprogress():
    to_do = [Task(5, 'homework', "1/6")]
    kanban = Kanban()
    kanban.to_do = to_do

    kanban.colm_movements(5, 'in progress')
    assert len(kanban.to_do) == 0  
    assert len(kanban.in_progress) == 1  
    
def test_colm_movements_inprogress_todo():
    in_progress = [Task(6, 'code', "1/7")]
    kanban = Kanban()
    kanban.in_progress = in_progress

    kanban.colm_movements(6, 'to do')
    assert len(kanban.in_progress) == 0  
    assert len(kanban.to_do) == 1   
