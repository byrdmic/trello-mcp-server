from pydantic import BaseModel


class CreateWebhookPayload(BaseModel):
    """
    Payload for creating a webhook.

    Note: ``callbackURL`` must be publicly reachable; Trello validates it with a
    HEAD request when the webhook is created.

    Attributes:
        callbackURL (str): The URL Trello will POST events to.
        idModel (str): The ID of the model (board, list, card, member, ...) to watch.
        description (str): An optional description for the webhook.
        active (bool): Whether the webhook is active.
    """

    callbackURL: str
    idModel: str
    description: str | None = None
    active: bool | None = None
