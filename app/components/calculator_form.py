import reflex as rx
from app.states.calculator_state import CalculatorState


def form_input(
    label: str,
    name: str,
    placeholder: str,
    input_type: str = "text",
    icon: str | None = None,
    required: bool = True,
    tooltip: str | None = None,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(label, class_name="text-sm font-medium text-gray-700"),
            rx.cond(
                tooltip is not None,
                rx.el.div(
                    rx.icon("info", class_name="h-4 w-4 text-gray-400 cursor-pointer"),
                    rx.el.div(
                        tooltip,
                        class_name="absolute bottom-full mb-2 w-max max-w-xs p-2 text-xs text-white bg-gray-800 rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none",
                    ),
                    class_name="relative group flex items-center",
                ),
            ),
            class_name="flex items-center gap-2 mb-1",
        ),
        rx.el.div(
            rx.cond(
                icon is not None,
                rx.icon(icon, class_name="h-5 w-5 text-gray-400"),
                None,
            ),
            rx.el.input(
                name=name,
                placeholder=placeholder,
                type=input_type,
                required=required,
                class_name="w-full bg-transparent focus:outline-none placeholder-gray-400",
            ),
            class_name="flex items-center gap-3 w-full border border-gray-200 bg-white rounded-lg px-3 py-2 focus-within:border-emerald-500 focus-within:ring-2 focus-within:ring-emerald-100 transition-all",
        ),
        class_name="w-full",
    )


def form_select(
    label: str, name: str, options: list, placeholder: str, required: bool = True
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700 mb-1"),
        rx.el.select(
            rx.el.option(placeholder, value="", disabled=True),
            rx.foreach(
                options,
                lambda option: rx.el.option(option["name"], value=option["code"]),
            ),
            name=name,
            required=required,
            class_name="w-full border border-gray-200 bg-white rounded-lg px-3 py-2 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100 transition-all",
        ),
        class_name="w-full",
    )


def transport_mode_selector() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Mode of Transport", class_name="text-sm font-medium text-gray-700 mb-1"
        ),
        rx.el.div(
            rx.foreach(
                CalculatorState.transport_modes,
                lambda mode: rx.el.button(
                    rx.icon(mode["icon"], class_name="h-5 w-5 mr-2"),
                    mode["name"],
                    on_click=lambda: CalculatorState.set_active_transport_mode(
                        mode["name"]
                    ),
                    class_name=rx.cond(
                        CalculatorState.active_transport_mode == mode["name"],
                        "flex items-center justify-center flex-1 px-4 py-2 text-sm font-semibold text-emerald-700 bg-emerald-50 border border-emerald-200 rounded-lg transition-colors",
                        "flex items-center justify-center flex-1 px-4 py-2 text-sm font-medium text-gray-600 bg-white border border-gray-200 hover:bg-gray-50 rounded-lg transition-colors",
                    ),
                    type="button",
                ),
            ),
            rx.el.input(
                type="hidden",
                name="transport_mode",
                default_value=CalculatorState.active_transport_mode,
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-2",
        ),
        class_name="w-full md:col-span-2",
    )


def calculator_form() -> rx.Component:
    """The advanced tariff calculator form."""
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Tariff Calculator", class_name="text-2xl font-bold text-gray-900 mb-1"
            ),
            rx.el.p(
                "Fill in the details below to calculate the estimated duties and taxes.",
                class_name="text-gray-600 mb-8",
            ),
            rx.el.form(
                rx.el.div(
                    form_input(
                        "Entry Date",
                        "entry_date",
                        "",
                        input_type="date",
                        icon="calendar",
                        tooltip="The date the goods are expected to enter the destination country.",
                    ),
                    form_select(
                        "Country of Origin",
                        "origin_country",
                        CalculatorState.countries,
                        "Select a country",
                    ),
                    form_input(
                        "Shipment Value",
                        "shipment_value",
                        "10000",
                        input_type="number",
                        icon="dollar-sign",
                        tooltip="Total value of the shipment in USD.",
                    ),
                    form_input(
                        "HS Code",
                        "hs_code",
                        "e.g. 6403.99.90",
                        icon="hash",
                        tooltip="Harmonized System code for the product.",
                    ),
                    form_input(
                        "Weight (kg)",
                        "weight",
                        "100",
                        input_type="number",
                        icon="weight",
                    ),
                    form_input(
                        "Quantity", "quantity", "500", input_type="number", icon="boxes"
                    ),
                    transport_mode_selector(),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.cond(
                            CalculatorState.is_loading,
                            rx.spinner(class_name="h-5 w-5 text-white"),
                            "Calculate Tariff",
                        ),
                        type="submit",
                        disabled=CalculatorState.is_loading,
                        class_name="w-full flex justify-center bg-emerald-500 hover:bg-emerald-600 text-white font-semibold px-6 py-3 rounded-xl transition-all duration-200 hover:scale-105 active:scale-95 disabled:bg-emerald-300 disabled:scale-100",
                    ),
                    class_name="mt-8",
                ),
                on_submit=CalculatorState.handle_submit,
                reset_on_submit=True,
            ),
            class_name="w-full max-w-4xl mx-auto bg-white p-8 rounded-2xl shadow-sm border border-gray-100",
        ),
        class_name="py-16 bg-gray-50",
    )