import builtins
import pytest
from cli import main

def test_cli_add_and_exit(monkeypatch, capsys):
    # Simulate user typing "add Task 1", then "exit"
    inputs = iter(["add Task 1", "exit"])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()

    output = capsys.readouterr().out

    assert "Added: Task 1" in output
    assert "Bye!" in output


def test_cli_list(monkeypatch, capsys):
    inputs = iter(["add Read book", "list", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    output = capsys.readouterr().out

    assert "Read book" in output
    assert "[❌]" in output or "[✘]" in output  # Not done yet


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


def test_cli_unknown_command(monkeypatch, capsys):
    inputs = iter(["blablabla", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Unknown command" in output


def test_cli_done_invalid_id(monkeypatch, capsys):
    inputs = iter(["done 999", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Task not found" in output


def test_cli_done_no_id(monkeypatch, capsys):
    inputs = iter(["done", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: done <id>" in output


def test_cli_delete_no_id(monkeypatch, capsys):
    inputs = iter(["delete", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: delete <id>" in output


def test_cli_delete_invalid_id(monkeypatch, capsys):
    inputs = iter(["delete 999", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Task not found" in output


def test_cli_delete_non_number(monkeypatch, capsys):
    inputs = iter(["delete abc", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: delete <id>" in output


def test_cli_add_no_title(monkeypatch, capsys):
    inputs = iter(["add", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: add <title>" in output


def test_cli_add_blank_title(monkeypatch, capsys):
    inputs = iter(["add    ", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Usage: add <title>" in output


