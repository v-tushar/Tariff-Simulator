import reflex as rx
import asyncio
from typing import TypedDict


class TariffBreakdown(TypedDict):
    name: str
    value: float
    percentage: float
    color: str


class Scenario(TypedDict):
    name: str
    shipment_value: int
    duties: int
    taxes: int
    fees: int
    total: int


class CostOverTime(TypedDict):
    month: str
    duties: int
    taxes: int
    fees: int


class RecentUpdate(TypedDict):
    code: str
    description: str
    date: str
    change: str


class ResultsState(rx.State):
    """State for the tariff results display."""

    result_summary: dict = {
        "total_landed_cost": 12350,
        "duties_and_taxes": 2350,
        "shipment_value": 10000,
        "hs_code": "6403.99.90",
    }
    tariff_breakdown: list[TariffBreakdown] = [
        {
            "name": "Merchandise Processing Fee",
            "value": 34.5,
            "percentage": 1.47,
            "color": "bg-blue-500",
        },
        {
            "name": "Customs Duty (25%)",
            "value": 2250.0,
            "percentage": 95.74,
            "color": "bg-emerald-500",
        },
        {
            "name": "Harbor Maintenance Fee",
            "value": 12.5,
            "percentage": 0.53,
            "color": "bg-purple-500",
        },
        {
            "name": "Other Taxes",
            "value": 53.0,
            "percentage": 2.26,
            "color": "bg-yellow-500",
        },
    ]
    scenarios: list[Scenario] = [
        {
            "name": "Agent 1 (Baseline)",
            "shipment_value": 10000,
            "duties": 2250,
            "taxes": 53,
            "fees": 47,
            "total": 12350,
        },
        {
            "name": "Agent 2 (Optimized)",
            "shipment_value": 10000,
            "duties": 1800,
            "taxes": 45,
            "fees": 40,
            "total": 11885,
        },
        {
            "name": "Agent 3 (Air Freight)",
            "shipment_value": 10000,
            "duties": 2250,
            "taxes": 53,
            "fees": 250,
            "total": 12553,
        },
    ]
    cost_over_time: list[CostOverTime] = [
        {"month": "Jan", "duties": 2250, "taxes": 53, "fees": 47},
        {"month": "Feb", "duties": 2300, "taxes": 55, "fees": 48},
        {"month": "Mar", "duties": 2100, "taxes": 50, "fees": 45},
        {"month": "Apr", "duties": 2400, "taxes": 60, "fees": 50},
        {"month": "May", "duties": 2350, "taxes": 58, "fees": 49},
        {"month": "Jun", "duties": 2500, "taxes": 62, "fees": 52},
    ]
    recent_updates: list[RecentUpdate] = [
        {
            "code": "6403.99.90",
            "description": "Footwear, outer soles of rubber...",
            "date": "2024-07-28",
            "change": "Duty rate increased by 2%",
        },
        {
            "code": "8517.12.00",
            "description": "Telephones for cellular networks...",
            "date": "2024-07-25",
            "change": "New exemption applied for specific origins",
        },
        {
            "code": "9006.53.00",
            "description": "Cameras, for roll film of a width...",
            "date": "2024-07-22",
            "change": "Classification ruling updated",
        },
    ]

    @rx.event
    def save_scenario(self) -> rx.event.EventSpec:
        return rx.toast("Scenario saved successfully!", duration=3000)

    @rx.event
    def export_csv(self) -> rx.event.EventSpec:
        return rx.toast("Exporting to CSV...", duration=3000)

    @rx.event
    def export_pdf(self) -> rx.event.EventSpec:
        return rx.toast("Generating PDF...", duration=3000)