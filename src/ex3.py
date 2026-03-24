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
        text_marca.value = f"Marca: {input_marca.value}"
        text_polegada.value = f"Polegadas: {input_polegada.value}"


        tem_erro = False

        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        if input_polegada.value:
            input_polegada.error = None
        else:
            tem_erro = True
            input_polegada.error = "Campo obrigatorio"




        if not tem_erro:
            input_marca.value = ""
            input_polegada.value = ""

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
                        color=Colors.WHITE,
                    ),
                    text,
                    input_marca,
                    input_polegada,
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
                            bgcolor=Colors.GREY_700,
                            color=Colors.BLUE,
                        ),
                        Container(
                            Column([
                                text_marca,
                                text_polegada
                            ],
                            ),
                            bgcolor=Colors.INDIGO_900,
                            border_radius=10,
                            padding=20,
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
    text = Text("Informações da Televisão")
    text_marca = Text("")
    text_polegada = Text("")


    input_marca = TextField(label="Digite a marca: ")
    input_polegada = TextField(label="Digite quantas polegadas: ")


    bnt_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)


