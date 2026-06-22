"""
This module contains tools for managing Trello notifications.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.services.notification import NotificationService
from server.trello import client

logger = logging.getLogger(__name__)

service = NotificationService(client)


async def get_notifications(
    ctx: Context, filter: str = "all", read_filter: str = "all"
) -> List[Dict]:
    """Retrieves the authenticated member's notifications.

    Args:
        filter (str): Comma-separated notification types to include, or "all".
        read_filter (str): Which notifications to return: "all", "read", or "unread".

    Returns:
        List[Dict]: A list of notification objects.
    """
    try:
        logger.info(f"Getting notifications (read_filter={read_filter})")
        result = await service.get_notifications(filter, read_filter)
        logger.info(f"Successfully retrieved {len(result)} notifications")
        return result
    except Exception as e:
        error_msg = f"Failed to get notifications: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_notification(ctx: Context, notification_id: str) -> Dict:
    """Retrieves a specific notification by ID.

    Args:
        notification_id (str): The ID of the notification.

    Returns:
        Dict: The notification object.
    """
    try:
        logger.info(f"Getting notification: {notification_id}")
        result = await service.get_notification(notification_id)
        logger.info(f"Successfully retrieved notification: {notification_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get notification: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def mark_notification_read(
    ctx: Context, notification_id: str, unread: bool = False
) -> Dict:
    """Marks a notification as read or unread.

    Args:
        notification_id (str): The ID of the notification.
        unread (bool): Set True to mark the notification unread, False to mark it read.

    Returns:
        Dict: The updated notification object.
    """
    try:
        logger.info(f"Marking notification {notification_id} unread={unread}")
        result = await service.mark_notification_read(notification_id, unread)
        logger.info(f"Successfully updated notification: {notification_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to mark notification: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
