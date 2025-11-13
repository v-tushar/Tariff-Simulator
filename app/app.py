import reflex as rx
from app.components.header import header
from app.components.hero import hero
from app.components.calculator_form import calculator_form
from app.components.results_panel import results_panel
from app.components.advanced_visualizations import advanced_visualizations
from app.states.calculator_state import CalculatorState


def skeleton_loader() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="h-24 bg-gray-200 rounded-lg w-full"),
            rx.el.div(class_name="h-24 bg-gray-200 rounded-lg w-full"),
            rx.el.div(class_name="h-24 bg-gray-200 rounded-lg w-full"),
            rx.el.div(class_name="h-24 bg-gray-200 rounded-lg w-full"),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6 bg-gray-100 rounded-t-2xl border-b border-gray-200",
        ),
        rx.el.div(
            rx.el.div(class_name="h-64 bg-gray-200 rounded-lg w-full lg:col-span-2"),
            rx.el.div(class_name="h-64 bg-gray-200 rounded-lg w-full"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6",
        ),
        class_name="w-full max-w-7xl mx-auto animate-pulse",
    )


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero(),
        calculator_form(),
        rx.cond(
            CalculatorState.is_loading,
            rx.el.section(skeleton_loader(), class_name="py-16 bg-gray-50"),
            rx.cond(
                CalculatorState.show_results,
                rx.el.div(results_panel(), advanced_visualizations()),
                rx.fragment(),
            ),
        ),
        class_name="font-['Inter'] bg-gray-50",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")