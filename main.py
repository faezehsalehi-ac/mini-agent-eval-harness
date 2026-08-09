from harness.task_loader import discover_tasks, load_task
from harness.evaluator import Evaluator
from harness.reporter import create_reporter

def run():
    evaluator = Evaluator()
    all_results = []

    for task_name in discover_tasks():
        task_module = load_task (task_name)
        result = evaluator.evaluate(task_module)
        all_results.append(result)
        status = "PASS" if result["passed"] == result["total"] else "FAIL"
        print (f"[{status}] {result['task_name']} : {result['passed']}/{result['total']}")





    total_cases = sum(r["total"] for r in all_results)
    total_passed = sum(r["passed"] for r in all_results)
    success_rate = (total_passed / total_cases *100) if total_cases > 0 else 0

    print(f"\nOverall success rate: {success_rate:.1f}% ({total_passed}/{total_cases})")

    reporter = create_reporter("json")
    reporter.save(all_results, "reports/final_report.json")
    print("\nReport saved to reports/final_report.json")


if __name__ == "__main__" :
    run()


