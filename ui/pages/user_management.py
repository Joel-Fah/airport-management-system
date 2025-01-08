from flet import *

def account_view():
    return Container(
        content=Column(
            controls=[
                Text("Welcome to Page 2", size=30),
                Text("This is the content of the second page."),
            ],
            alignment=MainAxisAlignment.CENTER
        ),
        alignment=alignment.center,
        expand=True,
    )
