from harness.task_loader import load_task
from harness.evaluator import Evaluator
from agent.code_generator import generate_solution, generated_solution_with_feedback
from agent.base_agent import Agent

MAX_ATTEMPTS = 3

def build_generated_task(task_module, solve_func):

        class GeneratedTask:
                TEST_CASES =  task_module.TEST_CASES
                solve = staticmethod(solve_func)
        return GeneratedTask



def run_agent_on_task(task_name: str) -> dict:
    task_module = load_task(task_name)
    agent = Agent(task_name=task_name)

    task_description = f"task: {task_name}\nExample test cases: {task_module.TEST_CASES[:2]}"

    generated_code = generate_solution(task_description)
    #print(f"Generated code:\n{generated_code}\n")

    result = None

    for attemp_num in range( 1, MAX_ATTEMPTS +1):
            namespace= {}
            try:
                    exec(generated_code, namespace)
                    generated_solve = namespace["solve"] 
                    generated_task = build_generated_task(task_module, generated_solve)
                    evaluator = Evaluator()
                    result = evaluator.evaluate(GenerationTask)
            except Exception as e:
                    result = {"passed": 0, "total": len(task_module, TEST_CASES)}

            agent.record_attemp(code=generated_code, result=result)
            print(f" Attemp{attemp_num}: {result['passed']}/{result['total']} passed")

            if result["passed"] == result["total"]:
                    break

            if attemp_num < MAX_ATTEMPTS:
                    error_info = result.get("error", f"{result['total'] - result['passed']} test case(s) failed")
                    generated_code = generated_solution_with_feedback(
                            task_description, generated_code, error_info
                    )
            return result

       

if __name__ == "__main__":
    for task_name in ["fibonacci", "is_palindrome", "two_sum" ]:
                      print(f"=== {task_name} ===")
                      run_agent_on_task(task_name)
                      print()