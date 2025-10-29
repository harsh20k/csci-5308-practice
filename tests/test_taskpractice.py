import sys, os
from datetime import timedelta

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sqlite3 import Date as date

import pytest

from Taskpractice import Taskk

#Requirements

#Use TDD approach with 100% code coverage to develop the following requirements.

#You need to implement a Task abstraction implementing a set of functionalities.
# Specifically, create a Task class with at least following methods:

#assignTo(team_member): Assign a task to a specific team member
#updateStatus(new_status): Change task status with validation
#isOverdue(): Determine if task is past its estimated completion time
#You may create additional classes/abstractions to fulfill the above requirements.
#Make reasonable assumptions if any information seem missing.


Taskka = Taskk("rajeev","ongoing",date.today() - timedelta(days=2))

def test_task_assignment():
    assert type(Taskka.assignTo("harsh")) == str

def test_task_assignment_function():
    Taskka.assignTo("pandey")
    assert Taskka.assignTo("pandey") == "pandey"

def test_update_status():
    assert Taskka.updateStatus("pending") == "pending"

@pytest.mark.parametrize(
                            "string,expected",
                            [
                                ("pending", "pending"),
                                ("removed", "removed"),
                                ("delayed", "delayed"),
                            ],
                        )
def test_update_status(string,expected):
    assert Taskka.updateStatus(string) == expected

def test_is_overdue():
    assert Taskka.isOverdue() is False

def test_is_overdue_false():
    task = Taskk("rajeev","ongoing",date.today() + timedelta(days=2))
    assert task.isOverdue() is True

def test_is_overdue_true():
    task = Taskk("rajeev","ongoing",date.today() - timedelta(days=2))
    assert task.isOverdue() is False



