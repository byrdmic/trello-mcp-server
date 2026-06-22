"""
This module contains tools for managing Trello boards, lists, and cards.
"""

from server.tools import (
    board,
    card,
    checklist,
    comment,
    customfield,
    label,
    list,
    member,
    notification,
    organization,
    search,
    webhook,
)


def register_tools(mcp):
    """Register tools with the MCP server."""
    # Board Tools
    mcp.add_tool(board.get_board)
    mcp.add_tool(board.get_boards)
    mcp.add_tool(board.get_board_labels)
    mcp.add_tool(board.create_board_label)
    mcp.add_tool(board.create_board)
    mcp.add_tool(board.update_board)
    mcp.add_tool(board.close_board)
    mcp.add_tool(board.delete_board)

    # List Tools
    mcp.add_tool(list.get_list)
    mcp.add_tool(list.get_lists)
    mcp.add_tool(list.create_list)
    mcp.add_tool(list.update_list)
    mcp.add_tool(list.delete_list)
    mcp.add_tool(list.move_list)
    mcp.add_tool(list.archive_all_cards)
    mcp.add_tool(list.move_all_cards)

    # Card Tools
    mcp.add_tool(card.get_card)
    mcp.add_tool(card.get_cards)
    mcp.add_tool(card.create_card)
    mcp.add_tool(card.update_card)
    mcp.add_tool(card.delete_card)
    mcp.add_tool(card.set_card_due)
    mcp.add_tool(card.set_card_due_complete)
    mcp.add_tool(card.move_card)
    mcp.add_tool(card.archive_card)
    mcp.add_tool(card.unarchive_card)
    mcp.add_tool(card.set_card_cover)
    mcp.add_tool(card.get_card_actions)
    mcp.add_tool(card.add_attachment)
    mcp.add_tool(card.get_attachments)
    mcp.add_tool(card.get_attachment)
    mcp.add_tool(card.delete_attachment)

    # Checklist Tools
    mcp.add_tool(checklist.get_checklist)
    mcp.add_tool(checklist.get_card_checklists)
    mcp.add_tool(checklist.create_checklist)
    mcp.add_tool(checklist.update_checklist)
    mcp.add_tool(checklist.delete_checklist)
    mcp.add_tool(checklist.add_checkitem)
    mcp.add_tool(checklist.update_checkitem)
    mcp.add_tool(checklist.delete_checkitem)

    # Comment Tools
    mcp.add_tool(comment.get_comments)
    mcp.add_tool(comment.add_comment)
    mcp.add_tool(comment.update_comment)
    mcp.add_tool(comment.delete_comment)

    # Member Tools
    mcp.add_tool(member.get_me)
    mcp.add_tool(member.get_member)
    mcp.add_tool(member.get_board_members)
    mcp.add_tool(member.add_card_member)
    mcp.add_tool(member.remove_card_member)

    # Label Tools
    mcp.add_tool(label.update_label)
    mcp.add_tool(label.delete_label)
    mcp.add_tool(label.add_card_label)
    mcp.add_tool(label.remove_card_label)
    mcp.add_tool(label.set_card_labels)

    # Search Tools
    mcp.add_tool(search.search)
    mcp.add_tool(search.search_members)

    # Custom Field Tools
    mcp.add_tool(customfield.get_board_custom_fields)
    mcp.add_tool(customfield.get_card_custom_field_items)
    mcp.add_tool(customfield.set_card_custom_field)

    # Webhook Tools
    mcp.add_tool(webhook.create_webhook)
    mcp.add_tool(webhook.get_webhooks)
    mcp.add_tool(webhook.get_webhook)
    mcp.add_tool(webhook.delete_webhook)

    # Organization (Workspace) Tools
    mcp.add_tool(organization.get_organizations)
    mcp.add_tool(organization.get_organization)

    # Notification Tools
    mcp.add_tool(notification.get_notifications)
    mcp.add_tool(notification.get_notification)
    mcp.add_tool(notification.mark_notification_read)
