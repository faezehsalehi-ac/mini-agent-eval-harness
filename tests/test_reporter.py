import json
import csv
from harness.reporter import create_reporter


SAMPLE_RESULTS = [
    {
        "task_name": "fake_task", "total":2, "passed": 2
    },
]

def test_json_reporter_creates_valid_file(tmp_path):
    output_file = tmp_path / "reporter.json"
    reporter = create_reporter("json")
    reporter.save(SAMPLE_RESULTS, str(output_file))



    assert output_file.exists()
    with open(output_file) as f :
        data = json.load(f)
    assert data == SAMPLE_RESULTS

def test_csv_reporter_creates_valid_file(tmp_path):
    output_file = tmp_path / "reporter.csv"
    reporter = create_reporter("csv")
    reporter.save(SAMPLE_RESULTS, str(output_file))



    assert output_file.exists()
    with open(output_file) as f :
        rows = list(csv.reader(f))
    assert rows[0] == ["task_name", "total", "passed"]
    assert rows[1] == ["fake_task", "2", "2"]


def test_create_reporter_raises_on_unknown_format():
    try:
        create_reporter ("xml")
        assert False, "Expected ValueError for unknown format"
    except ValueError:
        pass


