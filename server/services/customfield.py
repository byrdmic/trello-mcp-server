"""
Service for managing Trello custom fields in MCP server.
"""

from typing import Dict, List

from server.utils.trello_api import TrelloClient


class CustomFieldService:
    """
    Service class for managing Trello custom fields.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_board_custom_fields(self, board_id: str) -> List[Dict]:
        """Retrieves the custom field definitions for a board.

        Args:
            board_id (str): The ID of the board.

        Returns:
            List[Dict]: A list of custom field definition objects.
        """
        return await self.client.GET(f"/boards/{board_id}/customFields")

    async def get_card_custom_field_items(self, card_id: str) -> List[Dict]:
        """Retrieves the custom field values set on a card.

        Args:
            card_id (str): The ID of the card.

        Returns:
            List[Dict]: A list of custom field item objects.
        """
        return await self.client.GET(f"/cards/{card_id}/customFieldItems")

    async def set_card_custom_field(
        self, card_id: str, field_id: str, **kwargs
    ) -> Dict:
        """Sets (or clears) a custom field value on a card.

        Args:
            card_id (str): The ID of the card.
            field_id (str): The ID of the custom field.
            **kwargs: Either ``idValue`` for dropdown fields, or one typed value
                (text, number, checked, date) for other field types. Pass no
                values to clear the field.

        Returns:
            Dict: The updated custom field item.
        """
        id_value = kwargs.get("idValue")
        if id_value is not None:
            body = {"idValue": id_value}
        else:
            value: Dict[str, str] = {}
            if kwargs.get("text") is not None:
                value["text"] = kwargs["text"]
            if kwargs.get("number") is not None:
                value["number"] = str(kwargs["number"])
            if kwargs.get("checked") is not None:
                value["checked"] = "true" if kwargs["checked"] else "false"
            if kwargs.get("date") is not None:
                value["date"] = kwargs["date"]
            body = {"value": value}
        return await self.client.PUT(
            f"/cards/{card_id}/customField/{field_id}/item", data=body
        )
