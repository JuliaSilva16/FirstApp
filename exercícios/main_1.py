import flet as ft
# ft é um apelido para flet

def main(page: ft.Page):
    #configuração da página
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
                       # Ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de funcões
    def exibir_nome(e):
        txt_resultado.value = f'{input_nome.value}{input_sobrenome.value}'
        page.update()

    #Criação de componentes
    input_nome = ft.TextField(label="Nome" , hint_text="Digite seu nome:")
    input_sobrenome = ft.TextField(label="Sobrenome" , hint_text="Digite seu sobrenome:")
    btn_enviar = ft.FilledButton(text="Enviar",width=page.window.width, on_click=exibir_nome)
    txt_resultado = ft.Text(value="")

    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,
             ]

        )
    )

ft.app(main)