import flet as ft
from DataBaseClass import ComponentDB
from ComponentComparison.ComponentsComparison import *


def display_comparison_processor(component1, component2, page):
    comparison_table = ft.Column([
        ft.Row([
            ft.Text("Характеристика", weight=ft.FontWeight.BOLD),
            ft.Text(component1.get("name", "..."), weight=ft.FontWeight.BOLD),
            ft.Text(component2.get("name", "..."), weight=ft.FontWeight.BOLD),
        ]),
        ft.Row([ft.Text("Цена"), ft.Text(f"{component1.get('price', 0)} руб"), ft.Text(f"{component2.get('price', 0)} руб")]),
        ft.Row([ft.Text("Производитель"), ft.Text(component1.get("manufacturer", "...")), ft.Text(component2.get("manufacturer", "..."))]),
        ft.Row([ft.Text("Сокет"), ft.Text(component1.get("socket", "...")), ft.Text(component2.get("socket", "..."))]),
        ft.Row([ft.Text("Поколение"), ft.Text(str(component1.get("generation", "..."))), ft.Text(str(component2.get("generation", "...")))]),
        ft.Row([ft.Text("Количество ядер"), ft.Text(str(component1.get("cores", "..."))), ft.Text(str(component2.get("cores", "...")))]),
        ft.Row([ft.Text("Количество потоков"), ft.Text(str(component1.get("threads", "..."))), ft.Text(str(component2.get("threads", "...")))]),
        ft.Row([ft.Text("Базовая частота"), ft.Text(f"{component1.get('base_clock', 0)} ГГц"), ft.Text(f"{component2.get('base_clock', 0)} ГГц")]),
        ft.Row([ft.Text("Турбо частота"), ft.Text(f"{component1.get('turbo_clock', 0)} ГГц"), ft.Text(f"{component2.get('turbo_clock', 0)} ГГц")]),
        ft.Row([ft.Text("Встроенная графика"), ft.Text("Да" if component1.get("integrated_graphics", False) else "Нет"), ft.Text("Да" if component2.get("integrated_graphics", False) else "Нет")]),
        ft.Row([ft.Text("TDP"), ft.Text(f"{component1.get('tdp', 0)} Вт"), ft.Text(f"{component2.get('tdp', 0)} Вт")]),
        ft.Row([ft.Text("Тип памяти"), ft.Text(component1.get("memory_type", "...")), ft.Text(component2.get("memory_type", "..."))]),
        ft.Row([ft.Text("Количество каналов памяти"), ft.Text(str(component1.get("memory_channels", "..."))), ft.Text(str(component2.get("memory_channels", "...")))]),
        ft.Row([ft.Text("Максимальный объем памяти"), ft.Text(f"{component1.get('max_memory', 0)} ГБ"), ft.Text(f"{component2.get('max_memory', 0)} ГБ")]),
        ft.Row([ft.Text("Поддерживаемые частоты памяти"), ft.Text(component1.get("supported_ram_frequencies", "...")), ft.Text(component2.get("supported_ram_frequencies", "..."))]),
        ft.Row([ft.Text("PCI Express версия"), ft.Text(component1.get("pci_express_version", "...")), ft.Text(component2.get("pci_express_version", "..."))]),
    ], spacing=10)

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
