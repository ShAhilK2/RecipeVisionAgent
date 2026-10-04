

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool
from typing import Dict, Any
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')



load_dotenv()
client = TavilyClient()



@tool
def search_recipes(query: str) -> Dict[str, any]:
    """Search for information based on a query."""
    logging.info(f"Searching for: {query}")
    response = client.search(query=query)
    return response