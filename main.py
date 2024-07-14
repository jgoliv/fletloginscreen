import flet as ft
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:

    # page main configs ----------------------------------------------------------------------------------------------
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 500
    page.window.height = 500

    # creating fields and inputs -------------------------------------------------------------------------------------
    username_input: TextField = ft.TextField(label="Username", text_align=ft.TextAlign.LEFT, width=250)
    password_input: TextField = ft.TextField(label="Password", text_align=ft.TextAlign.LEFT, width=250, password=True)
    checkbox_input: Checkbox = ft.Checkbox(label="I agree to the conditions", value=False)
    submit_button: ElevatedButton = ft.ElevatedButton(text="Sign up", width=200, disabled=True)

    # validating function to enable submit button --------------------------------------------------------------------
    def validate(e: ControlEvent) -> None:
        inputs = [username_input.value, password_input.value, checkbox_input.value]
        if all(inputs):
            submit_button.disabled = False
        else:
            submit_button.disabled = True

        page.update()

    # after sign up page ---------------------------------------------------------------------------------------------
    def submit(e: ControlEvent) -> None:
        page.clean()
        page.add(
            ft.Row(
                controls=[ft.Text(value=f'Hello: {username_input.value}', size=25)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # link the functions to the UI -----------------------------------------------------------------------------------
    username_input.on_change = validate
    password_input.on_change = validate
    checkbox_input.on_change = validate
    submit_button.on_click = submit

    # render the main page -------------------------------------------------------------------------------------------
    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    [
                        username_input,
                        password_input,
                        checkbox_input,
                        submit_button
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)