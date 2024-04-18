from governator import Database, Group, Permission, Project, Role, Schema, User

database1 = Database(key="mydb")

finance_group = Group(
    group="finance",
    users=[
        User("finance_user_1"),
        User("finance_user_2"),
    ],
)
engineer_group = Group(
    group="engineering",
    users=[
        User("eng_user_1"),
        User("eng_user_2"),
        User("eng_user_3"),
    ],
)

finance_database_schema = Schema("finance_schema")

finance_role = Role(
    role="finance_role",
    permissions=[
        Permission(
            schemas=[finance_database_schema],
            privileges=["SELECT", "INSERT", "UPDATE", "DELETE"],
        )
    ],
    groups=[finance_group],
)

project = Project(databases=[database1])
