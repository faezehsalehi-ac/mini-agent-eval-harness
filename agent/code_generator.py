import anthropic

client = anthropic.Anthropic()

def generate_solution(task_description: str) -> str:
    prompt = f"""Write a Python function named 'solve' that solves this task:
    {task_description}
Return Only the function code, no explanation, no markdown formatting, no '''python fences. Just the raw Python code strting with 'def solve('."""

    response = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens=500,
        messages =[{"role": "user", "content":prompt}],
        
    )

    return response.content[0].text.strip()




def generated_solution_with_feedback(task_description: str, previous_attemp:str, error_info:str) -> str:

    prompt = f"""You previously tried to solve this task:
    {task_description}

    Your previous attemp was:
    {previous_attemp}
    It failed with this result: {error_info}
    Write a corrected Python function named 'solve'. Return Only the function code, no explanation, no markdown formatting, no '''python fences. """

    response = client.messsages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 500,
        messages = [{"role": "user", "content": prompt}],

    )

    return response.content[0].text.strip()