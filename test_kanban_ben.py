from KANBAN10_12 import Kanban, Task 
import pytest

#def colm_movements(self, task_id, move_to): 


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