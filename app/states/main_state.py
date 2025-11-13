import reflex as rx
from typing import TypedDict


class NavLink(TypedDict):
    name: str
    href: str


class MainState(rx.State):
    """The main state for the application."""

    nav_links: list[NavLink] = [
        {"name": "Simulator", "href": "/"},
        {"name": "Catalog", "href": "#"},
        {"name": "FAQ", "href": "#"},
    ]
    active_page: str = "Simulator"
    show_cmd_k_modal: bool = False

    @rx.event
    def toggle_cmd_k_modal(self):
        self.show_cmd_k_modal = not self.show_cmd_k_modal

    @rx.event
    def on_load_event(self):
        return rx.console_log("Cmd+K shortcut is active.")