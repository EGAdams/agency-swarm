from agency_swarm.agents import Agent

# from agency_swarm.tools import Retrieval, CodeInterpreter
from .tools import *


class Testpipelineorchestratoragent(Agent):
    def __init__(self):
        super().__init__(
            name="TestPipelineOrchestratorAgent",
            description="",
            instructions="./instructions.md",
            files_folder="./files",
            tools=[]  # add tools here like tools=[ExampleTool]
        )
