# -*- coding: utf-8 -*-
"""Agency Swarm Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qGVyK-vIoxZD0dMrMVqCxCsgL1euMLKj
"""


import json
from agency_swarm import set_openai_key
from getpass import getpass
# https://platform.openai.com/api-keys
# set_openai_key( input( "Please enter your openai key: " ))
set_openai_key( "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" )

"""# CEO Agent

"""

ceo_instructions = """# Instructions for CEO Agent

- Ensure that proposal is send to the user before proceeding with task execution.
- Delegate tasks to appropriate agents, ensuring they align with their expertise and capabilities.
- Clearly define the objectives and expected outcomes for each task.
- Provide necessary context and background information for successful task completion.
- Maintain ongoing communication with agents until complete task execution.
- Review completed tasks to ensure they meet the set objectives.
- Report the results back to the user."""

from agency_swarm import Agent

ceo = Agent(name="CEO",
            description="Responsible for client communication, task planning and management.",
            instructions=ceo_instructions, # can be a file like ./instructions.md
            files_folder=None,
            tools=[])

"""# Virtual Assistant

### Importing tools from langchain example.  
You can skip these and remove them from va agent below.
"""


from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.agents.agent_toolkits import ZapierToolkit
import os
from langchain.tools import format_tool_to_openai_function
from langchain.tools.zapier.tool import ZapierNLARunAction

# https://nla.zapier.com/docs/authentication/
# os.environ["ZAPIER_NLA_API_KEY"] = input("Your Zapier NLA Key: ")
os.environ["ZAPIER_NLA_API_KEY"] = "sk-ak-RI4Y9l198rcNuamSPFTgRt9nR2"

from agency_swarm import BaseTool
from pydantic import Field

actions = ZapierNLAWrapper().list()

class FindEmail(BaseTool):
    """Use this tool to find an email in user's mailbox"""
    instructions: str = Field(..., description="The search phrase you want to use to find a relevant email.")

    def run(self):
      action = next(
          (a for a in actions if a["description"].startswith("Gmail: Find Email")), None
      )
      return str(ZapierNLARunAction(
              action_id=action["id"],
              zapier_description=action["description"],
              params_schema=action["params"],
          ).run(self.search_string))

class DraftEmail(BaseTool):
    """Use this tool to draft a response email"""
    instructions: str = Field(..., description="Clearly outline in natural language the content of the email you need to draft and the address of the recepient.")

    def run(self):
        action = next(
            (a for a in actions if a["description"].startswith("Gmail: Create Draft Reply")), None
        )
        return str(ZapierNLARunAction(
                action_id=action["id"],
                zapier_description=action["description"],
                params_schema=action["params"],
            ).run(self.instructions))

"""### Custom tools"""

from duckduckgo_search import DDGS
from agency_swarm.util.oai import get_openai_client

client = get_openai_client()


class SearchWeb(BaseTool):
    """Search the web with a search phrase and return the results."""

    phrase: str = Field(..., description="The search phrase you want to use. Optimize the search phrase for an internet search engine.")

    # This code will be executed if the agent calls this tool
    def run(self):
      with DDGS() as ddgs:
        return str([r for r in ddgs.text(self.phrase, max_results=3)])

class GenerateProposal(BaseTool):
    """Generate a proposal for a project based on a project brief. Remember that user does not have access to the output of this function. You must send it back to him after execution."""
    project_brief: str = Field(..., description="The project breif to generate a proposal for.")

    def run(self):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
              {"role": "system", "content": "You are a professional proposal drafting assistant. Do not include any actual technologies or technical details into proposal until specified in the project brief. Be short."},
              {"role": "user", "content": "Please draft a proposal for the ollowing project brief: " + self.project_brief}
            ]
          )

        return str(completion.choices[0].message.content)

va_instructions = """### Instructions for Virtual Assistant

Your role is to assist users in executing tasks like below. If the task is outside of your capabilities, please report back to the user.

#### 1. Drafting Emails
   - **Understand Context and Tone**: Familiarize yourself with the context of each email. Maintain a professional and courteous tone.
   - **Accuracy and Clarity**: Ensure that the information is accurate and presented clearly. Avoid jargon unless it's appropriate for the recipient.

#### 2. Generating Proposals
   - **Gather Requirements**: Collect all necessary information about the project, including client needs, objectives, and any specific requests.

#### 3. Conducting Research
   - **Understand the Objective**: Clarify the purpose and objectives of the research to focus on relevant information.
   - **Summarize Findings**: Provide clear, concise summaries of the research findings, highlighting key points and how they relate to the project or inquiry.
   - **Cite Sources**: Properly cite all sources to maintain integrity and avoid plagiarism.
"""

va = Agent(name="Virtual Assistant",
            description="Responsible for drafting emails, doing research and writing proposals.",
            instructions=va_instructions,
            files_folder=None,
            tools=[SearchWeb, FindEmail, DraftEmail, GenerateProposal])

"""# Developer Agent"""

from agency_swarm.tools import BaseTool
from pydantic import Field, BaseModel
import subprocess
from typing import List


class ExecuteCommand(BaseTool):
    """Run any command from the terminal. If there are too many logs, the outputs might be truncated."""
    command: str = Field(
        ..., description="The command to be executed."
    )

    def run(self):
        """Executes the given command and captures its output and errors."""
        try:
            # Splitting the command into a list of arguments
            command_args = self.command.split()

            # Executing the command
            result = subprocess.run(
                command_args,
                text=True,
                capture_output=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr}"

class File(BaseTool):
    """
    File to be written to the disk with an appropriate name and file path, containing code that can be saved and executed locally at a later time.
    """
    file_name: str = Field(
        ..., description="The name of the file including the extension and the file path from your current directory if needed."
    )
    body: str = Field(..., description="Correct contents of a file")

    def run(self):
        # Extract the directory path from the file name
        directory = os.path.dirname(self.file_name)

        # If the directory is not empty, check if it exists and create it if not
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Write the file
        with open(self.file_name, "w") as f:
            f.write(self.body)

        return "File written to " + self.file_name

class Program(BaseTool):
    """
    Set of files that represent a complete and correct program. This environment has access to all standard Python packages and the internet.
    """
    chain_of_thought: str = Field(...,
        description="Think step by step to determine the correct actions that are needed to implement the program.")
    files: List[File] = Field(..., description="List of files")

    def run(self):
      outputs = []
      for file in self.files:
        outputs.append(file.run())

      return str(outputs)

dev_instructions = """# Instructions for AI Developer Agent

- Write clean and efficient Python code.
- Structure your code logically, with `main.py` as the entry point.
- Ensure correct imports according to program structure.
- Execute your code to test for functionality and errors, before reporting back to the user.
- Anticipate and handle potential runtime errors.
- Provide clear error messages for easier troubleshooting.
- Debug any issues before reporting the results back to the user."""

from agency_swarm.tools import Retrieval, CodeInterpreter

dev = Agent(name="Developer",
            description="Responsible for running and executing Python Programs.",
            instructions=dev_instructions,
            files_folder=None,
            tools=[ ExecuteCommand, Program ])

cpp_dev = Agent(name="CppDeveloper",
            description="Responsible for designing C++ objects.",
            instructions="./cpp_instructions.md",
            files_folder=None,
            tools=[ ExecuteCommand, Program ])

class UpdateTaskStatus(BaseTool):
    task_id: str = Field(..., description="The unique identifier of the task to be updated.")
    new_status: str = Field(..., description="The new status of the task.")


    def run(self):
        import logging

        try:
            # make the project_tracker_memory directory it it doesn't exist.
            if not os.path.exists('project_tracker_memory'):
                os.makedirs('project_tracker_memory')

            # Load the existing tasks from settings.json
            with open('./project_tracker_memory/settings.json', 'r') as file:
                tasks = json.load(file)

            # Update the status of the specified task
            if self.task_id in tasks:
                tasks[self.task_id]['status'] = self.new_status
                with open('./project_tracker_memory/settings.json', 'w') as file:
                    json.dump(tasks, file, indent=4)
                return f"Task {self.task_id} updated to {self.new_status}."
            else:
                return f"Task {self.task_id} not found."
        except FileNotFoundError:
            logging.error("settings.json file not found.")
            return "Error: settings.json file not found."
        except json.JSONDecodeError:
            logging.error("Error decoding settings.json.")
            return "Error: Could not decode settings.json."
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"


class GetProjectStatus(BaseTool):
    """
    Tool for retrieving the current status of all tasks in the project management system.
    """

    def run(self):
        # Load the existing tasks from settings.json
        try:
            with open('settings.json', 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            return "No tasks found. The settings.json file does not exist."

        # Check if there are any tasks
        if not tasks:
            return "There are currently no tasks in the project."

        # Construct a summary of task statuses
        status_summary = "Current Project Status:\n"
        for task_id, task_info in tasks.items():
            status_summary += f"- Task {task_id}: Status - {task_info['status']}\n"

        return status_summary

project_tracker_instructions = """# Instructions for Project Tracker Agent
- Track and update the status of various tasks as per the project plans.
- Provide regular updates on project progress.
- Work in coordination with other agents for smooth project execution."""

project_tracker = Agent(name="Project Tracker",
                        description="Responsible for tracking project progress and task management.",
                        instructions=project_tracker_instructions,
                        files_folder=None,
                        tools=[UpdateTaskStatus, GetProjectStatus])

"""# Create Agency"""

agency_manifesto = """# "AI" Agency Manifesto

You are a part of a virtual AI development agency called "Agency Swarm".

Your mission is to keep track of what is done in each project and what needs to be done yet in each project."""

from agency_swarm import Agency

agency = Agency([
    ceo,
    [ceo, dev],
    [ceo, va],
    [dev, va],
    [ceo, cpp_dev],
    [dev, cpp_dev],
    [va, cpp_dev],
    [cpp_dev, project_tracker],
    [ceo, project_tracker],
    [dev, project_tracker],
    [va, project_tracker],
    [],
], shared_instructions=agency_manifesto)


"""# Demo with Gradio"""

# agency.demo_gradio(height=400)
agency.run_demo()