from pydantic import BaseModel


class CreateCommentPayload(BaseModel):
    """
    Payload for adding a comment to a card.

    Attributes:
        text (str): The text content of the comment.
    """

    text: str
