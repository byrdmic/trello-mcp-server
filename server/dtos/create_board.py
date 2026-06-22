from pydantic import BaseModel


class CreateBoardPayload(BaseModel):
    """
    Payload for creating a board.

    Attributes:
        name (str): The name of the board.
        desc (str): The description of the board.
        idOrganization (str): The ID of the workspace/organization the board belongs to.
        defaultLabels (bool): Whether to use the default set of labels.
        defaultLists (bool): Whether to add the default lists (To Do, Doing, Done).
        idBoardSource (str): The ID of a board to copy into the new board.
        keepFromSource (str): Which properties to copy from idBoardSource ("cards" or "none").
        prefs_permissionLevel (str): The permission level ("private", "org", "public").
        prefs_background (str): The board background (a color name or background ID).
    """

    name: str
    desc: str | None = None
    idOrganization: str | None = None
    defaultLabels: bool | None = None
    defaultLists: bool | None = None
    idBoardSource: str | None = None
    keepFromSource: str | None = None
    prefs_permissionLevel: str | None = None
    prefs_background: str | None = None
