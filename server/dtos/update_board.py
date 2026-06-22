from pydantic import BaseModel


class UpdateBoardPayload(BaseModel):
    """
    Payload for updating a board.

    Attributes:
        name (str): The new name of the board.
        desc (str): The new description of the board.
        closed (bool): Whether the board is closed (archived).
        subscribed (bool): Whether the authenticated member is subscribed to the board.
        idOrganization (str): The ID of the workspace/organization to move the board to.
    """

    name: str | None = None
    desc: str | None = None
    closed: bool | None = None
    subscribed: bool | None = None
    idOrganization: str | None = None
