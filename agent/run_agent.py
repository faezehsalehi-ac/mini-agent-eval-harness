from harness.task_loader import load_task
from harness.evaluator import Evaluator
from agent.code_generator import generate_solution
from agent.base_agent import Agent


def run_agent_on_task(task_name: str) -> dict:
    task_module = load_task(task_name)
    agent = Agent(task_name=task_name)

    task_description = f"task: {task_name}\nExample test cases: {task_module.TEST_CASES[:2]}"

    generated_code = generate_solution(task_description)
    print(f"Generated code:\n{generated_code}\n")


    namespace = []
    exec(generated_code, namespace)
    generated_solve = namespace["solve"]


    class GenerationTask:
        TEST_CASES = task_module.TEST_CASES
        solve = staticmethod(generated_solve)

    evaluator = Evaluator()
    result = evaluator.evaluate(GenerationTask)
    agent.record_attemp(code=generated_code, result=result)

    return result

if __name__ == "__main__":
    for task_name in ["fibonacci", "is_palindrome", "two_sum" ]:
                      print(f"=== {task_name} ===")
                      result = run_agent_on_task(task_name)
                      status = "PASS" if result["passed"] == result["total"] else "FAIL"
                      print(f"[{status}] {result['passed']}/{result['tatal']}\n")