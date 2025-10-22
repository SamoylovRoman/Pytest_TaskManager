import builtins
import pytest
from cli import main
import allure

@allure.title("Add a task and exit the CLI")
@allure.feature("CLI Commands")
@allure.story("Add Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_add_and_exit(monkeypatch, capsys):
    # Simulate user typing "add Task 1", then "exit"
    inputs = iter(["add Task 1", "exit"])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()

    output = capsys.readouterr().out

    assert "Added: Task 1" in output
    assert "Bye!" in output

@allure.title("List tasks shows added task with not-done status")
@allure.feature("CLI Commands")
@allure.story("List Tasks")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Roman Samoilov")
def test_cli_list(monkeypatch, capsys):
    inputs = iter(["add Read book", "list", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    output = capsys.readouterr().out

    assert "Read book" in output
    assert "[❌]" in output or "[✘]" in output  # Not done yet


@allure.title("Mark a task as done")
@allure.feature("CLI Commands")
@allure.story("Mark Task Done")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Roman Samoilov")
def test_cli_mark_done(monkeypatch, capsys):
    inputs = iter([
        "add Task to complete",
        "done 1",
        "list",
        "exit"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out
    print(output)

    assert "Marked as done" in output
    assert "✔️" in output  # Task now marked complete


@allure.title("Handle unknown CLI command gracefully")
@allure.feature("CLI Commands")
@allure.story("Invalid Input")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_unknown_command(monkeypatch, capsys):
    inputs = iter(["blablabla", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Unknown command" in output

@allure.title("Mark non-existent task as done returns 'Task not found'")
@allure.feature("CLI Commands")
@allure.story("Mark Task as Done")
@allure.severity(allure.severity_level.MINOR)
def test_cli_done_invalid_id(monkeypatch, capsys):
    inputs = iter(["done 999", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Task not found" in output


@allure.title("Missing ID in 'done' command shows usage message")
@allure.feature("CLI Commands")
@allure.story("Mark Task as Done")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_done_no_id(monkeypatch, capsys):
    inputs = iter(["done", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: done <id>" in output


@allure.title("Missing ID in 'delete' command shows usage message")
@allure.feature("CLI Commands")
@allure.story("Delete Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_delete_no_id(monkeypatch, capsys):
    inputs = iter(["delete", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: delete <id>" in output


@allure.title("Deleting a non-existent task shows 'Task not found'")
@allure.feature("CLI Commands")
@allure.story("Delete Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_delete_invalid_id(monkeypatch, capsys):
    inputs = iter(["delete 999", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Task not found" in output


@allure.title("Non-numeric ID in 'delete' command shows usage message")
@allure.feature("CLI Commands")
@allure.story("Delete Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_delete_non_number(monkeypatch, capsys):
    inputs = iter(["delete abc", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: delete <id>" in output


@allure.title("Calling 'add' without a title shows usage message")
@allure.feature("CLI Commands")
@allure.story("Add Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_add_no_title(monkeypatch, capsys):
    inputs = iter(["add", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: add <title>" in output


@allure.title("Adding a blank title shows usage message")
@allure.feature("CLI Commands")
@allure.story("Add Task")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Roman Samoilov")
def test_cli_add_blank_title(monkeypatch, capsys):
    inputs = iter(["add    ", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: add <title>" in output


