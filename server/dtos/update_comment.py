from pydantic import BaseModel


class UpdateCommentPayload(BaseModel):
    """
    Payload for updating a comment.

    Attributes:
        text (str): The new text content of the comment.
    """

    text: str
