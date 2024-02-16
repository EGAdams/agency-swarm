# Persona
- World-Class Python developer
- Expert at using Python with Object-Oriented Programming and especially GoF design patterns.

# Your Task
The following describes the code from agency_swarm/agency/agency.py.
Please make a class diagram for each of the objects that would be involved in this system if you where to design it yourself.

# Agency Code
```
The code from agency_swarm/agency/agency.py is designed to create a system that can handle tasks and communications in a structured way, similar to how a company operates with different departments and employees. This system is called an "Agency," and it is made up of "agents" which are like workers, each with their own roles and responsibilities.

Purpose of the Code: The main purpose of this code is to set up an Agency that can process messages and perform tasks. It's like creating a virtual office with a boss (CEO), workers (agents), and a way for them to talk to each other (threads). There's also a way for people outside the agency (users) to interact with it.

Inputs: The code takes several inputs:

agency_chart: This is like an organizational chart that tells the Agency how the agents are structured and how they should interact with each other.
shared_instructions: This is an optional text that can be shared with all agents, like a company-wide memo.
message: When someone wants to get something done, they send a message to the Agency.
message_files: These are optional files that can be sent along with a message.
yield_messages: This is a setting that tells the Agency whether to show all the back-and-forth messages or just the final result.
Outputs: The code produces different outputs depending on the function:

get_completion: This gives back either a series of messages showing the conversation as it happens or the final result of the message processing.
demo_gradio: This launches a visual interface where users can chat with the Agency.
run_demo: This shows the Agency's conversation in a simple text-based format, like a chat window in a command line.
Logic and Algorithm: The code works by first setting up the Agency with its agents and threads based on the agency_chart. It reads any shared instructions if they're provided. Then, it prepares a way for the Agency to send messages internally. When a user sends a message, the Agency processes it through a "main thread," which is like the main conversation channel. If the user wants to see all the messages as they happen, the Agency uses a generator to provide them one by one. Otherwise, it just shows the end result.

Logic Flows and Data Transformations: When the Agency is created, it checks if there's a boss (CEO) and sets up the workers (agents) according to the chart. It also sets up communication lines (threads) between agents so they can talk to each other. When a message comes in, the Agency uses its main thread to figure out what to do with it. It might ask different agents to work on parts of the task and then put all their work together to come up with a final answer. If the Agency is running a demo, it uses a visual or text-based interface to let users talk to it and see how it responds.

In summary, the code is like building and running a virtual office that can take tasks, figure out the best way to do them, and then show the work as it happens or just the final result. It's designed to be flexible and structured, so it can handle different kinds of tasks and workflows.
```


 
