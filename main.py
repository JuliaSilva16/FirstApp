import flet as ft
# ft é um apelido para flet

def main(page: ft.Page):
    #configuração da página
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
                       # Ou ft.ThemeMode.DARK
    page.window_width = 375
    page.window_height = 667

    #Definição de funcões
    def exibir_nome(e):
        txt_resultado.value = input_nome.value
        page.update()


    #Criação de componentes
    input_nome = ft.TextField(label="Nome" , hint_text="Digite seu nome:")
    btn_enviar = ft.FilledButton(text="Enviar",width=page.window.width, on_click=exibir_nome)
    txt_resultado = ft.Text(value="")

    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                btn_enviar,
                txt_resultado,
             ]

        )
    )

ft.app(main)