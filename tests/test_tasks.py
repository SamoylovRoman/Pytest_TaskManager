from app.task_service import add_task, list_tasks, mark_task_done, delete_task


import allure

@allure.title("Add a task to the database")
@allure.feature("Database Operations")
@allure.story("Add Task")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Roman Samoilov")
def test_add_task(test_db):
    task = add_task(test_db, "Write pytest tests")
    assert task.id == 1
    assert task.title == "Write pytest tests"
    assert task.done is False


@allure.title("List tasks returns correct items after adding")
@allure.feature("Database Operations")
@allure.story("List Tasks")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Roman Samoilov")
def test_list_tasks(test_db):
    tasks = list_tasks(test_db)
    assert tasks == []

    add_task(test_db, "Task A")
    add_task(test_db, "Task B")

    tasks = list_tasks(test_db)
    assert len(tasks) == 2
    assert tasks[0].title == "Task A"
    assert tasks[1].title == "Task B"
    assert not tasks[0].done
    assert not tasks[1].done


@allure.title("Marking an existing task as done succeeds")
@allure.feature("Database Operations")
@allure.story("Mark Task as Done")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Roman Samoilov")
def test_mark_task_done_success(test_db):
    task = add_task(test_db, "Finish this test")
    success = mark_task_done(test_db, task.id)
    assert success is True

    updated_tasks = list_tasks(test_db)
    assert updated_tasks[0].done is True


@allure.title("Marking a non-existent task as done returns False")
@allure.feature("Database Operations")
@allure.story("Mark Task as Done")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Roman Samoilov")
def test_mark_task_done_invalid_id(test_db):
    success = mark_task_done(test_db, task_id=999)
    assert success is False


@allure.title("Deleting an existing task succeeds")
@allure.feature("Database Operations")
@allure.story("Delete Task")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Roman Samoilov")
def test_delete_task_success(test_db):
    task = add_task(test_db, "Task to be deleted")
    success = delete_task(test_db, task.id)
    assert success is True

    tasks = list_tasks(test_db)
    assert len(tasks) == 0


@allure.title("Deleting a non-existent task returns False")
@allure.feature("Database Operations")
@allure.story("Delete Task")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Roman Samoilov")
def test_delete_task_invalid_id(test_db):
    success = delete_task(test_db, 999)
    assert success is False



