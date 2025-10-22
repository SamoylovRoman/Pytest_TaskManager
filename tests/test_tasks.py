from app.task_service import add_task, list_tasks, mark_task_done, delete_task


def test_add_task(test_db):
    # Add a task
    task = add_task(test_db, "Write pytest tests")

    # Assert task properties
    assert task.id == 1  # First task should have ID 1
    assert task.title == "Write pytest tests"
    assert task.done is False


def test_list_tasks(test_db):
    # Initially, task list should be empty
    tasks = list_tasks(test_db)
    assert tasks == []

    # Add some tasks
    add_task(test_db, "Task A")
    add_task(test_db, "Task B")

    # Now list should return both tasks
    tasks = list_tasks(test_db)
    assert len(tasks) == 2
    assert tasks[0].title == "Task A"
    assert tasks[1].title == "Task B"
    assert tasks[0].done is False
    assert tasks[1].done is False


def test_mark_task_done_success(test_db):
    # Add a task
    task = add_task(test_db, "Finish this test")

    # Mark it as done
    success = mark_task_done(test_db, task.id)

    # Check that the function returned True
    assert success is True

    # Fetch the updated task
    updated_tasks = list_tasks(test_db)
    assert updated_tasks[0].done is True

def test_mark_task_done_invalid_id(test_db):
    # Try to mark a non-existent task
    success = mark_task_done(test_db, task_id=999)
    assert success is False


def test_delete_task_success(test_db):
    # Add a task
    task = add_task(test_db, "Task to be deleted")

    # Delete the task
    success = delete_task(test_db, task.id)
    assert success is True

    # Verify task is gone
    tasks = list_tasks(test_db)
    assert len(tasks) == 0

def test_delete_task_invalid_id(test_db):
    # Try to delete a task that doesn't exist
    success = delete_task(test_db, 999)
    assert success is False


