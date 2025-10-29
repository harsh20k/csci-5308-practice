from sqlite3 import Date as date


# class Taskk



class Taskk:
    assignedTo = "harsh"
    status = "new"
    deadline = date.today()

    def __init__(self,assignedTo,status,deadline):
        self.assignedTo = assignedTo
        self.status = status
        self.deadline = deadline

    def assignTo(self,team_member):
        self.assignedTo = team_member
        return self.assignedTo

    def updateStatus(self,status):
        self.status = status
        return self.status

    def isOverdue(self):
        if self.deadline > date.today():
            return True
        else:
            return False

