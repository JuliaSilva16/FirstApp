import flet as ft


def main(page: ft.Page):
     # Configuração da página
     page.title = "Minha Aplicação Flet"
     page.theme_mode = ft.ThemeMode.DARK
                                    # ou ft.ThemeMode.DARK
     page.window.width = 375
     page.window.height = 667

    #Definição de funções
     def exibir_numero_imparpar(e):
         txt_resultado.value = input_num.value
         page.update()
     def impar_par(e):
         valor = input_num.value
         if int(valor) % 2 == 0:
             txt_resultado.value = "Par"
             page.update()
         else:
             txt_resultado.value = "Impar"
             page.update()


    #Criação de componentes
     input_num = ft.TextField(label="Número", hint_text="Digita um número para saber se é ímpar ou par!")
     btn_enviar = ft.FilledButton(
         text="Enviar",
         width=page.window.width,
         on_click=impar_par,
     )
     txt_resultado = ft.Text(value="")

    #Construir o layout
     page.add(
          ft.Column(
               [
                    input_num,
                    btn_enviar,
                    txt_resultado,

               ]
          )
     )
ft.app(main)