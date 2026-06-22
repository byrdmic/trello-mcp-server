"""
Service for managing Trello organizations (workspaces) in MCP server.
"""

from typing import List

from server.models import TrelloOrganization
from server.utils.trello_api import TrelloClient


class OrganizationService:
    """
    Service class for managing Trello organizations (workspaces).
    """

    def __init__(self, client: TrelloClient):
        self.client = client

    async def get_organizations(
        self, member_id: str = "me"
    ) -> List[TrelloOrganization]:
        """Retrieves the organizations (workspaces) a member belongs to.

        Args:
            member_id (str): The ID or username of the member. Defaults to "me".

        Returns:
            List[TrelloOrganization]: A list of organization objects.
        """
        response = await self.client.GET(f"/members/{member_id}/organizations")
        return [TrelloOrganization(**org) for org in response]

    async def get_organization(self, org_id: str) -> TrelloOrganization:
        """Retrieves a specific organization (workspace) by ID.

        Args:
            org_id (str): The ID or name of the organization.

        Returns:
            TrelloOrganization: The organization object.
        """
        response = await self.client.GET(f"/organizations/{org_id}")
        return TrelloOrganization(**response)
