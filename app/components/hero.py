import reflex as rx
from app.states.calculator_state import CalculatorState


def filter_chip(text: str, icon: str) -> rx.Component:
    """A chip component for filtering options."""
    return rx.el.button(
        rx.icon(icon, class_name="h-4 w-4 mr-2"),
        text,
        class_name="flex items-center bg-white/20 hover:bg-white/30 text-white font-medium text-sm px-3 py-1.5 rounded-lg transition-all duration-200 hover:scale-105 active:scale-95",
    )


def hero() -> rx.Component:
    """The hero section with the main search interface."""
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "Interactive Multi-Agent Tariff Simulator",
                class_name="text-4xl md:text-6xl font-bold text-white text-center tracking-tighter",
            ),
            rx.el.p(
                "Instantly calculate duties, taxes, and fees across multiple scenarios.",
                class_name="text-lg text-emerald-100 mt-4 max-w-2xl text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("search", class_name="h-5 w-5 text-gray-400"),
                        rx.el.input(
                            placeholder="Search by HTS code...",
                            default_value=CalculatorState.search_query,
                            on_change=CalculatorState.set_search_query,
                            on_key_up=CalculatorState.get_suggestions.debounce(200),
                            on_focus=CalculatorState.get_suggestions,
                            class_name="w-full bg-transparent focus:outline-none text-lg placeholder-gray-400",
                        ),
                        rx.el.kbd(
                            "⌘K",
                            class_name="hidden md:inline-flex items-center justify-center text-xs font-medium text-gray-400 border border-gray-200 rounded-md px-2 py-1",
                        ),
                        class_name="flex items-center gap-3 flex-1",
                    ),
                    rx.el.button(
                        "Search",
                        class_name="bg-emerald-500 hover:bg-emerald-600 text-white font-semibold px-6 py-3 rounded-xl transition-all duration-200 hover:scale-105 active:scale-95",
                    ),
                    class_name="flex items-center bg-white shadow-lg rounded-2xl p-2 w-full max-w-2xl",
                ),
                rx.cond(
                    CalculatorState.search_suggestions.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            CalculatorState.search_suggestions,
                            lambda suggestion: rx.el.button(
                                rx.el.div(
                                    rx.el.p(
                                        suggestion["code"], class_name="font-semibold"
                                    ),
                                    rx.el.p(
                                        suggestion["description"],
                                        class_name="text-sm text-gray-500",
                                    ),
                                ),
                                on_click=lambda: CalculatorState.select_suggestion(
                                    suggestion["code"]
                                ),
                                class_name="text-left w-full p-2 hover:bg-gray-50 rounded-md",
                            ),
                        ),
                        class_name="absolute mt-2 w-full max-w-2xl bg-white rounded-lg shadow-xl p-2 z-10 border border-gray-100",
                    ),
                ),
                class_name="relative flex flex-col items-center mt-10 w-full max-w-2xl",
            ),
            rx.el.div(
                filter_chip("Categories", "layout-grid"),
                filter_chip("Countries", "globe"),
                filter_chip("Date Range", "calendar-days"),
                rx.upload.root(
                    rx.el.button(
                        rx.icon("upload", class_name="h-4 w-4 mr-2"),
                        "Upload HTS Codes",
                        class_name="flex items-center text-emerald-100 hover:text-white font-medium text-sm px-3 py-1.5 rounded-lg transition-all duration-200 hover:scale-105 active:scale-95",
                    ),
                    id="upload-hts",
                    on_drop=CalculatorState.handle_upload(
                        rx.upload_files(upload_id="upload-hts")
                    ),
                ),
                class_name="flex flex-wrap items-center justify-center gap-4 mt-6",
            ),
            class_name="flex flex-col items-center w-full max-w-7xl mx-auto p-4",
        ),
        class_name="w-full flex items-center justify-center py-20 md:py-32 bg-gradient-to-br from-emerald-900 via-emerald-800 to-gray-900",
    )