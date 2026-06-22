from pydantic import BaseModel


class SetCustomFieldPayload(BaseModel):
    """
    Payload for setting a custom field value on a card.

    For dropdown ("list") fields, provide ``idValue`` (the ID of the dropdown
    option). For all other field types, provide exactly one of the typed value
    fields. Provide no values to clear the field.

    Attributes:
        idValue (str): The ID of the dropdown option (for "list" custom fields).
        text (str): The value for a "text" custom field.
        number (str): The value for a "number" custom field.
        checked (bool): The value for a "checkbox" custom field.
        date (str): The value for a "date" custom field (ISO 8601 format).
    """

    idValue: str | None = None
    text: str | None = None
    number: str | None = None
    checked: bool | None = None
    date: str | None = None
