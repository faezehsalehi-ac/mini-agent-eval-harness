class Agent:

    def __init__(self, task_name:str):
        self.task_name = task_name
        self.memory: list[dict] = []

    def record_attemp(self, code:str, result: dict) -> None:
        self.memory.append({
            "attemp_number": len(self.memory) +1,
            "code": code,
            "passed": result["passed"],
            "total": result["total"],
        })


    def memory_summary(self) -> str:
        if not self.memory:
            return "No previous attempts."

        lines = []
        for attemp in self.memory:
            status = "PASSED" if attemp["passed"]== attemp["total"] else "FAILED"
            lines.append(
                f"Attemp {attemp['attemp_number']}: {status}"
                f"({attemp['passed']} / {attemp['total']} test cases)"
            )
        return "\n".join(lines)
