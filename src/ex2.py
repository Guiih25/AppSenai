import asyncio
from cProfile import label

import flet
import none
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, Button
from datetime import datetime

from flet.controls import page


def main(page: flet.Page):

    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text_nome.value = f"Nome: {input_nome.value}"
        text_cpf.value = f"CPF: {input_cpf.value}"
        text_email.value = f"E-mail: {input_email.value}"
        text_salario.value = f"Salário: R${input_salario.value},00"

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio"


        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
            navegar("/msg")

        # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.BLUE,
                        color=Colors.RED_500,
                    ),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
                    bnt_salvar

                ]
            )
        )
        if page.route == "/msg":
            page.views.append(
                View(
                    route="/msg",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",
                            bgcolor=Colors.RED_500,
                            color=Colors.BLUE,
                        ),
                        Container(
                            Column([
                                text_nome,
                                text_cpf,
                                text_email,
                                text_salario
                            ],
                            ),
                            bgcolor=Colors.INDIGO_900,
                            border_radius=10,
                            padding=5,
                            width=400,

                        )

                    ]
                )
            )


    # Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text_nome = Text("")
    text_cpf = Text("")
    text_email = Text("")
    text_salario = Text("")

    input_nome = TextField(label="Digite seu Nome: ")
    input_cpf = TextField(label="Digite seu CPF: ")
    input_email = TextField(label="Digite seu E-mail: ")
    input_salario = TextField(label="Digite seu salario: ")

    bnt_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)


