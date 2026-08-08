from harness.strategies import ExactMatchStrategy

class Evaluator:

    def __init__(self, strategy=None):
        self.strategy = strategy or ExactMatchStrategy()

    def evaluate(self, task_module) -> dict:

        results = []
        for case in task_module.TEST_CASES:
            actual = task_module.solve(**case["input"])
            passed = self.strategy.compare (actual, case["expected"])
            results.append({
                "input" : case["input"],
                "expected" : case["expected"],
                "actual": actual,
                "passed": passed,
            })
        return {
            "task_name": task_module.__name__.split(".")[-1],
            "total": len(results),
            "passed": sum(1 for r in results if r["passed"]),
            "details": results,

        }