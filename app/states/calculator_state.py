import reflex as rx
import asyncio
from typing import TypedDict
import pandas as pd
import logging


class Country(TypedDict):
    name: str
    code: str


class TransportMode(TypedDict):
    name: str
    icon: str


class HTSCode(TypedDict):
    code: str
    description: str


class CalculatorState(rx.State):
    """State for the tariff calculator form."""

    form_data: dict = {}
    is_loading: bool = False
    show_results: bool = False
    countries: list[Country] = [
        {"name": "China", "code": "CN"},
        {"name": "United States", "code": "US"},
        {"name": "Mexico", "code": "MX"},
        {"name": "Canada", "code": "CA"},
        {"name": "Germany", "code": "DE"},
        {"name": "Japan", "code": "JP"},
    ]
    transport_modes: list[TransportMode] = [
        {"name": "Ocean", "icon": "ship"},
        {"name": "Air", "icon": "plane"},
        {"name": "Rail", "icon": "train-track"},
        {"name": "Truck", "icon": "truck"},
    ]
    active_transport_mode: str = "Ocean"
    search_query: str = ""
    search_suggestions: list[HTSCode] = []
    all_hts_codes: list[HTSCode] = [
        {"code": "6403.99.90", "description": "Footwear, outer soles of rubber..."},
        {"code": "8517.12.00", "description": "Telephones for cellular networks..."},
        {"code": "9006.53.00", "description": "Cameras, for roll film of a width..."},
        {
            "code": "8703.23.00",
            "description": "Vehicles with spark-ignition engine >1.5L",
        },
        {
            "code": "2204.21.80",
            "description": "Wine of fresh grapes, in containers > 2L",
        },
    ]

    @rx.event
    def set_active_transport_mode(self, mode: str):
        self.active_transport_mode = mode

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.is_loading = True
        self.show_results = False
        yield
        await asyncio.sleep(2)
        self.form_data = form_data
        self.is_loading = False
        self.show_results = True
        yield rx.toast("Calculation complete!", duration=3000)

    @rx.event
    def get_suggestions(self, query: str | None = None):
        if query is None:
            query = self.search_query
        if not query:
            self.search_suggestions = []
            return
        self.search_suggestions = [
            code
            for code in self.all_hts_codes
            if query.lower() in code["code"].lower()
            or query.lower() in code["description"].lower()
        ][:5]

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def select_suggestion(self, code: str):
        self.search_query = code
        self.search_suggestions = []

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
        try:
            upload_data = await files[0].read()
            upload_dir = rx.get_upload_dir()
            upload_dir.mkdir(parents=True, exist_ok=True)
            file_path = upload_dir / files[0].filename
            with file_path.open("wb") as f:
                f.write(upload_data)
            df = pd.read_csv(file_path)
            if "hts_code" in df.columns:
                num_codes = len(df["hts_code"].dropna())
                yield rx.toast(
                    f"Successfully parsed {num_codes} HTS codes.", duration=3000
                )
            else:
                yield rx.toast("CSV must contain a 'hts_code' column.", duration=5000)
        except Exception as e:
            logging.exception(f"Error processing file: {e}")
            yield rx.toast(f"Error processing file: {e}", duration=5000)