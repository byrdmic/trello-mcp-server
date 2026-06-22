"""
This module contains tools for managing Trello members.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.models import TrelloMember
from server.services.member import MemberService
from server.trello import client

logger = logging.getLogger(__name__)

service = MemberService(client)


async def get_me(ctx: Context) -> TrelloMember:
    """Retrieves the authenticated member (the owner of the configured token).

    Returns:
        TrelloMember: The authenticated member's details.
    """
    try:
        logger.info("Getting authenticated member")
        result = await service.get_me()
        logger.info("Successfully retrieved authenticated member")
        return result
    except Exception as e:
        error_msg = f"Failed to get authenticated member: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_member(ctx: Context, member_id: str) -> TrelloMember:
    """Retrieves a specific member by ID or username.

    Args:
        member_id (str): The ID or username of the member to retrieve.

    Returns:
        TrelloMember: The member's details.
    """
    try:
        logger.info(f"Getting member: {member_id}")
        result = await service.get_member(member_id)
        logger.info(f"Successfully retrieved member: {member_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get member: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_board_members(ctx: Context, board_id: str) -> List[TrelloMember]:
    """Retrieves all members of a board.

    Args:
        board_id (str): The ID of the board whose members to retrieve.

    Returns:
        List[TrelloMember]: A list of member objects.
    """
    try:
        logger.info(f"Getting members for board: {board_id}")
        result = await service.get_board_members(board_id)
        logger.info(
            f"Successfully retrieved {len(result)} members for board: {board_id}"
        )
        return result
    except Exception as e:
        error_msg = f"Failed to get board members: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def add_card_member(ctx: Context, card_id: str, member_id: str) -> List[Dict]:
    """Adds a member to a card.

    Args:
        card_id (str): The ID of the card.
        member_id (str): The ID of the member to add.

    Returns:
        List[Dict]: The updated list of members on the card.
    """
    try:
        logger.info(f"Adding member {member_id} to card: {card_id}")
        result = await service.add_card_member(card_id, member_id)
        logger.info(f"Successfully added member {member_id} to card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to add card member: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def remove_card_member(ctx: Context, card_id: str, member_id: str) -> List[Dict]:
    """Removes a member from a card.

    Args:
        card_id (str): The ID of the card.
        member_id (str): The ID of the member to remove.

    Returns:
        List[Dict]: The updated list of members on the card.
    """
    try:
        logger.info(f"Removing member {member_id} from card: {card_id}")
        result = await service.remove_card_member(card_id, member_id)
        logger.info(f"Successfully removed member {member_id} from card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to remove card member: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
