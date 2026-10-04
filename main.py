from dotenv import load_dotenv
from langchain.agents import create_agent
from tools import search_recipes
from prompt import CHEF_PROMPT, SYSTEM_CHEF_PROMPT
from photo_decode import choose_image_file, build_image_message
load_dotenv()
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')


logging.info("Creating agent...")
agent = create_agent(
    model="gpt-5-nano",
    tools=[search_recipes],
    system_prompt=SYSTEM_CHEF_PROMPT
)

logging.info("Choosing image file...")
path = choose_image_file()

logging.info("Building Image into base64 and adding Chef prompt...")
message=build_image_message(path,CHEF_PROMPT)


logging.info("Invoking agent...")
response = agent.invoke({
    "messages" : [
      message
    ]
})


logging.info("Printing response...")
print(response["messages"][-1].content)