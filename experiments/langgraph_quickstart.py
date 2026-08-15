from typing import TypedDict
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    task: str
    result: str

def solve_step(state: AgentState) -> AgentState:
    state["result"] = f"Solved: {state['task']}"
    return state

def report_step(state: AgentState) -> AgentState:
    state["result"] = f"[REPORT] {state['result']}"
    return state

graph = StateGraph(AgentState)
graph.add_node ("solve", solve_step)
graph.add_node ("report", report_step)

graph.set_entry_point("solve")
graph.add_edge("solve", "report")
graph.add_edge("report", END)

app = graph.compile()

final_state = app.invoke({"task": "fibonacci(10)", "result": ""})

print (final_state)
