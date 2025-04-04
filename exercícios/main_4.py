import flet as ft
from datetime import datetime

def main(page: ft.Page):
    #configuração da página
    page.title = "Minha aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
                       # Ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de funcões
    def classificar(e):
        try:
            data_nascimento = datetime.strptime(input_idade.value, "%d/%m/%Y")
            data_atual = datetime.now()
            mes = datetime.today().month
            dia = datetime.today().day
            classificacao = data_atual.year - data_nascimento.year

            if mes< data_nascimento.month :
                classificacao = classificacao - 1

            elif mes == data_nascimento.month :
                if dia < data_nascimento.day:
                    classificacao = classificacao - 1

            if classificacao <= 0 or classificacao < 18:
                txt_resultado.value= "Menor de idade"

            elif classificacao >= 18 or classificacao <= 120:
                txt_resultado.value= "Maior de idade"

            else:
                txt_resultado.value= "Error,verifique o ano de nasimento(meses não são anos,passou de 150 anos, não é mais calculado)"

            page.update()

        except ValueError:
           txt_resultado.value = "Digite uma data valida"

        page.update()

    #Criação de componentes
    input_idade = ft.TextField(label="Data de nascimento" , hint_text="Digite sua data de nascimento:")
    btn_enviar = ft.FilledButton(text="Enviar",width=page.window.width, on_click=classificar)
    txt_resultado = ft.Text(value="")

    #Contruir o layout
    page.add(
        ft.Column(
            [
                input_idade,
                btn_enviar,
                txt_resultado,
             ]

        )
    )

ft.app(main)