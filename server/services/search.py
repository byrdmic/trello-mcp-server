"""
Service for searching across Trello in MCP server.
"""

from typing import Dict, List

from server.utils.trello_api import TrelloClient


class SearchService:
    """
    Service class for searching Trello.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def search(self, **kwargs) -> Dict:
        """Searches across Trello cards, boards, organizations, and members.

        Args:
            **kwargs: Search parameters (query and optional filters).

        Returns:
            Dict: The search results, keyed by model type (cards, boards, ...).
        """
        return await self.client.GET("/search", params=kwargs)

    async def search_members(self, query: str, limit: int = 8) -> List[Dict]:
        """Searches for members by name or username.

        Args:
            query (str): The search query.
            limit (int): The maximum number of members to return (1-20).

        Returns:
            List[Dict]: A list of matching member objects.
        """
        return await self.client.GET(
            "/search/members", params={"query": query, "limit": limit}
        )
