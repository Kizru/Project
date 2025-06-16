import flet as ft
from DataBaseClass import ComponentDB
from ComponentComparison.ComponentsComparison import *


def display_comparison_processor(component1, component2, page):
    """
    Отображает сравнение двух процессоров в виде таблицы.
    :param component1: Словарь с характеристиками первого процессора.
    :param component2: Словарь с характеристиками второго процессора.
    :param page: Объект страницы Flet для добавления интерфейса.
    """
    # Создаем заголовок таблицы
    comparison_table = ft.Column([
        ft.Row([
            ft.Container(
                ft.Text("Характеристика", weight=ft.FontWeight.BOLD),
                width=200,
                alignment=ft.alignment.center_left
            ),
            ft.Container(
                ft.Text(component1.get("name", "..."), weight=ft.FontWeight.BOLD),
                width=200,
                alignment=ft.alignment.center
            ),
            ft.Container(
                ft.Text(component2.get("name", "..."), weight=ft.FontWeight.BOLD),
                width=200,
                alignment=ft.alignment.center
            ),
        ]),
        ft.Row([
            ft.Container(ft.Text("Цена"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(f"{component1.get('price', 0)} руб"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(f"{component2.get('price', 0)} руб"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Производитель"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(component1.get("manufacturer", "...")), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(component2.get("manufacturer", "...")), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Сокет"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(component1.get("socket", "...")), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(component2.get("socket", "...")), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Поколение"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(str(component1.get("generation", "..."))), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(str(component2.get("generation", "..."))), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Количество ядер"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(str(component1.get("cores", "..."))), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(str(component2.get("cores", "..."))), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Количество потоков"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(str(component1.get("threads", "..."))), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(str(component2.get("threads", "..."))), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Базовая частота"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(f"{component1.get('base_clock', 0)} ГГц"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(f"{component2.get('base_clock', 0)} ГГц"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Турбо частота"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(f"{component1.get('turbo_clock', 0)} ГГц"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(f"{component2.get('turbo_clock', 0)} ГГц"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Встроенная графика"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text("Да" if component1.get("integrated_graphics", False) else "Нет"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text("Да" if component2.get("integrated_graphics", False) else "Нет"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("TDP"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(f"{component1.get('tdp', 0)} Вт"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(f"{component2.get('tdp', 0)} Вт"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Тип памяти"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(component1.get("memory_type", "...")), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(component2.get("memory_type", "...")), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Количество каналов памяти"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(str(component1.get("memory_channels", "..."))), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(str(component2.get("memory_channels", "..."))), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Максимальный объем памяти"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(f"{component1.get('max_memory', 0)} ГБ"), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(f"{component2.get('max_memory', 0)} ГБ"), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("Поддерживаемые частоты памяти"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(component1.get("supported_ram_frequencies", "...")), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(component2.get("supported_ram_frequencies", "...")), width=200, alignment=ft.alignment.center),
        ]),
        ft.Row([
            ft.Container(ft.Text("PCI Express версия"), width=200, alignment=ft.alignment.center_left),
            ft.Container(ft.Text(component1.get("pci_express_version", "...")), width=200, alignment=ft.alignment.center),
            ft.Container(ft.Text(component2.get("pci_express_version", "...")), width=200, alignment=ft.alignment.center),
        ]),
    ], spacing=5)

    # Добавляем таблицу на новую страницу
    page.views.append(ft.View("/comparison_result", [
        ft.AppBar(title=ft.Text("Результат сравнения процессоров"), bgcolor=ft.colors.SURFACE_VARIANT),
        comparison_table,
        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/compare")),
    ]))
    page.update()

def display_comparison_graphics_card(component1, component2, page):
    pass

def display_comparison_cooler(component1, component2, page):
    pass

def display_comparison_motherboard(component1, component2, page):
    pass

def display_comparison_ram(component1, component2, page):
    pass

def display_comparison_storage(component1, component2, page):
    pass

def display_comparison_power_supply(component1, component2, page):
    pass

def display_comparison_case(component1, component2, page):
    pass
