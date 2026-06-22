from pydantic import BaseModel


class CreateAttachmentPayload(BaseModel):
    """
    Payload for adding a URL attachment to a card.

    Note: Only URL-based attachments are supported. Uploading a local file
    (multipart/form-data) is not supported by this server.

    Attributes:
        url (str): The URL to attach to the card.
        name (str): An optional display name for the attachment.
        mimeType (str): An optional MIME type for the attachment.
    """

    url: str
    name: str | None = None
    mimeType: str | None = None
