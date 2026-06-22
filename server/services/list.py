from typing import Dict, List

from server.models import TrelloList
from server.utils.trello_api import TrelloClient


class ListService:
    """
    Service class for managing Trello lists.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    # Lists
    async def get_list(self, list_id: str) -> TrelloList:
        """Retrieves a specific list by its ID.

        Args:
            list_id (str): The ID of the list to retrieve.

        Returns:
            TrelloList: The list object containing list details.
        """
        response = await self.client.GET(f"/lists/{list_id}")
        return TrelloList(**response)

    async def get_lists(self, board_id: str) -> List[TrelloList]:
        """Retrieves all lists on a given board.

        Args:
            board_id (str): The ID of the board whose lists to retrieve.

        Returns:
            List[TrelloList]: A list of list objects.
        """
        response = await self.client.GET(f"/boards/{board_id}/lists")
        return [TrelloList(**list_data) for list_data in response]

    async def create_list(
        self, board_id: str, name: str, pos: str = "bottom"
    ) -> TrelloList:
        """Creates a new list on a given board.

        Args:
            board_id (str): The ID of the board to create the list in.
            name (str): The name of the new list.
            pos (str, optional): The position of the new list. Can be "top" or "bottom". Defaults to "bottom".

        Returns:
            TrelloList: The newly created list object.
        """
        data = {"name": name, "idBoard": board_id, "pos": pos}
        response = await self.client.POST("/lists", data=data)
        return TrelloList(**response)

    async def update_list(self, list_id: str, name: str) -> TrelloList:
        """Updates the name of a list.

        Args:
            list_id (str): The ID of the list to update.
            name (str): The new name for the list.

        Returns:
            TrelloList: The updated list object.
        """
        response = await self.client.PUT(f"/lists/{list_id}", data={"name": name})
        return TrelloList(**response)

    async def delete_list(self, list_id: str) -> TrelloList:
        """Archives a list.

        Args:
            list_id (str): The ID of the list to close.

        Returns:
            TrelloList: The archived list object.
        """
        response = await self.client.PUT(
            f"/lists/{list_id}/closed", data={"value": "true"}
        )
        return TrelloList(**response)

    async def move_list(
        self, list_id: str, board_id: str | None = None, pos: str | None = None
    ) -> TrelloList:
        """Moves a list to another board and/or changes its position.

        Args:
            list_id (str): The ID of the list to move.
            board_id (str | None): The ID of the destination board (optional).
            pos (str | None): The new position ("top", "bottom", or a number) (optional).

        Returns:
            TrelloList: The updated list object.
        """
        data = {}
        if board_id is not None:
            data["idBoard"] = board_id
        if pos is not None:
            data["pos"] = pos
        response = await self.client.PUT(f"/lists/{list_id}", data=data)
        return TrelloList(**response)

    async def archive_all_cards(self, list_id: str) -> Dict:
        """Archives all cards in a list.

        Args:
            list_id (str): The ID of the list whose cards to archive.

        Returns:
            Dict: The response from the archive operation.
        """
        return await self.client.POST(f"/lists/{list_id}/archiveAllCards")

    async def move_all_cards(
        self, list_id: str, board_id: str, dest_list_id: str
    ) -> List[Dict]:
        """Moves all cards in a list to another list.

        Args:
            list_id (str): The ID of the source list.
            board_id (str): The ID of the board containing the destination list.
            dest_list_id (str): The ID of the destination list.

        Returns:
            List[Dict]: The moved card objects.
        """
        return await self.client.POST(
            f"/lists/{list_id}/moveAllCards",
            data={"idBoard": board_id, "idList": dest_list_id},
        )
