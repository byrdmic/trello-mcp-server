import logging
import os

from dotenv import load_dotenv

from server.utils.trello_api import TrelloClient

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


# Initialize Trello client and service
try:
    api_key = os.getenv("TRELLO_API_KEY")
    token = os.getenv("TRELLO_TOKEN")
    if not api_key or not token:
        raise ValueError(
            "TRELLO_API_KEY and TRELLO_TOKEN must be set in environment variables"
        )
    client = TrelloClient(api_key=api_key, token=token)
    logger.info("Trello client and service initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Trello client: {str(e)}")
    raise


# Add a prompt for common Trello operations
def trello_help() -> str:
    """Provides help information about available Trello operations."""
    return """
    Available Trello Operations:
    1. Board Operations:
       - Get a specific board / list all boards
       - Get board labels / add a label to a board
       - Create, update, close (archive), or delete a board
    2. List Operations:
       - Get a specific list / list all lists in a board
       - Create, update (rename), or archive a list
       - Move a list / archive all cards in a list / move all cards to another list
    3. Card Operations:
       - Get a specific card / list all cards in a list
       - Create, update, or delete a card
       - Set/clear due date, set due complete, move, archive/unarchive a card
       - Set a card cover / get a card's action history
       - Add (URL), list, get, or remove card attachments
    4. Checklist Operations:
       - Get a checklist / list checklists in a card
       - Create, update, or delete a checklist
       - Add, update, or delete a checkitem
    5. Comment Operations:
       - List, add, update, or delete card comments
    6. Member Operations:
       - Get the authenticated member / get a member / get board members
       - Add or remove a member on a card
    7. Label Operations:
       - Update or delete a board label
       - Add, remove, or set the labels on a card
    8. Search:
       - Search across cards, boards, members, and organizations
       - Search for members
    9. Custom Fields:
       - Get a board's custom fields / a card's custom field values
       - Set a card's custom field value
    10. Webhooks:
       - Create, list, get, or delete webhooks
    11. Organizations (Workspaces):
       - List a member's workspaces / get a workspace
    12. Notifications:
       - List notifications / get a notification / mark read or unread
    """
