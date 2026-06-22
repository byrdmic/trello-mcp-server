"""
Service for managing Trello members in MCP server.
"""

from typing import Dict, List

from server.models import TrelloMember
from server.utils.trello_api import TrelloClient


class MemberService:
    """
    Service class for managing Trello members.
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_me(self) -> TrelloMember:
        """Retrieves the authenticated member.

        Returns:
            TrelloMember: The authenticated member's details.
        """
        response = await self.client.GET("/members/me")
        return TrelloMember(**response)

    async def get_member(self, member_id: str) -> TrelloMember:
        """Retrieves a specific member by ID or username.

        Args:
            member_id (str): The ID or username of the member to retrieve.

        Returns:
            TrelloMember: The member's details.
        """
        response = await self.client.GET(f"/members/{member_id}")
        return TrelloMember(**response)

    async def get_board_members(self, board_id: str) -> List[TrelloMember]:
        """Retrieves all members of a board.

        Args:
            board_id (str): The ID of the board whose members to retrieve.

        Returns:
            List[TrelloMember]: A list of member objects.
        """
        response = await self.client.GET(f"/boards/{board_id}/members")
        return [TrelloMember(**member) for member in response]

    async def add_card_member(self, card_id: str, member_id: str) -> List[Dict]:
        """Adds a member to a card.

        Args:
            card_id (str): The ID of the card.
            member_id (str): The ID of the member to add.

        Returns:
            List[Dict]: The updated list of members on the card.
        """
        return await self.client.POST(
            f"/cards/{card_id}/idMembers", data={"value": member_id}
        )

    async def remove_card_member(self, card_id: str, member_id: str) -> List[Dict]:
        """Removes a member from a card.

        Args:
            card_id (str): The ID of the card.
            member_id (str): The ID of the member to remove.

        Returns:
            List[Dict]: The updated list of members on the card.
        """
        return await self.client.DELETE(f"/cards/{card_id}/idMembers/{member_id}")
