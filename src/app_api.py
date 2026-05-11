import asyncio
import flet as ft
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow

from src.api_endpoints import get_planetas, get_personagens


def main(page: ft.Page):
    page.title = "Dragon Ball API"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    list_view = ListView(expand=True, spacing=10, padding=15)

    def montar_lista_personagens():
        list_view.controls.clear()
        lista_dados = get_personagens()

        COR_PRIMARIA = "#f85c1b"
        COR_CARD = "#111d23"
        COR_TEXTO_VAR = "#aebdc5"

        for item in lista_dados.get("items", []):
            nome = str(item.get("name", "Desconhecido")).upper()
            ki = str(item.get("ki", "0"))
            imagem = item.get("image", "")
            descricao = item.get("description", "Sem descrição.")

            list_view.controls.append(
                ft.Container(
                    bgcolor=COR_CARD,
                    border_radius=ft.BorderRadius(12, 12, 12, 12),
                    padding=15,
                    margin=ft.Margin(0, 0, 0, 15),
                    content=ft.Column([
                        ft.Image(src=imagem, width=400, height=200, fit="cover",
                                 border_radius=ft.BorderRadius(10, 10, 10, 10)),
                        ft.Column([
                            ft.Row([
                                ft.Text(nome, size=20, weight=FontWeight.BOLD, color=Colors.WHITE),
                                ft.Text(ki, size=12, color=Colors.WHITE),
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Text(descricao, size=13, color=COR_TEXTO_VAR, max_lines=2,
                                    overflow=TextOverflow.ELLIPSIS),

                        ], spacing=10)
                    ])
                )
            )
        page.update()

    def montar_lista_planetas():
        list_view.controls.clear()
        lista_dados = get_planetas()

        for item in lista_dados.get("items", []):
            list_view.controls.append(
                ListTile(
                    leading=Image(src=item.get("image", ""), width=50, height=50, fit="contain"),
                    title=Text(item.get("name", "Planeta"), weight=FontWeight.BOLD, color=Colors.ORANGE),
                    subtitle=Text(item.get("description", ""), max_lines=2, color=Colors.GREY,
                                  overflow=TextOverflow.ELLIPSIS),
                )
            )
        page.update()

    def mudar_aba(e):
        # Aqui pegamos o índice diretamente do clique
        if e.control.selected_index == 1:
            montar_lista_planetas()
        else:
            montar_lista_personagens()

    nav_bar = NavigationBar(
        selected_index=0,
        destinations=[
            NavigationBarDestination(icon=Icons.PERSON, label="Personagens"),
            NavigationBarDestination(icon=Icons.PUBLIC, label="Planetas"),
        ],
        on_change=mudar_aba,
    )

    def route_change(e=None):
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    ft.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD, color=Colors.WHITE),
                        bgcolor=Colors.ORANGE,
                        center_title=True
                    ),
                    list_view,  # A lista fica no centro
                ],
                navigation_bar=nav_bar,  # A barra fica fixa embaixo
                padding=0
            )
        )
        # Carrega personagens por padrão
        montar_lista_personagens()
        page.update()

    page.on_route_change = route_change
    route_change()


if __name__ == "__main__":
    ft.app(target=main)
