"""
Service for managing Trello cards in MCP server.
"""

from typing import Any, Dict, List

from server.models import TrelloCard
from server.utils.trello_api import TrelloClient


class CardService:
    """
    Service class for managing Trello cards.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_card(self, card_id: str) -> TrelloCard:
        """Retrieves a specific card by its ID.

        Args:
            card_id (str): The ID of the card to retrieve.

        Returns:
            TrelloCard: The card object containing card details.
        """
        response = await self.client.GET(f"/cards/{card_id}")
        return TrelloCard(**response)

    async def get_cards(self, list_id: str) -> List[TrelloCard]:
        """Retrieves all cards in a given list.

        Args:
            list_id (str): The ID of the list whose cards to retrieve.

        Returns:
            List[TrelloCard]: A list of card objects.
        """
        response = await self.client.GET(f"/lists/{list_id}/cards")
        return [TrelloCard(**card) for card in response]

    async def create_card(self, **kwargs) -> TrelloCard:
        """Creates a new card in a given list.

        Args
            list_id (str): The ID of the list to create the card in.
            name (str): The name of the new card.
            desc (str, optional): The description of the new card. Defaults to None.

        Returns:
            TrelloCard: The newly created card object.
        """
        response = await self.client.POST("/cards", data=kwargs)
        return TrelloCard(**response)

    async def update_card(self, card_id: str, **kwargs) -> TrelloCard:
        """Updates a card's attributes.

        Args:
            card_id (str): The ID of the card to update.
            **kwargs: Keyword arguments representing the attributes to update on the card.

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(f"/cards/{card_id}", data=kwargs)
        return TrelloCard(**response)

    async def delete_card(self, card_id: str) -> Dict[str, Any]:
        """Deletes a card.

        Args:
            card_id (str): The ID of the card to delete.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(f"/cards/{card_id}")

    async def set_due(self, card_id: str, due: str | None) -> TrelloCard:
        """Sets or clears a card's due date.

        Args:
            card_id (str): The ID of the card.
            due (str | None): An ISO 8601 datetime to set, or None to clear the due date.

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(f"/cards/{card_id}", data={"due": due})
        return TrelloCard(**response)

    async def set_due_complete(self, card_id: str, value: bool) -> TrelloCard:
        """Marks a card's due date as complete or incomplete.

        Args:
            card_id (str): The ID of the card.
            value (bool): Whether the due date is complete.

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(
            f"/cards/{card_id}", data={"dueComplete": value}
        )
        return TrelloCard(**response)

    async def move_card(
        self, card_id: str, list_id: str, pos: str = "bottom"
    ) -> TrelloCard:
        """Moves a card to a list and/or position.

        Args:
            card_id (str): The ID of the card to move.
            list_id (str): The ID of the destination list.
            pos (str): The position in the list ("top", "bottom", or a number).

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(
            f"/cards/{card_id}", data={"idList": list_id, "pos": pos}
        )
        return TrelloCard(**response)

    async def set_closed(self, card_id: str, closed: bool) -> TrelloCard:
        """Archives or unarchives a card.

        Args:
            card_id (str): The ID of the card.
            closed (bool): True to archive, False to unarchive (send back to the board).

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(f"/cards/{card_id}", data={"closed": closed})
        return TrelloCard(**response)

    async def set_cover(self, card_id: str, **kwargs) -> TrelloCard:
        """Sets a card's cover.

        Args:
            card_id (str): The ID of the card.
            **kwargs: Cover attributes (color, idAttachment, idUploadedBackground, size, brightness).

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(f"/cards/{card_id}", data={"cover": kwargs})
        return TrelloCard(**response)

    async def get_actions(self, card_id: str, filter: str | None = None) -> List[Dict]:
        """Retrieves the action history of a card.

        Args:
            card_id (str): The ID of the card.
            filter (str | None): Comma-separated action types to include (e.g. "updateCard").

        Returns:
            List[Dict]: A list of action objects.
        """
        params = {"filter": filter} if filter else None
        return await self.client.GET(f"/cards/{card_id}/actions", params=params)

    async def add_attachment(self, card_id: str, **kwargs) -> Dict:
        """Adds a URL attachment to a card.

        Args:
            card_id (str): The ID of the card.
            **kwargs: Attachment attributes (url, name, mimeType).

        Returns:
            Dict: The created attachment object.
        """
        return await self.client.POST(f"/cards/{card_id}/attachments", data=kwargs)

    async def get_attachments(self, card_id: str) -> List[Dict]:
        """Retrieves all attachments on a card.

        Args:
            card_id (str): The ID of the card.

        Returns:
            List[Dict]: A list of attachment objects.
        """
        return await self.client.GET(f"/cards/{card_id}/attachments")

    async def get_attachment(self, card_id: str, attachment_id: str) -> Dict:
        """Retrieves a specific attachment on a card.

        Args:
            card_id (str): The ID of the card.
            attachment_id (str): The ID of the attachment.

        Returns:
            Dict: The attachment object.
        """
        return await self.client.GET(
            f"/cards/{card_id}/attachments/{attachment_id}"
        )

    async def delete_attachment(
        self, card_id: str, attachment_id: str
    ) -> Dict[str, Any]:
        """Removes an attachment from a card.

        Args:
            card_id (str): The ID of the card.
            attachment_id (str): The ID of the attachment to remove.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(
            f"/cards/{card_id}/attachments/{attachment_id}"
        )
