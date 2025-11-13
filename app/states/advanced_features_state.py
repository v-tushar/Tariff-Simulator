import reflex as rx
from typing import TypedDict


class RateHistory(TypedDict):
    date: str
    rate: float


class CountryComparison(TypedDict):
    hs_code: str
    description: str
    cn: float
    us: float
    mx: float
    ca: float
    de: float


class AdvancedFeaturesState(rx.State):
    """State for advanced data visualizations."""

    tariff_rate_history: list[RateHistory] = [
        {"date": "2023-01", "rate": 2.5},
        {"date": "2023-04", "rate": 2.5},
        {"date": "2023-07", "rate": 3.0},
        {"date": "2023-10", "rate": 3.2},
        {"date": "2024-01", "rate": 3.2},
        {"date": "2024-04", "rate": 3.5},
        {"date": "2024-07", "rate": 4.0},
    ]
    country_comparison_data: list[CountryComparison] = [
        {
            "hs_code": "6403.99.90",
            "description": "Footwear",
            "cn": 25.0,
            "us": 8.5,
            "mx": 20.0,
            "ca": 18.0,
            "de": 17.0,
        },
        {
            "hs_code": "8517.12.00",
            "description": "Cellphones",
            "cn": 10.0,
            "us": 0.0,
            "mx": 15.0,
            "ca": 0.0,
            "de": 0.0,
        },
        {
            "hs_code": "8703.23.00",
            "description": "Vehicles >1.5L",
            "cn": 15.0,
            "us": 2.5,
            "mx": 20.0,
            "ca": 6.1,
            "de": 10.0,
        },
        {
            "hs_code": "2204.21.80",
            "description": "Wine",
            "cn": 14.0,
            "us": 1.2,
            "mx": 20.0,
            "ca": 0.0,
            "de": 2.7,
        },
    ]