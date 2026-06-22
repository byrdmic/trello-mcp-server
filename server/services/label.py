"""
Service for managing Trello labels in MCP server.
"""

from typing import Any, Dict, List

from server.models import TrelloCard, TrelloLabel
from server.utils.trello_api import TrelloClient


class LabelService:
    """
    Service class for managing Trello labels and card-label associations.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def update_label(self, label_id: str, **kwargs) -> TrelloLabel:
        """Updates a label's name and/or color.

        Args:
            label_id (str): The ID of the label to update.
            **kwargs: The label attributes to update (name, color).

        Returns:
            TrelloLabel: The updated label object.
        """
        response = await self.client.PUT(f"/labels/{label_id}", data=kwargs)
        return TrelloLabel(**response)

    async def delete_label(self, label_id: str) -> Dict[str, Any]:
        """Deletes a label from its board.

        Args:
            label_id (str): The ID of the label to delete.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(f"/labels/{label_id}")

    async def add_card_label(self, card_id: str, label_id: str) -> List[Dict]:
        """Adds an existing label to a card.

        Args:
            card_id (str): The ID of the card.
            label_id (str): The ID of the label to add.

        Returns:
            List[Dict]: The updated list of label IDs on the card.
        """
        return await self.client.POST(
            f"/cards/{card_id}/idLabels", data={"value": label_id}
        )

    async def remove_card_label(self, card_id: str, label_id: str) -> Dict[str, Any]:
        """Removes a label from a card.

        Args:
            card_id (str): The ID of the card.
            label_id (str): The ID of the label to remove.

        Returns:
            Dict[str, Any]: The response from the remove operation.
        """
        return await self.client.DELETE(f"/cards/{card_id}/idLabels/{label_id}")

    async def set_card_labels(self, card_id: str, label_ids: str) -> TrelloCard:
        """Replaces the full set of labels on a card.

        Args:
            card_id (str): The ID of the card.
            label_ids (str): Comma-separated label IDs (empty string clears all labels).

        Returns:
            TrelloCard: The updated card object.
        """
        response = await self.client.PUT(
            f"/cards/{card_id}", data={"idLabels": label_ids}
        )
        return TrelloCard(**response)
