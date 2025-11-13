import reflex as rx
from app.states.advanced_features_state import AdvancedFeaturesState

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


def tariff_rate_history_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Tariff Rate History (HS Code: 6403.99.90)",
            class_name="text-lg font-semibold text-gray-900 mb-4",
        ),
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.x_axis(
                data_key="date", tick_line=False, axis_line=False, class_name="text-xs"
            ),
            rx.recharts.y_axis(
                tick_line=False,
                axis_line=False,
                class_name="text-xs",
                domain=[0, "auto"],
            ),
            rx.recharts.line(
                type_="monotone",
                data_key="rate",
                stroke="#10b981",
                stroke_width=2,
                dot=False,
            ),
            data=AdvancedFeaturesState.tariff_rate_history,
            height=300,
            margin={"top": 5, "right": 20, "left": -10, "bottom": 5},
        ),
        class_name="p-6 border border-gray-200 rounded-xl bg-white col-span-1 lg:col-span-2",
    )


def country_comparison_matrix() -> rx.Component:
    headers = ["HS Code", "Description", "CN", "US", "MX", "CA", "DE"]
    return rx.el.div(
        rx.el.h3(
            "Country Comparison Matrix",
            class_name="text-lg font-semibold text-gray-900 mb-4",
        ),
        rx.el.div(
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
                        AdvancedFeaturesState.country_comparison_data,
                        lambda row: rx.el.tr(
                            rx.el.td(
                                row["hs_code"],
                                class_name="px-4 py-3 text-sm font-mono text-gray-600",
                            ),
                            rx.el.td(
                                row["description"],
                                class_name="px-4 py-3 text-sm text-gray-800",
                            ),
                            rx.el.td(
                                f"{row['cn']:.1f}%",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                            rx.el.td(
                                f"{row['us']:.1f}%",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                            rx.el.td(
                                f"{row['mx']:.1f}%",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                            rx.el.td(
                                f"{row['ca']:.1f}%",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                            rx.el.td(
                                f"{row['de']:.1f}%",
                                class_name="px-4 py-3 text-sm text-gray-600",
                            ),
                            class_name="border-t border-gray-100",
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-100",
                ),
                class_name="min-w-full divide-y divide-gray-200 table-auto",
            ),
            class_name="overflow-hidden border border-gray-200 rounded-xl",
        ),
        class_name="p-6 border border-gray-200 rounded-xl bg-white col-span-1 lg:col-span-3",
    )


def advanced_visualizations() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Advanced Visualizations",
                    class_name="text-2xl font-bold text-gray-900 mb-1",
                ),
                rx.el.p(
                    "Explore tariff trends and comparisons across different dimensions.",
                    class_name="text-gray-600 mb-8",
                ),
                rx.el.div(
                    tariff_rate_history_chart(),
                    country_comparison_matrix(),
                    class_name="grid grid-cols-1 lg:grid-cols-5 gap-6",
                ),
                class_name="w-full max-w-7xl mx-auto",
            ),
            class_name="w-full max-w-7xl mx-auto",
        ),
        class_name="py-16 bg-gray-50",
    )