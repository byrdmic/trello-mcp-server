from pydantic import BaseModel


class SetCardCoverPayload(BaseModel):
    """
    Payload for setting a card's cover.

    Provide either a ``color`` or an ``idAttachment`` (an existing card attachment
    to use as the cover image).

    Attributes:
        color (str): A cover color ("pink", "yellow", "lime", "blue", "black",
            "orange", "red", "purple", "sky", "green").
        idAttachment (str): The ID of a card attachment to use as the cover image.
        idUploadedBackground (str): The ID of an uploaded background to use as the cover.
        size (str): The cover size ("normal" or "full").
        brightness (str): The cover brightness ("light" or "dark").
    """

    color: str | None = None
    idAttachment: str | None = None
    idUploadedBackground: str | None = None
    size: str | None = None
    brightness: str | None = None
