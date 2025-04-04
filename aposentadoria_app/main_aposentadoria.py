from datetime import datetime

import flet as ft
from flet import AppBar, ElevatedButton,Page,Text, View, colors
from flet.core.border_radius import horizontal
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.types import MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    page.title = "INSS"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def tela(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    ft.Image(src='INSS.svg.png'),
                    ElevatedButton(text="Simulção de aposentadoria", on_click=lambda _: page.go("/simulacao")),
                    ElevatedButton(text="Ver regras", on_click=lambda _: page.go("/regras")),
                ],vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao",
                    [
                        AppBar(title=Text("Simulação INSS"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text("Requisitos Básicos do Sistema"),
                        Text(" Entradas do Usuário:\n\n"),
                        input_idade,
                        genero,
                        input_tempo_contribuicao,
                        input_media_salarial,
                        categoria,
                        ElevatedButton(text="Resultado", on_click=lambda _: page.go("/simulacao")),
                    ],vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        elif page.route == "/regras":
            page.views.append(
                View(
                    "/regras",
                    [
                        AppBar(title=Text("Regras do INSS"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text("Regras Básicas de Aposentadoria:\n\n"),

                        Text(
                            "Aposentadoria por Idade:\n\n"
                            "Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n "
                            "Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\n"),
                        Text(
                            "Aposentadoria por Tempo de Contribuição:\n\n "
                            "Homens: 35 anos de contribuição.\n"
                            "Mulheres: 30 anos de contribuição.\n\n"),
                        Text(
                            "Valor Estimado do Benefício:\n\n"
                            " O valor da aposentadoria será uma média de 60% da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo de contribuição.")
                    ]
                )
            )
        # elif page.route == "/resultado":


    def conta(e):
        idade = input_idade.value
        tempo = input_tempo_contribuicao.value
        media_salarial = input_media_salarial.value
        conta = media_salarial * 60
        resultado = conta / 100
        data_atual = datetime.today
        categoria = ""
        genero = ""

        # if categoria == contribuicao:






        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    input_idade = ft.TextField(label="Idade: ",hint_text="Digite sua idade")
    input_tempo_contribuicao = ft.TextField(label="Tempo de contribuição com o INSS até o momento",hint_text="Número de anos de contribuição")
    input_media_salarial = ft.TextField(label="Digite a média salarial dos últimos anos ", hint_text="Pelo menos dos últimos 5 anos de contribuição")
    genero = ft.Dropdown(
        label="Genero",
        width=page.window.width,
        fill_color=Colors.PURPLE,
        options=[Option(key='Masc', text='Masculino'), Option(key='Fem', text='Feminino')],
    )

    categoria = ft.Dropdown(
        label="Categoria",
        width=page.window.width,
        fill_color=Colors.PURPLE,
        options=[Option(key='Contri', text='Contribuição'), Option(key='idd', text='Idade')],
    )

    page.on_route_change = tela
    page.on_view_pop = voltar

    page.go(page.route)


ft.app(main)