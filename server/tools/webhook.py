"""
This module contains tools for managing Trello webhooks.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.dtos.create_webhook import CreateWebhookPayload
from server.services.webhook import WebhookService
from server.trello import client

logger = logging.getLogger(__name__)

service = WebhookService(client)


async def create_webhook(ctx: Context, payload: CreateWebhookPayload) -> Dict:
    """Creates a webhook that watches a Trello model for changes.

    ⚠️ NOTE: ``callbackURL`` must be publicly reachable; Trello validates it with a
    HEAD request at creation time and rejects the webhook if it does not respond.
    This MCP server does not receive the webhook events itself.

    Args:
        callbackURL (str): The URL Trello will POST events to.
        idModel (str): The ID of the model (board, list, card, member, ...) to watch.
        description (str): An optional description for the webhook.

    Returns:
        Dict: The created webhook object.
    """
    try:
        logger.info(f"Creating webhook for model: {payload.idModel}")
        result = await service.create_webhook(
            **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully created webhook for model: {payload.idModel}")
        return result
    except Exception as e:
        error_msg = f"Failed to create webhook: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_webhooks(ctx: Context) -> List[Dict]:
    """Retrieves all webhooks created with the configured token.

    Returns:
        List[Dict]: A list of webhook objects.
    """
    try:
        logger.info("Getting webhooks for token")
        result = await service.get_webhooks()
        logger.info(f"Successfully retrieved {len(result)} webhooks")
        return result
    except Exception as e:
        error_msg = f"Failed to get webhooks: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_webhook(ctx: Context, webhook_id: str) -> Dict:
    """Retrieves a specific webhook by ID.

    Args:
        webhook_id (str): The ID of the webhook.

    Returns:
        Dict: The webhook object.
    """
    try:
        logger.info(f"Getting webhook: {webhook_id}")
        result = await service.get_webhook(webhook_id)
        logger.info(f"Successfully retrieved webhook: {webhook_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get webhook: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_webhook(ctx: Context, webhook_id: str) -> Dict:
    """Deletes a webhook.

    ⚠️ WARNING: This is irreversible — the webhook is permanently removed and will
    stop delivering events.

    Args:
        webhook_id (str): The ID of the webhook to delete.

    Returns:
        Dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting webhook: {webhook_id}")
        result = await service.delete_webhook(webhook_id)
        logger.info(f"Successfully deleted webhook: {webhook_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete webhook: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
