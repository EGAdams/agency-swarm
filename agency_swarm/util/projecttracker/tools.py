from agency_swarm.tools import BaseTool
from pydantic import Field


class ExampleTool(BaseTool):
    """Enter your tool description here. It should be informative for the model."""
    content: str = Field(
        ..., description="Enter parameter descriptions using pydantic for the model here."
    )
    
    def run(self):
        """Enter your code for tool execution here."""
        pass
