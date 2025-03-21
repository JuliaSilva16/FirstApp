import flet as ft

def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Criar função
    def somar(e):
        try:
            adicao = int(input_num1.value) + int(input_num2.value)
            txt_resultado.value=  f'Resultado = {adicao}'
            page.update()

        except ValueError:
            txt_resultado.value = "Deve ser um número inteiro"

        page.update()


    def subtrair(e):
        try:
            subtracao = int(input_num1.value) - int(input_num2.value)
            txt_resultado.value = f'Resultado = {subtracao}'
            page.update()

        except ValueError:
           txt_resultado.value = "Deve ser um número inteiro"

        page.update()


    def multiplicar(e):
        try:
            multiplicacao = int(input_num1.value) * int(input_num2.value)
            txt_resultado.value = f'Resultado = {multiplicacao}'

        except ValueError:
            txt_resultado.value = "Deve ser um número inteiro"

        page.update()

    def dividir(e):
        try:
            divisao = int(input_num1.value) / int(input_num2.value)
            if int(input_num1.value) > 0 and int(input_num2.value) > 0:
                txt_resultado.value = f'Resultado = {divisao}'

            else:
                txt_resultado.value = 'Os números devem ser maior que 0'

        except ValueError:
            txt_resultado.value = "Número inválido"

        page.update()


    #Criação de componentes
    input_num1 = ft.TextField(label="Número", hint_text="Digite um número")
    input_num2 = ft.TextField(label="Número", hint_text="Digite um número")
    btn_adicao = ft.FilledButton(
        text="Adição",
        width=page.window.width,
        on_click=somar
    )

    btn_subtracao = ft.FilledButton(
        text="Subtração",
        width=page.window.width,
        on_click=subtrair
    )

    btn_multiplicacao = ft.FilledButton(
        text="Multiplicação",
        width=page.window.width,
        on_click=multiplicar
    )

    btn_divisao = ft.FilledButton(
        text="Divisão",
        width=page.window.width,
        on_click=dividir
    )

    txt_resultado = ft.Text(value="")

    #Criar layouts
    page.add(
        ft.Column(
            [
                input_num1,
                input_num2,
                txt_resultado,
                btn_adicao,
                btn_subtracao,
                btn_multiplicacao,
                btn_divisao,
            ]

        )
    )



ft.app(main)
