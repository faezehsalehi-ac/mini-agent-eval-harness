import anthropic

client = anthropic.Anthropic()

def add_numbers(a:float, b:float) -> float:
    return a+b


tools = [

    {
        "name": "add_numbers",
        "description":"Add Two numbers together and return the result.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
            },
            "required": ["a", "b"],
        },
    }
]

response = client.messages.create(
    model = "claude-sonnet-4-6",
    max_tokens = 1000,
    tools = tools,
    messages= [{"role": "user", "content": "what is 456 plus 789?"}],
)

for block in response.content:
    if block.type == "tool_use":
        print(f"Model wants to call: {block.name} with input {block.input}")
        result = add_numbers(**block.input)
        print(f"we executed it ourselves, result: {result}")
    elif block.type == "text":
        print(f"Model said:{block.text}")