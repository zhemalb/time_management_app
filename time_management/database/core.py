from .database import sql_execute
from .models import User, Tag, Status, Project, Task


def add_new_user(user: User):
    sql_execute(f"""
        INSERT INTO users(username, email, password)
        VALUES (%s, %s, %s)
    """, [user.get_name(), user.get_email(), user.get_password()])


def add_new_tag(tag: Tag):
    sql_execute(f"""
        INSERT INTO tags(tag_name, tag_desc, tag_color, fk_user_id)
        VALUES (%s, %s, %s, %s) 
    """, [tag.get_name(), tag.get_desc(), tag.get_color(), tag.get_user().id])


def add_new_status(status: Status):
    sql_execute(f"""
        INSERT INTO statuses(status_name, status_urgency, status_color, fk_user_id)
        VALUES (%s, %s, %s, %s) 
    """, [status.get_name(), status.get_urgency(), status.get_color(), status.get_user().id])


def add_new_project(project: Project):
    sql_execute(f"""
        INSERT INTO projects(project_name, project_desc, project_color, fk_user_id) 
        VALUES (%s, %s, %s, %s)
    """, [project.get_name(), project.get_desc(), project.get_color(), project.get_user().id()])


def link_tags_with_task(tags: list[Tag], task_id: int):
    for tag in tags:
        sql_execute(f"""
            INSERT INTO tags_ans_tasks(task_id, tag_id)
            VALUES (%s, %s)
        """, [tag.get_id(), task_id])


def get_last_task():
    return sql_execute(f"""
        SELECT t.task_id
        FROM tasks t
        WHERE t.task_id = (
            SELECT max(t1.task_id)
            FROM tasks t1
        )
    """, [], "get")


def add_new_task(task: Task):
    sql_execute(f"""
        INSERT INTO tasks(task_name, task_description, task_color, task_deadline, task_project, task_status, fk_user_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) 
    """, [task.get_name, task.get_desc(), task.get_color(), task.get_deadline(), task.get_project().get_id(),
          task.get_status().get_id(), task.get_user().id])

    link_tags_with_task(task.get_tags(), get_last_task())


def get_user_with_email(email: str):
    return sql_execute(f"""
        SELECT u.id
            FROM users u
        WHERE u.email = %s
    """, [email], "get")


def get_user_by_id(user_id: int) -> User:
    result = sql_execute(f"""
        SELECT u.id, u.username, u.email, u.password
            FROM users u
        WHERE u.id = %s
    """, [user_id], "get")

    to_return = User()
    to_return.id_ = result[0]
    to_return.username_ = result[1]
    to_return.email_ = result[2]
    to_return.password_ = result[3]

    return to_return


def get_project_by_id(project_id: int) -> Project:
    result = sql_execute(f"""
        SELECT project_id, project_name, project_desc, project_color, fk_user_id
        FROM projects p
        WHERE p.project_id = %s
    """, [project_id], "get")

    return Project(result[1], get_user_by_id(result[-1]), result[0], result[2], result[3])


def get_status_by_id(status_id: int) -> Status:
    result = sql_execute(f"""
        SELECT s.status_id, s.status_name, s.status_urgency, s.status_color, fk_user_id
        FROM statuses s 
        WHERE s.status_id = %s
    """, [status_id], "get")

    return Status(result[1], get_user_by_id(result[-1]), result[2], result[0], result[3])


def get_tag_by_id(tag_id: int) -> Tag:
    result = sql_execute(f"""
        SELECT t.tag_id, t.tag_name, t.tag_desc, t.tag_color, fk_user_id 
            FROM tags t
        WHERE t.tag_id = %s
    """, [tag_id], "get")

    return Tag(result[1], result[2], get_user_by_id(result[-1]), result[0], result[3])


def get_all_tags_of_task(task_id: int) -> list[Tag]:
    result = sql_execute(f"""
        SELECT tat.tag_id
            FROM tags_ans_tasks tat
        WHERE tat.task_id = %s
    """, [task_id], "get all")

    data = list()
    for current in result:
        tag_id = current[0]
        data.append(get_tag_by_id(tag_id))

    return data


def get_all_tasks_by_user(user: User) -> list[Task]:
    result = sql_execute(f"""
        SELECT task_id, task_name, task_description, task_color, task_deadline, task_project, task_status
            FROM tasks t
        LEFT JOIN users u
            ON u.id = t.fk_user_id
        WHERE u.email = %s
    """, [user.email()], "get all")

    if len(result) == 0:
        return []

    data = []
    for task in result:
        data.append(Task(task[1], get_all_tags_of_task(task[0]), user, task[3], task[0], task[2],
                         get_project_by_id(task[-2]), get_status_by_id(task[-1]), result[-3]))

    return data
