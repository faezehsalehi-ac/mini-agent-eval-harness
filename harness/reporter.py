import json
import csv
class JSONReporter:

    def save(self, results: list[dict],path: str) -> None:
        with open (path, "w") as f:
                   json.dump(results, f, indent=2)

class CSVReporter:

      def save(self, results: list[dict], path: str) -> None:
            with open (path, "w", newline="") as f:
                  writer = csv.writer(f)
                  writer.writerow(["task_name", "total", "passed"])
                  for r in results:
                        writer.writerow([r["task_name"], r["total"], r["passed"]])


def create_reporter(format_name: str):
    reporters = {
        "json": JSONReporter,
        "csv": CSVReporter,
    }
    if format_name not in reporters:
        raise ValueError (f"Unknown report format: {format_name}")
    return reporters[format_name]() 