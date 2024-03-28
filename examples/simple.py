from governator import Database, Project, utils

database1 = Database(key="mydb")

project = Project(databases=[database1])
