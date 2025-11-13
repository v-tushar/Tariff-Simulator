import reflex as rx
from app.states.main_state import MainState


def nav_link(link: dict) -> rx.Component:
    return rx.el.a(
        link["name"],
        href=link["href"],
        class_name=rx.cond(
            MainState.active_page == link["name"],
            "text-gray-900 font-semibold",
            "text-gray-600 font-medium hover:text-gray-900 transition-colors",
        ),
    )


def header() -> rx.Component:
    """The navigation header for the app."""
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("landmark", class_name="h-6 w-6 text-emerald-500"),
                    rx.el.span(
                        "TariffSim", class_name="text-xl font-bold text-gray-900"
                    ),
                    class_name="flex items-center gap-2",
                ),
                href="/",
                class_name="transition-transform hover:scale-105",
            ),
            rx.el.nav(
                rx.foreach(MainState.nav_links, nav_link),
                class_name="hidden md:flex items-center gap-8 text-sm",
            ),
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6 text-gray-600"),
                class_name="md:hidden p-2 rounded-md hover:bg-gray-100 transition-colors",
            ),
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto p-4",
        ),
        class_name="w-full bg-white/80 backdrop-blur-md border-b border-gray-200 sticky top-0 z-50",
    )