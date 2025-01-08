# ui/main.py

from flet import *

from ui.pages.home import home_view
from ui.pages.user_management import account_view
from ui.pages.terminal import terminals_page

def main(page: Page):
    page.title="Airport Management System"
    page.window.width=800
    page.window.height=600
    page.window.maximized = True
    page.padding=0
    page.spacing=0

    # Globals
    selected_index = 0

    # A dictionary mapping routes to page views
    pages = {
        "page1": home_view(page),
        "page2": account_view(),
    }

    # Navigation function
    def switch_page(e):
        nonlocal selected_index
        if e.control.selected_index != selected_index:
            selected_index = e.control.selected_index
            selected_route = selected_index
            page.views.clear()  # Clear all views
            page.views.append(View(route=f"/{selected_route}", controls=[layout(f"page{selected_route + 1}")]))
            page.update()

    # Sidebar Navigation
    sidebar = NavigationRail(
        selected_index=selected_index,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=88,
        min_extended_width=400,
        group_alignment=-1,
        destinations=[
            NavigationRailDestination(icon=Icons.WAREHOUSE_ROUNDED, label="Airports", padding=padding.symmetric(vertical=8),),
            NavigationRailDestination(icon=Icons.ACCOUNT_CIRCLE_ROUNDED, label="My account", padding=padding.symmetric(vertical=8),),
        ],
        leading=Container(
            content=Image(src="images/ams.svg", width=56),
            padding=padding.only(bottom=20)
        ),
        on_change=switch_page,
    )

    # Layout Function
    def layout(active_page):
        return Row(
            controls=[
                sidebar,
                VerticalDivider(width=1),
                pages[active_page],
            ],
            alignment=MainAxisAlignment.CENTER,
            expand=True,
        )

    # Initial load
    page.views.append(View(route="/page1", controls=[layout("page1")]))
    page.update()

    # Handle custom routes
    def route_change(route):
        if route.route.startswith("/terminals/"):
            airport_id = route.route.split("/")[2]
            page.views.append(View(route=route.route, controls=[terminals_page(page,    airport_id)]))
            page.update()

    page.on_route_change = route_change

# Run the app
if __name__ == "__main__":
    import flet as ft
    from utils.utils import initialise_system

    initialise_system()
    ft.app(target=main, assets_dir="assets")