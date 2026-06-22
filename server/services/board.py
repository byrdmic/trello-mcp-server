"""
Service for managing Trello boards in MCP server.
"""

from typing import Any, Dict, List

from server.models import TrelloBoard, TrelloLabel
from server.utils.trello_api import TrelloClient


class BoardService:
    """
    Service class for managing Trello boards
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_board(self, board_id: str) -> TrelloBoard:
        """Retrieves a specific board by its ID.

        Args:
            board_id (str): The ID of the board to retrieve.

        Returns:
            TrelloBoard: The board object containing board details.
        """
        response = await self.client.GET(f"/boards/{board_id}")
        return TrelloBoard(**response)

    async def get_boards(self, member_id: str = "me") -> List[TrelloBoard]:
        """Retrieves all boards for a given member.

        Args:
            member_id (str): The ID of the member whose boards to retrieve. Defaults to "me" for the authenticated user.

        Returns:
            List[TrelloBoard]: A list of board objects.
        """
        response = await self.client.GET(f"/members/{member_id}/boards")
        return [TrelloBoard(**board) for board in response]

    async def get_board_labels(self, board_id: str) -> List[TrelloLabel]:
        """Retrieves all labels for a specific board.

        Args:
            board_id (str): The ID of the board whose labels to retrieve.

        Returns:
            List[TrelloLabel]: A list of label objects for the board.
        """
        response = await self.client.GET(f"/boards/{board_id}/labels")
        return [TrelloLabel(**label) for label in response]

    async def create_board_label(self, board_id: str, **kwargs) -> TrelloLabel:
        """Create label for a specific board.

        Args:
            board_id (str): The ID of the board whose to add label.

        Returns:
            List[TrelloLabel]: A list of label objects for the board.
        """
        response = await self.client.POST(f"/boards/{board_id}/labels", data=kwargs)
        return TrelloLabel(**response)

    async def create_board(self, **kwargs) -> TrelloBoard:
        """Creates a new board.

        Args:
            **kwargs: Board attributes (name and optional fields).

        Returns:
            TrelloBoard: The newly created board object.
        """
        response = await self.client.POST("/boards", data=kwargs)
        return TrelloBoard(**response)

    async def update_board(self, board_id: str, **kwargs) -> TrelloBoard:
        """Updates a board's attributes.

        Args:
            board_id (str): The ID of the board to update.
            **kwargs: The board attributes to update.

        Returns:
            TrelloBoard: The updated board object.
        """
        response = await self.client.PUT(f"/boards/{board_id}", data=kwargs)
        return TrelloBoard(**response)

    async def close_board(self, board_id: str) -> TrelloBoard:
        """Closes (archives) a board.

        Args:
            board_id (str): The ID of the board to close.

        Returns:
            TrelloBoard: The closed board object.
        """
        response = await self.client.PUT(f"/boards/{board_id}", data={"closed": True})
        return TrelloBoard(**response)

    async def delete_board(self, board_id: str) -> Dict[str, Any]:
        """Permanently deletes a board.

        Args:
            board_id (str): The ID of the board to delete.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(f"/boards/{board_id}")
