"""
Service for managing Trello notifications in MCP server.
"""

from typing import Dict, List

from server.utils.trello_api import TrelloClient


class NotificationService:
    """
    Service class for managing Trello notifications.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_notifications(
        self, filter: str = "all", read_filter: str = "all"
    ) -> List[Dict]:
        """Retrieves the authenticated member's notifications.

        Args:
            filter (str): Comma-separated notification types to include, or "all".
            read_filter (str): Which notifications to return: "all", "read", or "unread".

        Returns:
            List[Dict]: A list of notification objects.
        """
        return await self.client.GET(
            "/members/me/notifications",
            params={"filter": filter, "read_filter": read_filter},
        )

    async def get_notification(self, notification_id: str) -> Dict:
        """Retrieves a specific notification by ID.

        Args:
            notification_id (str): The ID of the notification.

        Returns:
            Dict: The notification object.
        """
        return await self.client.GET(f"/notifications/{notification_id}")

    async def mark_notification_read(
        self, notification_id: str, unread: bool = False
    ) -> Dict:
        """Marks a notification as read or unread.

        Args:
            notification_id (str): The ID of the notification.
            unread (bool): Set True to mark the notification unread, False to mark it read.

        Returns:
            Dict: The updated notification object.
        """
        return await self.client.PUT(
            f"/notifications/{notification_id}/unread",
            data={"value": "true" if unread else "false"},
        )
