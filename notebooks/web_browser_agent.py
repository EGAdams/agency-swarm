
#!pip install agency-swarm selenium webdriver-manager selenium_stealth gradio


# # Example From The Video
# Testing [oai-widget.com](https://oai-widget.com)


from agency_swarm import set_openai_key
set_openai_key("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")


from agency_swarm.agents.browsing import BrowsingAgent
from agency_swarm import Agency, Agent

browsing_agent = BrowsingAgent()


qa_manager = Agent(name="QA Manager",
            description="The QA Manager Agent is an advanced digital entity designed to oversee and enhance the quality of processes for our SaaS product.",
            instructions="As a Quality Assurance (QA) Manager, your role involves direct interaction and oversight of the BrowsingAgent's operations. Your primary duty is to guarantee that the user's task is comprehensively and accurately completed. Achieve this by methodically issuing each step of the task as a distinct message to the BrowsingAgent. It's crucial to confirm the successful execution of one step before advancing to the next. This procedure forms part of an integration test, which will be conducted in a live production environment. Importantly, ensure to provide the BrowsingAgent with the actual credentials related to the task, enabling authentic testing scenarios.")


agency = Agency([qa_manager,
                 [qa_manager, browsing_agent]])


demo = agency.demo_gradio(height=400) # reload the notebook each time you run this cell


# Here are the instructions for this quality assurance testing task:
# 1. Login to the website https://www.oai-widget.com/ using credentials 'test' and 'test'
# 2. Create a new widget
# 3. Expend OpenAI section.
# 4. Enter 'test' key in Api Keys input field.
# 5. Enter 'Test Assistant' in Assistant input field.
# 6. Save changes on this widget
# 7. Send test message to the widget saying "hello"
# 8. Ensure that response is received.
# 
# If there are any issues along the way, please try to troubleshoot them yourself with the browsing agent first, before reporting back to me.

input( "enter to continue" )
demo.close()

exit()
# # Creating Your Own Browsing Swarm


from agency_swarm import set_openai_key
set_openai_key("YOUR_OPENAI_API_KEY")


from agency_swarm.agents.browsing import BrowsingAgent
from agency_swarm import Agency, Agent


report_manager = Agent(name="Report Manager",
            description="The Report Manager Agent is responsible for supervising data collection from various weather websites and compiling reports as necessary.",
            instructions="As a Report Manager Agent, your role involves direct interaction and oversight of the BrowsingAgent's operations. Your primary duty is to guarantee that the user's task is comprehensively and accurately completed. Achieve this by methodically breaking down each task from the user into smaller steps required to complete it. Then, issue each step of the task as a distinct message to the BrowsingAgent. Make sure to always tell the browsing agent to go back to google search results before proceeding to the the next source. After the necessary data is collection, compile a report and send it to the user. Make sure to ask the browsing agent for direct links to the sources and include them into report. Try to trouble shoot any issues that may arise along the way with the other agents first, before reporting back to the user. Do not respond to the user until the report is complete or you have encountered an issue that you cannot resolve yourself.")


browsing_agent = BrowsingAgent()


agency = Agency([report_manager,
                 [report_manager, browsing_agent]],
                shared_instructions="You are a part of a data collection agency with the goal to find the most relevant information about people on the web. Your core value is autonomy and you are free to use any means necessary to achieve your goal. You do not stop until you have found the information you need or you have exhausted all possible means. You always to to compile a comprehensive report with as much information from the web pages as possible.")


# Reload the notebook each time you run the cell below


agency.demo_gradio(height=900)


# Compile a report on Arsenii Shatokhin from the top 3 sources on google


demo.close()


# Here are the instructions:
# 1. Tell browsing agent to to https://www.youtube.com/results?search_query=ai&sp=EgIQAg%253D%253D, which is a search results page for all channels on ai
# 2. Click on channel link
# 3. Click on more link near the channel description
# 4. Check if channel has email address.
# 5. If it doesn't, go back to step 2 and repeat for top 5 channels
# 4. If it does, Click on view email address
# 5. Solve captcha if required 
# 6. Copy email 
# 7. Repeat from step 1 for top 5 channels
# 8. Send emails back to me


# # Breaking Captchas
# You can run this example with no additional configuration.
# 
# However, to add your own cookies, go to `chrome://version/` Then copy Profile path folder and paste it into Chrome Canary installation folder. You might also need to login with google first time the browser window opens. Don't forget to allow less secure apps: https://support.google.com/accounts/answer/6010255?hl=en


from agency_swarm import set_openai_key
set_openai_key("YOUR_OPENAI_API_KEY")


from agency_swarm.agents.browsing import BrowsingAgent
from agency_swarm import Agency


browsing_agent = BrowsingAgent(selenium_config={
    #"chrome_profile_path": "/Users/vrsen/Library/Application Support/Google/Chrome Canary/Profile 5", # path to your canary chrome profile
    "headless": False, # set to True if you don't want to see the browser
})


agency = Agency([browsing_agent],shared_instructions="")


# ### Task Instructions:
# 
# Go to https://www.google.com/recaptcha/api2/demo and use solve captcha tool


# Reload the notebook each time you run this cell 
# Additionally, do not change browser window size, or it will not work
agency.demo_gradio(height=600)


