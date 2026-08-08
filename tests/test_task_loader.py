from harness.task_loader import discover_tasks, load_task


def test_discover_tasks_finds_all_task () :
    tasks = discover_tasks()
    assert "fibonacci" in tasks
    assert "is_palindrome" in tasks
    assert "two_sum" in tasks


def test_load_task_returns_working_module():
    task = load_task("fibonacci")
    assert task.solve(10) == 55