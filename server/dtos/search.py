from pydantic import BaseModel


class SearchPayload(BaseModel):
    """
    Payload for searching across Trello.

    Attributes:
        query (str): The search query. Supports Trello's search operators.
        modelTypes (str): Comma-separated model types to search
            ("actions", "boards", "cards", "members", "organizations"). Defaults to "all".
        idBoards (str): "mine" or comma-separated board IDs to scope the search.
        idOrganizations (str): Comma-separated organization IDs to scope the search.
        idCards (str): Comma-separated card IDs to scope the search.
        board_fields (str): Comma-separated board fields to return.
        boards_limit (int): Maximum number of boards to return (max 1000).
        card_fields (str): Comma-separated card fields to return.
        cards_limit (int): Maximum number of cards to return (max 1000).
        cards_page (int): The page of card results to return (max 100).
        partial (bool): Whether to match partial words.
    """

    query: str
    modelTypes: str | None = None
    idBoards: str | None = None
    idOrganizations: str | None = None
    idCards: str | None = None
    board_fields: str | None = None
    boards_limit: int | None = None
    card_fields: str | None = None
    cards_limit: int | None = None
    cards_page: int | None = None
    partial: bool | None = None
