"""
This module contains tools for managing Trello custom fields.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.dtos.set_custom_field import SetCustomFieldPayload
from server.services.customfield import CustomFieldService
from server.trello import client

logger = logging.getLogger(__name__)

service = CustomFieldService(client)


async def get_board_custom_fields(ctx: Context, board_id: str) -> List[Dict]:
    """Retrieves the custom field definitions for a board.

    Args:
        board_id (str): The ID of the board.

    Returns:
        List[Dict]: A list of custom field definition objects.
    """
    try:
        logger.info(f"Getting custom fields for board: {board_id}")
        result = await service.get_board_custom_fields(board_id)
        logger.info(f"Successfully retrieved custom fields for board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get board custom fields: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_card_custom_field_items(ctx: Context, card_id: str) -> List[Dict]:
    """Retrieves the custom field values set on a card.

    Args:
        card_id (str): The ID of the card.

    Returns:
        List[Dict]: A list of custom field item objects.
    """
    try:
        logger.info(f"Getting custom field items for card: {card_id}")
        result = await service.get_card_custom_field_items(card_id)
        logger.info(f"Successfully retrieved custom field items for card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get card custom field items: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def set_card_custom_field(
    ctx: Context, card_id: str, field_id: str, payload: SetCustomFieldPayload
) -> Dict:
    """Sets (or clears) a custom field value on a card.

    For dropdown ("list") fields, provide ``idValue``. For other field types,
    provide exactly one typed value (text, number, checked, date). Provide no
    values to clear the field.

    Args:
        card_id (str): The ID of the card.
        field_id (str): The ID of the custom field.
        idValue (str): The ID of the dropdown option (for "list" custom fields).
        text (str): The value for a "text" custom field.

    Returns:
        Dict: The updated custom field item.
    """
    try:
        logger.info(f"Setting custom field {field_id} on card: {card_id}")
        result = await service.set_card_custom_field(
            card_id, field_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully set custom field {field_id} on card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to set card custom field: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
