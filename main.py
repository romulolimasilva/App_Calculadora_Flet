import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.window_width = 350
    page.window_height = 450
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # O visor da calculadora
    display = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        width=300, 
        read_only=True,
        text_size=20
    )

    def on_click(e):
        data = e.control.content.value
        
        if data == "C":
            display.value = "0"
        elif data == "=":
            try:
                # Resolve a expressão matemática
                display.value = str(eval(display.value.replace("x", "*")))
            except:
                display.value = "Erro"
        else:
            if display.value == "0" or display.value == "Erro":
                display.value = data
            else:
                display.value += data
        
        page.update()

    # Função auxiliar para criar botões com ft.Colors
    def btn(text, color=ft.Colors.BLUE_GREY_100, text_color=ft.Colors.BLACK):
        return ft.ElevatedButton(
            content=ft.Text(value=text),
            on_click=on_click, 
            bgcolor=color, 
            color=text_color,
            expand=1 # Faz o botão crescer para preencher a linha
        )

    # Organização visual em linhas e colunas
    page.add(
        ft.Column(
            width=300,
            controls=[
                display,
                ft.Row(
                    controls=[
                        btn("C", ft.Colors.ORANGE_400, ft.Colors.WHITE), 
                        btn("/"), btn("*"), btn("-")
                    ]
                ),
                ft.Row(controls=[btn("7"), btn("8"), btn("9"), btn("+")]),
                ft.Row(controls=[btn("4"), btn("5"), btn("6"), btn("=")]),
                ft.Row(controls=[btn("1"), btn("2"), btn("3"), btn("0")]),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

ft.app(target=main)