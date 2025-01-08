# ui/pages/terminal.py

from flet import *

from utils.db_utils import fetch_records

def terminals_page(page: Page, airport_id: int):
    airport_terminals = fetch_records(table="Terminal", filters={"airport_id": airport_id})

    terminal_list = []
    for terminal in airport_terminals:
        terminal_list.append(
            Card(
                content=Column(
                        controls=[
                            Text(terminal["name"], size=28),
                        ],
                    ),
            )
        )

    return Column(
        controls=[
            Row(
                spacing=8,
                controls=[
                    IconButton(
                        tooltip='Back',
                        on_click=lambda e: e.page.go(page.views.pop().route),
                        icon=Icons.ARROW_BACK,
                    ),
                    Text(f"Terminals for Airport ID: {airport_id}", size=24, weight=FontWeight.BOLD),
                ]
            ),
            ListView(
                controls=terminal_list,
                expand=True,
            ),
        ],
        expand=True,
    )