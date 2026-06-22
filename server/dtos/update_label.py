from pydantic import BaseModel


class UpdateLabelPayload(BaseModel):
    """
    Payload for updating a label.

    Attributes:
        name (str): The new name of the label.
        color (str): The new color of the label (or None to remove the color).
    """

    name: str | None = None
    color: str | None = None
