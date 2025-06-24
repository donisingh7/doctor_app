from fastapi import HTTPException
from typing import Any

class MCPTool:
    name: str
    description: str
    async def run(self, **kwargs) -> Any:
        raise NotImplementedError

# Example:
class CheckAvailability(MCPTool):
    name = "check_availability"
    description = "Given doctor_id & date_range, return free slots"

    async def run(self, doctor_id: int, start: str, end: str):
        # call crud.get_free_slots(...)
        return [...]

# Later, a registry:
TOOLS = { tool.name: tool() for tool in [CheckAvailability(), …] }
