import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import Taskk

#Requirements

#Use TDD approach with 100% code coverage to develop the following requirements.

#You need to implement a Task abstraction implementing a set of functionalities.
# Specifically, create a Task class with at least following methods:

#assignTo(team_member): Assign a task to a specific team member
#updateStatus(new_status): Change task status with validation
#isOverdue(): Determine if task is past its estimated completion time
#You may create additional classes/abstractions to fulfill the above requirements.
#Make reasonable assumptions if any information seem missing.


Taskka = Taskk()

def test_task_assignment():
    assert type(Taskka.assignTo("harsh")) == str

def test_task_assignment_function():
    Taskka.assignTo("pandey")
    assert Taskka.assignTo("pandey") == "pandey"

def test_update_status():
    assert Taskka.updateStatus("pending") == "pending"

