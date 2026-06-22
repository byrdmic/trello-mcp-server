"""
This module contains tools for managing Trello labels and card-label associations.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.dtos.update_label import UpdateLabelPayload
from server.models import TrelloCard, TrelloLabel
from server.services.label import LabelService
from server.trello import client

logger = logging.getLogger(__name__)

service = LabelService(client)


async def update_label(
    ctx: Context, label_id: str, payload: UpdateLabelPayload
) -> TrelloLabel:
    """Updates a label's name and/or color.

    Args:
        label_id (str): The ID of the label to update.
        name (str): The new name of the label.
        color (str): The new color of the label.

    Returns:
        TrelloLabel: The updated label object.
    """
    try:
        logger.info(f"Updating label: {label_id}")
        result = await service.update_label(
            label_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully updated label: {label_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to update label: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_label(ctx: Context, label_id: str) -> Dict:
    """Deletes a label from its board.

    ⚠️ WARNING: This is irreversible and removes the label from every card that
    uses it across the board.

    Args:
        label_id (str): The ID of the label to delete.

    Returns:
        Dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting label: {label_id}")
        result = await service.delete_label(label_id)
        logger.info(f"Successfully deleted label: {label_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete label: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def add_card_label(ctx: Context, card_id: str, label_id: str) -> List[Dict]:
    """Adds an existing label to a card.

    Args:
        card_id (str): The ID of the card.
        label_id (str): The ID of the label to add.

    Returns:
        List[Dict]: The updated list of label IDs on the card.
    """
    try:
        logger.info(f"Adding label {label_id} to card: {card_id}")
        result = await service.add_card_label(card_id, label_id)
        logger.info(f"Successfully added label {label_id} to card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to add card label: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def remove_card_label(ctx: Context, card_id: str, label_id: str) -> Dict:
    """Removes a label from a card.

    Args:
        card_id (str): The ID of the card.
        label_id (str): The ID of the label to remove.

    Returns:
        Dict: The response from the remove operation.
    """
    try:
        logger.info(f"Removing label {label_id} from card: {card_id}")
        result = await service.remove_card_label(card_id, label_id)
        logger.info(f"Successfully removed label {label_id} from card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to remove card label: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def set_card_labels(ctx: Context, card_id: str, label_ids: str) -> TrelloCard:
    """Replaces the full set of labels on a card.

    Args:
        card_id (str): The ID of the card.
        label_ids (str): Comma-separated label IDs. Pass an empty string to clear all labels.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Setting labels on card: {card_id}")
        result = await service.set_card_labels(card_id, label_ids)
        logger.info(f"Successfully set labels on card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to set card labels: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
