from agency_swarm.agents import Agent

# from agency_swarm.tools import Retrieval, CodeInterpreter
from .tools import *


class Projecttracker(Agent):
    def __init__(self):
        super().__init__(
            name="ProjectTracker",
            description="Responsible for tracking project progress, task management and communicates with all other Agents to synchronize task statuses",
            instructions="./instructions.md",
            files_folder="./files",
            tools=[]  # add tools here like tools=[ExampleTool]
        )
