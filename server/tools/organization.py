"""
This module contains tools for managing Trello organizations (workspaces).
"""

import logging
from typing import List

from mcp.server.fastmcp import Context

from server.models import TrelloOrganization
from server.services.organization import OrganizationService
from server.trello import client

logger = logging.getLogger(__name__)

service = OrganizationService(client)


async def get_organizations(
    ctx: Context, member_id: str = "me"
) -> List[TrelloOrganization]:
    """Retrieves the organizations (workspaces) a member belongs to.

    Args:
        member_id (str): The ID or username of the member. Defaults to "me" for the
            authenticated user.

    Returns:
        List[TrelloOrganization]: A list of organization objects.
    """
    try:
        logger.info(f"Getting organizations for member: {member_id}")
        result = await service.get_organizations(member_id)
        logger.info(
            f"Successfully retrieved {len(result)} organizations for member: {member_id}"
        )
        return result
    except Exception as e:
        error_msg = f"Failed to get organizations: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_organization(ctx: Context, org_id: str) -> TrelloOrganization:
    """Retrieves a specific organization (workspace) by ID.

    Args:
        org_id (str): The ID or name of the organization.

    Returns:
        TrelloOrganization: The organization object.
    """
    try:
        logger.info(f"Getting organization: {org_id}")
        result = await service.get_organization(org_id)
        logger.info(f"Successfully retrieved organization: {org_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get organization: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
