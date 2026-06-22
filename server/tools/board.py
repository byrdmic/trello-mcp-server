"""
This module contains tools for managing Trello boards.
"""

import logging
from typing import List

from mcp.server.fastmcp import Context

from server.models import TrelloBoard, TrelloLabel
from server.dtos.create_label import CreateLabelPayload
from server.dtos.create_board import CreateBoardPayload
from server.dtos.update_board import UpdateBoardPayload
from server.services.board import BoardService
from server.trello import client

logger = logging.getLogger(__name__)

service = BoardService(client)


async def get_board(ctx: Context, board_id: str) -> TrelloBoard:
    """Retrieves a specific board by its ID.

    Args:
        board_id (str): The ID of the board to retrieve.

    Returns:
        TrelloBoard: The board object containing board details.
    """
    try:
        logger.info(f"Getting board with ID: {board_id}")
        result = await service.get_board(board_id)
        logger.info(f"Successfully retrieved board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get board: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_boards(ctx: Context) -> List[TrelloBoard]:
    """Retrieves all boards for the authenticated user.

    Returns:
        List[TrelloBoard]: A list of board objects.
    """
    try:
        logger.info("Getting all boards")
        result = await service.get_boards()
        logger.info(f"Successfully retrieved {len(result)} boards")
        return result
    except Exception as e:
        error_msg = f"Failed to get boards: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_board_labels(ctx: Context, board_id: str) -> List[TrelloLabel]:
    """Retrieves all labels for a specific board.

    Args:
        board_id (str): The ID of the board whose labels to retrieve.

    Returns:
        List[TrelloLabel]: A list of label objects for the board.
    """
    try:
        logger.info(f"Getting labels for board: {board_id}")
        result = await service.get_board_labels(board_id)
        logger.info(f"Successfully retrieved {len(result)} labels for board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get board labels: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def create_board_label(ctx: Context, board_id: str, payload: CreateLabelPayload) -> TrelloLabel:
    """Create label for a specific board.

    Args:
        board_id (str): The ID of the board whose to add label to.
        name (str): The name of the label.
        color (str): The color of the label.

    Returns:
        TrelloLabel: A label object for the board.
    """
    try:
        logger.info(f"Creating label {payload.name} label for board: {board_id}")
        result = await service.create_board_label(board_id, **payload.model_dump(exclude_unset=True))
        logger.info(f"Successfully created label {payload.name} labels for board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get board labels: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def create_board(ctx: Context, payload: CreateBoardPayload) -> TrelloBoard:
    """Creates a new board.

    Args:
        name (str): The name of the board.
        desc (str): The description of the board.
        idOrganization (str): The ID of the workspace the board belongs to.

    Returns:
        TrelloBoard: The newly created board object.
    """
    try:
        logger.info(f"Creating board with name: {payload.name}")
        result = await service.create_board(**payload.model_dump(exclude_unset=True))
        logger.info(f"Successfully created board: {payload.name}")
        return result
    except Exception as e:
        error_msg = f"Failed to create board: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def update_board(
    ctx: Context, board_id: str, payload: UpdateBoardPayload
) -> TrelloBoard:
    """Updates a board's attributes.

    Args:
        board_id (str): The ID of the board to update.
        name (str): The new name of the board.
        desc (str): The new description of the board.

    Returns:
        TrelloBoard: The updated board object.
    """
    try:
        logger.info(f"Updating board: {board_id}")
        result = await service.update_board(
            board_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully updated board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to update board: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def close_board(ctx: Context, board_id: str) -> TrelloBoard:
    """Closes (archives) a board. This is reversible by reopening the board.

    Args:
        board_id (str): The ID of the board to close.

    Returns:
        TrelloBoard: The closed board object.
    """
    try:
        logger.info(f"Closing board: {board_id}")
        result = await service.close_board(board_id)
        logger.info(f"Successfully closed board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to close board: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_board(ctx: Context, board_id: str) -> dict:
    """Permanently deletes a board.

    ⚠️ WARNING: This is irreversible. Deleting a board permanently removes the
    board and all of its lists and cards. Prefer ``close_board`` to archive instead.

    Args:
        board_id (str): The ID of the board to delete.

    Returns:
        dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting board: {board_id}")
        result = await service.delete_board(board_id)
        logger.info(f"Successfully deleted board: {board_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete board: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise

