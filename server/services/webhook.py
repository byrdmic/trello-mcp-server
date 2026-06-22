"""
Service for managing Trello webhooks in MCP server.
"""

from typing import Any, Dict, List

from server.utils.trello_api import TrelloClient


class WebhookService:
    """
    Service class for managing Trello webhooks.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def create_webhook(self, **kwargs) -> Dict:
        """Creates a webhook.

        Args:
            **kwargs: Webhook attributes (callbackURL, idModel, description, active).

        Returns:
            Dict: The created webhook object.
        """
        return await self.client.POST("/webhooks", data=kwargs)

    async def get_webhooks(self) -> List[Dict]:
        """Retrieves all webhooks created with the configured token.

        Returns:
            List[Dict]: A list of webhook objects.
        """
        return await self.client.GET(f"/tokens/{self.client.token}/webhooks")

    async def get_webhook(self, webhook_id: str) -> Dict:
        """Retrieves a specific webhook by ID.

        Args:
            webhook_id (str): The ID of the webhook.

        Returns:
            Dict: The webhook object.
        """
        return await self.client.GET(f"/webhooks/{webhook_id}")

    async def delete_webhook(self, webhook_id: str) -> Dict[str, Any]:
        """Deletes a webhook.

        Args:
            webhook_id (str): The ID of the webhook to delete.

        Returns:
            Dict[str, Any]: The response from the delete operation.
        """
        return await self.client.DELETE(f"/webhooks/{webhook_id}")
