# ui/pages/home.py

import datetime

from flet import *

from services.airport_service import AIRPORT_TABLE_NAME, AIRPORT_DISPLAY_FIELDS
from ui.pages.terminal import terminals_page
from ui.ui_utils.constants import BORDER_RADIUS
from utils.db_utils import fetch_records
from utils.utils import timeago

# Airport Data
airports = fetch_records(table=AIRPORT_TABLE_NAME, fields=AIRPORT_DISPLAY_FIELDS, echo=False)

def home_view(page: Page):
    def view_details(e, airport_id):
        page.views.append(View(route=f"/terminals/{airport_id}", controls=[terminals_page(page, airport_id)]))
        page.update()

    return Stack(
        controls=[
            Column(
                controls=[
                    Stack(
                        controls=[
                            Container(
                                padding=padding.all(16),
                                border_radius=16,
                                expand=True,
                                content=Column(
                                    spacing=8,
                                    controls=[
                                        Text(
                                            "Airport Management System",
                                            weight=FontWeight.BOLD,
                                            size=36,
                                            color=colors.BLUE,
                                        ),
                                        Text(
                                            "A lightweight airport management system to manage flights, passengers, "
                                            "tickets, terminals, and staff. Built with Python and SQLite3, it ensures "
                                            "efficient and straightforward airport operations.",
                                            size=16,
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                    ListView(
                        padding=padding.all(12),
                        spacing=20,
                        divider_thickness=1,
                        controls=[
                            Row(
                                spacing=16,
                                controls=[
                                    Image(src=airport["image_url"], fit=ImageFit.COVER, width=400, height=224,
                                          error_content=Container(
                                              alignment=alignment.center,
                                              bgcolor=colors.WHITE10,
                                              border_radius=16,
                                              width=400, height=224,
                                              content=Image(src="images/favicon.svg", scale=0.5)
                                          ),
                                          ),
                                    Column(
                                        expand=True,
                                        controls=[
                                            Text(value=f"added {timeago(airport['created_at'])}",
                                                 style=TextStyle(size=12, color=colors.GREY)),
                                            Text(value=f"{airport['name']} ({airport['code']})",
                                                 style=TextStyle(size=28, weight=FontWeight.W_500)),
                                            Text(f"{airport['location']}",
                                                 style=TextStyle(size=20, color=colors.GREY, weight=FontWeight.W_500)),
                                            Row(
                                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                expand=True,
                                                controls=[
                                                    Container(
                                                        padding=padding.symmetric(vertical=8),
                                                        content=ElevatedButton(
                                                            on_click=lambda e, airport_id=airport['id']: view_details(e, airport_id),
                                                            content=Row(
                                                                spacing=8,
                                                                controls=[
                                                                    Icon(Icons.VISIBILITY, color=colors.WHITE),
                                                                    Text('View Details', color=colors.WHITE),
                                                                ]
                                                            ),
                                                            style=ButtonStyle(
                                                                bgcolor=colors.BLUE,
                                                                padding=padding.symmetric(vertical=8,
                                                                                          horizontal=20),
                                                                shape=RoundedRectangleBorder(
                                                                    radius=border_radius.all(
                                                                        BORDER_RADIUS * 1.25)
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    Row(
                                                        spacing=8,
                                                        controls=[
                                                            Container(
                                                                padding=padding.symmetric(vertical=8),
                                                                content=ElevatedButton(
                                                                    on_click=None,
                                                                    content=Row(
                                                                        spacing=8,
                                                                        controls=[
                                                                            Icon(Icons.EDIT),
                                                                            Text('Edit'),
                                                                        ]
                                                                    ),
                                                                    style=ButtonStyle(
                                                                        padding=padding.symmetric(vertical=8,
                                                                                                  horizontal=20),
                                                                        shape=RoundedRectangleBorder(
                                                                            radius=border_radius.all(
                                                                                BORDER_RADIUS * 1.25)
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                            Container(
                                                                padding=padding.symmetric(vertical=8),
                                                                content=ElevatedButton(
                                                                    on_click=None,
                                                                    content=Row(
                                                                        spacing=8,
                                                                        controls=[
                                                                            Icon(Icons.DELETE, color=colors.RED),
                                                                            Text('Delete', color=colors.RED),
                                                                        ]
                                                                    ),
                                                                    style=ButtonStyle(
                                                                        padding=padding.symmetric(vertical=8,
                                                                                                  horizontal=20),
                                                                        bgcolor=colors.RED_50,
                                                                        shape=RoundedRectangleBorder(
                                                                            radius=border_radius.all(
                                                                                BORDER_RADIUS * 1.25)
                                                                        ),
                                                                    )
                                                                ),
                                                            ),
                                                        ]
                                                    )
                                                ]
                                            )
                                        ],
                                        alignment=MainAxisAlignment.START,
                                    ),
                                ],
                                alignment=MainAxisAlignment.START,
                                expand=True
                            )
                            for airport in airports
                        ],
                        expand=True,
                    ),
                ]
            ),
            FloatingActionButton(icon=Icons.ADD, text="Add airport", bottom=0, right=0),
        ],
        expand=True,
    )