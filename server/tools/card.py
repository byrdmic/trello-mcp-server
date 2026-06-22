"""
This module contains tools for managing Trello cards.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.models import TrelloCard
from server.services.card import CardService
from server.trello import client
from server.dtos.update_card import UpdateCardPayload
from server.dtos.create_card import CreateCardPayload
from server.dtos.set_card_cover import SetCardCoverPayload
from server.dtos.create_attachment import CreateAttachmentPayload

logger = logging.getLogger(__name__)

service = CardService(client)


async def get_card(ctx: Context, card_id: str) -> TrelloCard:
    """Retrieves a specific card by its ID.

    Args:
        card_id (str): The ID of the card to retrieve.

    Returns:
        TrelloCard: The card object containing card details.
    """
    try:
        logger.info(f"Getting card with ID: {card_id}")
        result = await service.get_card(card_id)
        logger.info(f"Successfully retrieved card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_cards(ctx: Context, list_id: str) -> List[TrelloCard]:
    """Retrieves all cards in a given list.

    Args:
        list_id (str): The ID of the list whose cards to retrieve.

    Returns:
        List[TrelloCard]: A list of card objects.
    """
    try:
        logger.info(f"Getting cards for list: {list_id}")
        result = await service.get_cards(list_id)
        logger.info(f"Successfully retrieved {len(result)} cards for list: {list_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get cards: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def create_card(ctx: Context, payload: CreateCardPayload) -> TrelloCard:
    """Creates a new card in a given list.

    Args:
        list_id (str): The ID of the list to create the card in.
        name (str): The name of the new card.
        desc (str, optional): The description of the new card. Defaults to None.

    Returns:
        TrelloCard: The newly created card object.
    """
    try:
        logger.info(f"Creating card in list {payload.idList} with name: {payload.name}")
        result = await service.create_card(**payload.model_dump(exclude_unset=True))
        logger.info(f"Successfully created card in list: {payload.idList}")
        return result
    except Exception as e:
        error_msg = f"Failed to create card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def update_card(
    ctx: Context, card_id: str, payload: UpdateCardPayload
) -> TrelloCard:
    """Updates a card's attributes.

    Args:
        card_id (str): The ID of the card to update.
        **kwargs: Keyword arguments representing the attributes to update on the card.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Updating card: {card_id} with payload: {payload}")
        result = await service.update_card(
            card_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully updated card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to update card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_card(ctx: Context, card_id: str) -> dict:
    """Deletes a card.

    Args:
        card_id (str): The ID of the card to delete.

    Returns:
        dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting card: {card_id}")
        result = await service.delete_card(card_id)
        logger.info(f"Successfully deleted card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def set_card_due(ctx: Context, card_id: str, due: str | None = None) -> TrelloCard:
    """Sets or clears a card's due date.

    Args:
        card_id (str): The ID of the card.
        due (str | None): An ISO 8601 datetime (e.g. "2026-07-01T17:00:00Z") to set
            the due date, or omit/null to clear it.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Setting due date on card {card_id}: {due}")
        result = await service.set_due(card_id, due)
        logger.info(f"Successfully set due date on card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to set card due date: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def set_card_due_complete(ctx: Context, card_id: str, value: bool) -> TrelloCard:
    """Marks a card's due date as complete or incomplete.

    Args:
        card_id (str): The ID of the card.
        value (bool): Whether the due date is complete.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Setting dueComplete on card {card_id}: {value}")
        result = await service.set_due_complete(card_id, value)
        logger.info(f"Successfully set dueComplete on card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to set card due complete: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def move_card(
    ctx: Context, card_id: str, list_id: str, pos: str = "bottom"
) -> TrelloCard:
    """Moves a card to a list and/or position.

    Args:
        card_id (str): The ID of the card to move.
        list_id (str): The ID of the destination list.
        pos (str): The position in the list ("top", "bottom", or a number). Defaults to "bottom".

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Moving card {card_id} to list {list_id} at pos {pos}")
        result = await service.move_card(card_id, list_id, pos)
        logger.info(f"Successfully moved card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to move card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def archive_card(ctx: Context, card_id: str) -> TrelloCard:
    """Archives a card (sets closed=true). Reversible with ``unarchive_card``.

    Args:
        card_id (str): The ID of the card to archive.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Archiving card: {card_id}")
        result = await service.set_closed(card_id, True)
        logger.info(f"Successfully archived card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to archive card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def unarchive_card(ctx: Context, card_id: str) -> TrelloCard:
    """Unarchives a card (sets closed=false), returning it to its board.

    Args:
        card_id (str): The ID of the card to unarchive.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Unarchiving card: {card_id}")
        result = await service.set_closed(card_id, False)
        logger.info(f"Successfully unarchived card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to unarchive card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def set_card_cover(
    ctx: Context, card_id: str, payload: SetCardCoverPayload
) -> TrelloCard:
    """Sets a card's cover (a color or an existing attachment).

    Args:
        card_id (str): The ID of the card.
        color (str): A cover color.
        idAttachment (str): The ID of a card attachment to use as the cover image.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Setting cover on card: {card_id}")
        result = await service.set_cover(
            card_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully set cover on card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to set card cover: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_card_actions(
    ctx: Context, card_id: str, filter: str | None = None
) -> List[Dict]:
    """Retrieves the action (activity) history of a card.

    Args:
        card_id (str): The ID of the card.
        filter (str | None): Comma-separated action types to include (e.g. "updateCard,commentCard").

    Returns:
        List[Dict]: A list of action objects.
    """
    try:
        logger.info(f"Getting actions for card: {card_id}")
        result = await service.get_actions(card_id, filter)
        logger.info(f"Successfully retrieved actions for card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get card actions: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def add_attachment(
    ctx: Context, card_id: str, payload: CreateAttachmentPayload
) -> Dict:
    """Adds a URL attachment to a card.

    Note: Only URL-based attachments are supported (uploading a local file is not).

    Args:
        card_id (str): The ID of the card.
        url (str): The URL to attach.
        name (str): An optional display name for the attachment.

    Returns:
        Dict: The created attachment object.
    """
    try:
        logger.info(f"Adding attachment to card: {card_id}")
        result = await service.add_attachment(
            card_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully added attachment to card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to add attachment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_attachments(ctx: Context, card_id: str) -> List[Dict]:
    """Retrieves all attachments on a card.

    Args:
        card_id (str): The ID of the card.

    Returns:
        List[Dict]: A list of attachment objects.
    """
    try:
        logger.info(f"Getting attachments for card: {card_id}")
        result = await service.get_attachments(card_id)
        logger.info(f"Successfully retrieved attachments for card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get attachments: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_attachment(ctx: Context, card_id: str, attachment_id: str) -> Dict:
    """Retrieves a specific attachment on a card.

    Args:
        card_id (str): The ID of the card.
        attachment_id (str): The ID of the attachment.

    Returns:
        Dict: The attachment object.
    """
    try:
        logger.info(f"Getting attachment {attachment_id} for card: {card_id}")
        result = await service.get_attachment(card_id, attachment_id)
        logger.info(f"Successfully retrieved attachment: {attachment_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get attachment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_attachment(ctx: Context, card_id: str, attachment_id: str) -> Dict:
    """Removes an attachment from a card.

    ⚠️ WARNING: This is irreversible — the attachment is permanently removed.

    Args:
        card_id (str): The ID of the card.
        attachment_id (str): The ID of the attachment to remove.

    Returns:
        Dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting attachment {attachment_id} from card: {card_id}")
        result = await service.delete_attachment(card_id, attachment_id)
        logger.info(f"Successfully deleted attachment: {attachment_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete attachment: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
