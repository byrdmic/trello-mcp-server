"""
This module contains tools for searching across Trello.
"""

import logging
from typing import Dict, List

from mcp.server.fastmcp import Context

from server.dtos.search import SearchPayload
from server.services.search import SearchService
from server.trello import client

logger = logging.getLogger(__name__)

service = SearchService(client)


async def search(ctx: Context, payload: SearchPayload) -> Dict:
    """Searches across Trello cards, boards, organizations, and members.

    Use ``modelTypes`` to limit which kinds of objects are searched, and
    ``idBoards`` / ``idOrganizations`` / ``idCards`` to scope the search. The
    query supports Trello's search operators (e.g. "board:", "label:", "due:").

    Args:
        query (str): The search query.
        modelTypes (str): Comma-separated model types to search.
        idBoards (str): "mine" or comma-separated board IDs to scope the search.

    Returns:
        Dict: The search results, keyed by model type (cards, boards, ...).
    """
    try:
        logger.info(f"Searching Trello with query: {payload.query}")
        result = await service.search(**payload.model_dump(exclude_unset=True))
        logger.info("Successfully completed search")
        return result
    except Exception as e:
        error_msg = f"Failed to search: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def search_members(ctx: Context, query: str, limit: int = 8) -> List[Dict]:
    """Searches for members by name or username.

    Args:
        query (str): The search query.
        limit (int): The maximum number of members to return (1-20). Defaults to 8.

    Returns:
        List[Dict]: A list of matching member objects.
    """
    try:
        logger.info(f"Searching members with query: {query}")
        result = await service.search_members(query, limit)
        logger.info(f"Successfully retrieved {len(result)} members")
        return result
    except Exception as e:
        error_msg = f"Failed to search members: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
