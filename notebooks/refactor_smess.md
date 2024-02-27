# Persona
Act as a world-class Python Developer and seasoned user of many types of effective software design patterns.  

# What I think
The following Python code needs a lot of work, plus I don't even think it is working right as it is.  

# Your Task
Completely redesign the following code using any design patterns that you see fit.  It probably needs to use the Observer pattern for communication for starters.

Don't write any code yet.  I want you to think step by step and concentrate all of you energy on making the design decisions.  

Please write the source for a mermaid sequence diagram so that I can look at it and see what you are thinking.  I'll give feedback then.

# Code to refactor
```python
def _create_send_message_tool(self, agent: Agent, recipient_agents: List[Agent]):
        """
        Creates a SendMessage tool to enable an agent to send messages to specified recipient agents.


        Parameters:
            agent (Agent): The agent who will be sending messages.
            recipient_agents (List[Agent]): A list of recipient agents who can receive messages.

        Returns:
            SendMessage: A SendMessage tool class that is dynamically created and configured for the given agent and its recipient agents. This tool allows the agent to send messages to the specified recipients, facilitating inter-agent communication within the agency.
        """
        recipient_names = [agent.name for agent in recipient_agents]
        recipients = Enum("recipient", {name: name for name in recipient_names})

        agent_descriptions = ""
        for recipient_agent in recipient_agents:
            if not recipient_agent.description:
                continue
            agent_descriptions += recipient_agent.name + ": "
            agent_descriptions += recipient_agent.description + "\n"

        outer_self = self

        class SendMessage(BaseTool):
            instructions: str = Field(...,
                                      description="Please repeat your instructions step-by-step, including both completed "
                                                  "and the following next steps that you need to perfrom. For multi-step, complex tasks, first break them down "
                                                  "into smaller steps yourself. Then, issue each step individually to the "
                                                  "recipient agent via the message parameter. Each identified step should be "
                                                  "sent in separate message. Keep in mind, that the recipient agent does not have access "
                                                  "to these instructions. You must include recipient agent-specific instructions "
                                                  "in the message parameter.")
            recipient: recipients = Field(..., description=agent_descriptions)
            message: str = Field(...,
                                 description="Specify the task required for the recipient agent to complete. Focus on "
                                             "clarifying what the task entails, rather than providing exact "
                                             "instructions.")
            message_files: List[str] = Field(default=None,
                                             description="A list of file ids to be sent as attachments to this message. Only use this if you have the file id that starts with 'file-'.",
                                             examples=["file-1234", "file-5678"])

            @field_validator('recipient')
            def check_recipient(cls, value):
                if value.value not in recipient_names:
                    raise ValueError(f"Recipient {value} is not valid. Valid recipients are: {recipient_names}")
                return value

            def run(self):
                thread = outer_self.agents_and_threads[self.caller_agent.name][self.recipient.value]

                if not outer_self.async_mode:
                    gen = thread.get_completion(message=self.message, message_files=self.message_files)
                    try:
                        while True:
                            yield next(gen)
                    except StopIteration as e:
                        message = e.value
                else:
                    message = thread.get_completion_async(message=self.message, message_files=self.message_files)

                return message or ""

        SendMessage.caller_agent = agent
        if self.async_mode:
            SendMessage.__doc__ = self.send_message_tool_description_async
        else:
            SendMessage.__doc__ = self.send_message_tool_description

        return SendMessage

    def _create_get_response_tool(self, agent: Agent, recipient_agents: List[Agent]):
        """
        Creates a CheckStatus tool to enable an agent to check the status of a task with a specified recipient agent.
        """
        recipient_names = [agent.name for agent in recipient_agents]
        recipients = Enum("recipient", {name: name for name in recipient_names})

        outer_self = self

        class GetResponse(BaseTool):
            """This tool allows you to check the status of a task or get a response from a specified recipient agent, if the task has been completed. You must always use 'SendMessage' tool with the designated agent first."""
            recipient: recipients = Field(...,
                                          description=f"Recipient agent that you want to check the status of. Valid recipients are: {recipient_names}")

            @field_validator('recipient')
            def check_recipient(cls, value):
                if value.value not in recipient_names:
                    raise ValueError(f"Recipient {value} is not valid. Valid recipients are: {recipient_names}")
                return value

            def run(self):
                thread = outer_self.agents_and_threads[self.caller_agent.name][self.recipient.value]

                return thread.check_status()

        GetResponse.caller_agent = agent

        return GetResponse
```
