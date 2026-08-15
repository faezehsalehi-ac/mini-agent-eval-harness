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