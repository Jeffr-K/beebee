import os
from typing import Any, List

from langchain_tavily import TavilySearch


class TavilyTool:

    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")

    def tool(self) -> List[Any]:
        tool = TavilySearch(max_results=2)
        return [tool]