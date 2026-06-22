"""
Service for managing Trello card comments in MCP server.
"""

from typing import Any, Dict, List

from server.utils.trello_api import TrelloClient


class CommentService:
    """
    Service class for managing Trello card comments.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_comments(self, card_id: str) -> List[Dict]:
        """Retrieves all comments on a card.

        Args:
            card_id (str): The ID of the card whose comments to retrieve.

        Returns:
            List[Dict]: A list of comment action objects.
        """
        return await self.client.GET(
            f"/cards/{card_id}/actions", params={"filter": "commentCard"}
        )

    async def add_comment(self, card_id: str, text: str) -> Dict:
        """Adds a comment to a card.

        Args:
            card_id (str): The ID of the card to comment on.
            text (str): The text content of the comment.

        Returns:
            Dict: The created comment action object.
        """
        return await self.client.POST(
            f"/cards/{card_id}/actions/comments", data={"text": text}
        )

    async def update_comment(self, action_id: str, text: str) -> Dict:
        """Updates an existing comment.

        Args:
            action_id (str): The ID of the comment action to update.
            text (str): The new text content of the comment.

        Returns:
            Dict: The updated comment action object.
        """
        return await self.client.PUT(f"/actions/{action_id}", data={"text": text})

    async def delete_comment(self, action_id: str) -> Dict[str, Any]:
        """Deletes a comment.

        Args:
            action_id (str): The ID of the comment action to delete.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(f"/actions/{action_id}")
