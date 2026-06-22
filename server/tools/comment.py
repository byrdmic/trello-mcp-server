"""
This module contains tools for managing Trello card comments.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.dtos.create_comment import CreateCommentPayload
from server.dtos.update_comment import UpdateCommentPayload
from server.services.comment import CommentService
from server.trello import client

logger = logging.getLogger(__name__)

service = CommentService(client)


async def get_comments(ctx: Context, card_id: str) -> List[Dict]:
    """Retrieves all comments on a card.

    Args:
        card_id (str): The ID of the card whose comments to retrieve.

    Returns:
        List[Dict]: A list of comment action objects.
    """
    try:
        logger.info(f"Getting comments for card: {card_id}")
        result = await service.get_comments(card_id)
        logger.info(f"Successfully retrieved comments for card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get comments: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def add_comment(
    ctx: Context, card_id: str, payload: CreateCommentPayload
) -> Dict:
    """Adds a comment to a card.

    Args:
        card_id (str): The ID of the card to comment on.
        text (str): The text content of the comment.

    Returns:
        Dict: The created comment action object.
    """
    try:
        logger.info(f"Adding comment to card: {card_id}")
        result = await service.add_comment(card_id, payload.text)
        logger.info(f"Successfully added comment to card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to add comment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def update_comment(
    ctx: Context, action_id: str, payload: UpdateCommentPayload
) -> Dict:
    """Updates an existing comment.

    Args:
        action_id (str): The ID of the comment action to update.
        text (str): The new text content of the comment.

    Returns:
        Dict: The updated comment action object.
    """
    try:
        logger.info(f"Updating comment: {action_id}")
        result = await service.update_comment(action_id, payload.text)
        logger.info(f"Successfully updated comment: {action_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to update comment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_comment(ctx: Context, action_id: str) -> Dict:
    """Deletes a comment.

    ⚠️ WARNING: This is irreversible — the comment is permanently removed.

    Args:
        action_id (str): The ID of the comment action to delete.

    Returns:
        Dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting comment: {action_id}")
        result = await service.delete_comment(action_id)
        logger.info(f"Successfully deleted comment: {action_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete comment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
