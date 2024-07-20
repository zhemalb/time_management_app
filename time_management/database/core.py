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
    """, [project.get_name(), project.get_desc(), project.get_color(), project.get_user().id])


def link_tags_with_task(tags: list[Tag], task_id: int):
    for tag in tags:
        sql_execute(f"""
            INSERT INTO tags_ans_tasks(task_id, tag_id)
            VALUES (%s, %s)
        """, [tag.id, task_id])


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
    """, [task.get_name, task.get_desc(), task.get_color(), task.get_deadline(), task.get_project().id,
          task.get_status().id, task.get_user().id])

    link_tags_with_task(task.get_tags(), get_last_task())


def get_user_with_email(email: str):
    return sql_execute(f"""
        SELECT u.id
            FROM users u
        WHERE u.email = %s
    """, [email], "get")
