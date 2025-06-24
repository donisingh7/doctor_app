from fastapi import FastAPI, Depends
from .deps import get_db, settings
from .mcp_tools import TOOLS

app = FastAPI()

@app.get("/mcp/tools")
async def list_tools():
    return [{"name": t.name, "description": t.description} for t in TOOLS.values()]

@app.post("/mcp/run/{tool_name}")
async def run_tool(tool_name: str, payload: dict, db=Depends(get_db)):
    tool = TOOLS.get(tool_name)
    if not tool: raise HTTPException(404, "Tool not found")
    # inject db or settings as needed
    return await tool.run(**payload, db=db, settings=settings)
