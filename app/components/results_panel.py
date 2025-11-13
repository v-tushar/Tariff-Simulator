import reflex as rx
from app.states.results_state import (
    ResultsState,
    CostOverTime,
    Scenario,
    TariffBreakdown,
    RecentUpdate,
)

TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "border_color": "#E8E8E8",
        "border_radius": "0.75rem",
        "box_shadow": "0px 4px 16px rgba(0, 0, 0, 0.1)",
        "padding": "0.5rem 0.75rem",
    },
    "item_style": {},
    "label_style": {"font_weight": "600"},
}


def summary_card(title: str, value: rx.Var[str], icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-gray-400"),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-gray-600"),
            rx.el.p(value, class_name="text-2xl font-semibold text-gray-900"),
            class_name="flex flex-col",
        ),
        class_name="flex items-center gap-4",
    )


def tariff_breakdown_item(item: TariffBreakdown) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name=f"{item['color']} w-2 h-2 rounded-full mr-3"),
            rx.el.p(item["name"], class_name="text-sm font-medium text-gray-700"),
            rx.el.p(
                f"{item['percentage']:.2f}%",
                class_name="ml-auto text-sm font-semibold text-gray-900",
            ),
        ),
        rx.el.p(f"${item['value']:.2f}", class_name="text-sm text-gray-500 pl-5"),
        class_name="w-full",
    )


def scenario_comparison_table() -> rx.Component:
    headers = [
        "Metric",
        "Agent 1 (Baseline)",
        "Agent 2 (Optimized)",
        "Agent 3 (Air Freight)",
    ]
    rows = [
        ("Shipment Value", "shipment_value"),
        ("Duties", "duties"),
        ("Taxes", "taxes"),
        ("Fees", "fees"),
        ("Total Landed Cost", "total"),
    ]
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.foreach(
                        headers,
                        lambda header: rx.el.th(
                            header,
                            class_name="px-4 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider",
                        ),
                    )
                ),
                class_name="bg-gray-50",
            ),
            rx.el.tbody(
                rx.foreach(
                    rows,
                    lambda row: rx.el.tr(
                        rx.el.td(
                            row[0],
                            class_name="px-4 py-3 text-sm font-medium text-gray-800",
                        ),
                        rx.foreach(
                            ResultsState.scenarios,
                            lambda scenario: rx.el.td(
                                f"${scenario[row[1]]}",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                        ),
                        class_name="border-t border-gray-200",
                    ),
                ),
                class_name="bg-white divide-y divide-gray-200",
            ),
            class_name="min-w-full divide-y divide-gray-200 table-auto",
        ),
        class_name="overflow-hidden border border-gray-200 rounded-xl",
    )


def cost_breakdown_chart() -> rx.Component:
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
        rx.recharts.x_axis(
            data_key="month", tick_line=False, axis_line=False, class_name="text-xs"
        ),
        rx.recharts.y_axis(tick_line=False, axis_line=False, class_name="text-xs"),
        rx.recharts.area(
            type_="monotone",
            data_key="duties",
            stack_id="1",
            stroke="#10b981",
            fill="#10b981",
        ),
        rx.recharts.area(
            type_="monotone",
            data_key="taxes",
            stack_id="1",
            stroke="#3b82f6",
            fill="#3b82f6",
        ),
        rx.recharts.area(
            type_="monotone",
            data_key="fees",
            stack_id="1",
            stroke="#f59e0b",
            fill="#f59e0b",
        ),
        data=ResultsState.cost_over_time,
        height=300,
        class_name="w-full",
    )


def recent_updates_item(item: RecentUpdate) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(item["code"], class_name="text-sm font-semibold text-gray-800"),
            rx.el.p(item["date"], class_name="text-xs text-gray-500"),
            class_name="flex justify-between items-center",
        ),
        rx.el.p(item["description"], class_name="text-sm text-gray-600 mt-1"),
        rx.el.p(item["change"], class_name="text-sm font-medium text-red-600 mt-1"),
        class_name="py-3 border-b border-gray-100 last:border-b-0",
    )


def action_button(text: str, icon: str, on_click: rx.event.EventSpec) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="h-4 w-4 mr-2"),
        text,
        on_click=on_click,
        class_name="flex items-center text-sm font-medium text-gray-600 bg-white border border-gray-200 hover:bg-gray-50 px-4 py-2 rounded-lg transition-all duration-200 hover:scale-105 active:scale-95",
    )


def results_panel() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    summary_card(
                        "Total Landed Cost",
                        f"${ResultsState.result_summary['total_landed_cost']}",
                        "wallet",
                    ),
                    summary_card(
                        "Duties & Taxes",
                        f"${ResultsState.result_summary['duties_and_taxes']}",
                        "landmark",
                    ),
                    summary_card(
                        "Shipment Value",
                        f"${ResultsState.result_summary['shipment_value']}",
                        "package",
                    ),
                    summary_card(
                        "HS Code", ResultsState.result_summary["hs_code"], "hash"
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 p-6 bg-gray-50 rounded-t-2xl border-b border-gray-200",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Tariff Breakdown",
                            class_name="text-lg font-semibold text-gray-900",
                        ),
                        rx.el.div(
                            rx.foreach(
                                ResultsState.tariff_breakdown, tariff_breakdown_item
                            ),
                            class_name="flex flex-col gap-3 mt-4",
                        ),
                        class_name="p-6 border border-gray-200 rounded-xl bg-white",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "Cost Breakdown Over Time",
                                class_name="text-lg font-semibold text-gray-900",
                            ),
                            action_button(
                                "Save Scenario", "save", ResultsState.save_scenario
                            ),
                            class_name="flex justify-between items-center",
                        ),
                        cost_breakdown_chart(),
                        class_name="p-6 border border-gray-200 rounded-xl bg-white col-span-2",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Multi-Agent Scenario Comparison",
                            class_name="text-lg font-semibold text-gray-900",
                        ),
                        scenario_comparison_table(),
                        class_name="p-6 border border-gray-200 rounded-xl bg-white col-span-2",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Recent Tariff Updates",
                            class_name="text-lg font-semibold text-gray-900 mb-4",
                        ),
                        rx.foreach(ResultsState.recent_updates, recent_updates_item),
                        class_name="p-6 border border-gray-200 rounded-xl bg-white",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6 pt-0",
                ),
                rx.el.div(
                    action_button(
                        "Export as CSV", "file-down", ResultsState.export_csv
                    ),
                    action_button(
                        "Export as PDF", "file-text", ResultsState.export_pdf
                    ),
                    class_name="flex justify-end gap-3 p-6 border-t border-gray-200",
                ),
                class_name="bg-white rounded-2xl shadow-sm border border-gray-100",
            ),
            class_name="w-full max-w-7xl mx-auto",
        ),
        class_name="py-16 bg-gray-50",
    )