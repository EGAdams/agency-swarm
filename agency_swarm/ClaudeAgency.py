class Agency:

    def __init__(self):
        self.agents = {}
        self.communication_channels = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent
        self.setup_communication_channels(agent)

    def setup_communication_channels(self, agent):
        recipients = self.get_allowed_recipients(agent)
        send_message_tool = self.create_send_message_tool(agent, recipients)
        agent.add_tool(send_message_tool)

        if self.async_mode:
            get_response_tool = self.create_get_response_tool(agent, recipients)
            agent.add_tool(get_response_tool)

    def get_allowed_recipients(self, agent):
        # Logic to determine which other agents this agent can send messages to
        # Returns list of agent objects
        return allowed_recipients
    
    def create_send_message_tool(self, agent, recipients):
        # Create and return SendMessage tool configured for given agent and recipients

    def create_get_response_tool(self, agent, recipients):
        # Create and return GetResponse tool for given agent and recipients

class SendMessage(BaseTool):

    def __init__(self, agent, recipients):
        self.agent = agent
        self.recipients = recipients
    
    def run(self):
        # Logic to send message and return response

class GetResponse(BaseTool):

    def __init__(self, agent, recipients):
        self.agent = agent
        self.recipients = recipients

    def run(self):
        # Logic to get response status from recipient