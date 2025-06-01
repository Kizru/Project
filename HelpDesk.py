import flet as ft
import os
import subprocess
import sys

def open_help_file(e):
    help_file = "usermanual.chm"
    try:
        if os.path.exists(help_file):
            subprocess.Popen(["hh.exe", help_file], shell=True)
        else:
            print(f"Файл справки {help_file} не найден!")
    except Exception as ex:
        print(f"Ошибка при открытии файла справки: {ex}")

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]
all_builds = gaming_builds + office_builds  # Все 20 сборок

# Словарь с деталями сборок
build_details = {
    "Игровая сборка 1": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 2": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 3": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 4": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Игровая сборка 5": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Игровая сборка 6": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Игровая сборка 7": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 8": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 9": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 10": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 1": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 2": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 3": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 4": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Офисная сборка 5": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Офисная сборка 6": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 7": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 8": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 9": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 10": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
}

# Список всех возможных вариантов комплектующих с ценами
component_options = {
    "Процессор": [
        ("Intel Core i5-13600K", 25000),
        ("AMD Ryzen 7 7800X", 28000),
        ("Intel Core i9-13900KF", 35000),
        ("AMD Ryzen 9 7900X", 40000),
        ("Intel Core i5-13400", 18000),
        ("AMD Ryzen 5 7600", 15000),
        ("Intel Core i7-13700", 22000),
        ("AMD Ryzen 7 7700", 20000),
    ],
    "Охлаждение": [
        ("Cooler Master Hyper 212 RGB", 1200),
        ("Noctua NH-U12A", 2500),
        ("Corsair Hydro X Series H115i RGB Platinum", 4000),
        ("NZXT Kraken X73", 3000),
        ("Cooler Master Hyper 212 EVO", 1000),
        ("Noctua NH-L9A", 1500),
        ("DeepCool Gammaxx 400", 2000),
        ("Arctic Freezer 34 eSports", 2200),
    ],
    "Материнская плата": [
        ("ASUS ROG Strix B660-A WIFI", 15000),
        ("MSI MAG B660M Mortar WiFi", 12000),
        ("Gigabyte Z790 AORUS Elite AX", 20000),
        ("ASRock X670E Taichi", 25000),
        ("ASUS TUF B660M-PLUS WIFI", 10000),
        ("MSI B660M PRO WIFI", 8000),
        ("Gigabyte B660M DS3H", 9000),
        ("ASRock B660M Pro RS", 7000),
    ],
    "Оперативная память": [
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", 6000),
        ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", 5000),
        ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        ("Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz", 3500),
    ],
    "SSD": [
        ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        ("WD Black SN850X 2TB NVMe M.2", 15000),
        ("Kingston KC2500 2TB NVMe M.2", 12000),
        ("Sabrent Rocket 4 Plus 2TB NVMe M.2", 13000),
        ("Samsung 870 QVO 500GB SATA III", 3000),
        ("WD Blue SN550 500GB NVMe M.2", 4000),
        ("Kingston A400 480GB SATA III", 2000),
        ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
    ],
    "Жесткий диск": [
        ("Seagate BarraCuda 4TB SATA III", 3500),
        ("Western Digital Blue 6TB SATA III", 5000),
        ("Toshiba P300 4TB SATA III", 4000),
        ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        ("Seagate Barracuda 2TB SATA III", 2500),
        ("Western Digital Blue 4TB SATA III", 4500),
        ("Toshiba P300 2TB SATA III", 3000),
        ("Hitachi GST Ultrastar 4TB SATA III", 5500),
    ],
    "Видеокарта": [
        ("NVIDIA GeForce RTX 4070 Ti", 45000),
        ("AMD Radeon RX 7900 XT", 50000),
        ("NVIDIA GeForce RTX 4080", 60000),
        ("AMD Radeon RX 7800 XT", 55000),
        ("NVIDIA GeForce GT 730 2GB", 1500),
        ("AMD Radeon R5 230 2GB", 2000),
        ("NVIDIA GeForce MX550 2GB", 2500),
        ("AMD Radeon RX 640 2GB", 3000),
    ],
    "Блок питания": [
        ("Corsair RMx 850W Gold", 4000),
        ("EVGA SuperNOVA 850 G3 850W", 5000),
        ("Seasonic PRIME TX 850W Gold", 4500),
        ("Thermaltake Toughpower GF1 850W Gold", 5500),
        ("Corsair RMx 550W Gold", 3000),
        ("EVGA SuperNOVA 550 G3 550W", 3500),
        ("Seasonic Prime TX 550W Gold", 3200),
        ("Thermaltake Toughpower GF1 550W Gold", 3800),
    ],
    "Корпус": [
        ("Fractal Design Define Mini XL", 3000),
        ("NZXT H510 Elite", 2500),
        ("BitFenix Aegis Mini", 2800),
        ("Phanteks Enthoo Pro Mini", 3500),
        ("Fractal Design Node 304", 2000),
        ("NZXT H440", 2200),
        ("BitFenix Aurora", 2500),
        ("Phanteks Eclipse P300", 2800),
    ],
}

import flet as ft
import os
import subprocess
import sys

def open_help_file(e):
    help_file = "usermanual.chm"
    try:
        if os.path.exists(help_file):
            subprocess.Popen(["hh.exe", help_file], shell=True)
        else:
            print(f"Файл справки {help_file} не найден!")
    except Exception as ex:
        print(f"Ошибка при открытии файла справки: {ex}")

# Генерация списка сборок
gaming_builds = [f"Игровая сборка {i}" for i in range(1, 11)]
office_builds = [f"Офисная сборка {i}" for i in range(1, 11)]
all_builds = gaming_builds + office_builds  # Все 20 сборок

# Словарь с деталями сборок
build_details = {
    "Игровая сборка 1": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 2": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 3": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 4": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Игровая сборка 5": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Игровая сборка 6": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Игровая сборка 7": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Игровая сборка 8": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Игровая сборка 9": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Игровая сборка 10": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 1": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 2": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 3": {
        "Процессор": "Intel Core i5-13600K",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 4": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
    "Офисная сборка 5": {
        "Процессор": "Intel Core i9-13900KF",
        "Охлаждение": "DeepCool Gammaxx 400",
        "Материнская плата": "ASRock X670E Taichi",
        "Оперативная память": "Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz",
        "SSD": "Kingston KC2500 2TB NVMe M.2",
        "Жесткий диск": "Toshiba P300 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4080",
        "Блок питания": "Seasonic PRIME TX 850W Gold",
        "Корпус": "BitFenix Aegis Mini",
    },
    "Офисная сборка 6": {
        "Процессор": "AMD Ryzen 9 7900X",
        "Охлаждение": "Arctic Freezer 34 eSports",
        "Материнская плата": "Gigabyte Z790 AORUS Elite AX",
        "Оперативная память": "Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz",
        "SSD": "Sabrent Rocket 4 Plus 2TB NVMe M.2",
        "Жесткий диск": "Hitachi GST Ultrastar 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7800 XT",
        "Блок питания": "Thermaltake Toughpower GF1 850W Gold",
        "Корпус": "Phanteks Enthoo Pro Mini",
    },
    "Офисная сборка 7": {
        "Процессор": "Intel Core i7-13700",
        "Охлаждение": "Cooler Master Hyper 212 EVO",
        "Материнская плата": "ASUS TUF B660M-PLUS WIFI",
        "Оперативная память": "Corsair Value Select 16GB (2x8GB) DDR4 3200MHz",
        "SSD": "Samsung 870 QVO 500GB SATA III",
        "Жесткий диск": "Seagate Barracuda 2TB SATA III",
        "Видеокарта": "NVIDIA GeForce GT 730 2GB",
        "Блок питания": "Corsair RMx 550W Gold",
        "Корпус": "Fractal Design Node 304",
    },
    "Офисная сборка 8": {
        "Процессор": "AMD Ryzen 5 7600",
        "Охлаждение": "Noctua NH-L9A",
        "Материнская плата": "MSI B660M PRO WIFI",
        "Оперативная память": "G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz",
        "SSD": "WD Blue SN550 500GB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 4TB SATA III",
        "Видеокарта": "AMD Radeon R5 230 2GB",
        "Блок питания": "EVGA SuperNOVA 550 G3 550W",
        "Корпус": "NZXT H440",
    },
    "Офисная сборка 9": {
        "Процессор": "Intel Core i5-13400",
        "Охлаждение": "Cooler Master Hyper 212 RGB",
        "Материнская плата": "ASUS ROG Strix B660-A WIFI",
        "Оперативная память": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz",
        "SSD": "Samsung 980 Pro 1TB NVMe M.2",
        "Жесткий диск": "Seagate BarraCuda 4TB SATA III",
        "Видеокарта": "NVIDIA GeForce RTX 4070 Ti",
        "Блок питания": "Corsair RMx 850W Gold",
        "Корпус": "Fractal Design Define Mini XL",
    },
    "Офисная сборка 10": {
        "Процессор": "AMD Ryzen 7 7800X",
        "Охлаждение": "Noctua NH-U12A",
        "Материнская плата": "MSI MAG B660M Mortar WiFi",
        "Оперативная память": "G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz",
        "SSD": "WD Black SN850X 2TB NVMe M.2",
        "Жесткий диск": "Western Digital Blue 6TB SATA III",
        "Видеокарта": "AMD Radeon RX 7900 XT",
        "Блок питания": "EVGA SuperNOVA 850 G3 850W",
        "Корпус": "NZXT H510 Elite",
    },
}

# Список всех возможных вариантов комплектующих с ценами
component_options = {
    "Процессор": [
        ("Intel Core i5-13600K", 25000),
        ("AMD Ryzen 7 7800X", 28000),
        ("Intel Core i9-13900KF", 35000),
        ("AMD Ryzen 9 7900X", 40000),
        ("Intel Core i5-13400", 18000),
        ("AMD Ryzen 5 7600", 15000),
        ("Intel Core i7-13700", 22000),
        ("AMD Ryzen 7 7700", 20000),
    ],
    "Охлаждение": [
        ("Cooler Master Hyper 212 RGB", 1200),
        ("Noctua NH-U12A", 2500),
        ("Corsair Hydro X Series H115i RGB Platinum", 4000),
        ("NZXT Kraken X73", 3000),
        ("Cooler Master Hyper 212 EVO", 1000),
        ("Noctua NH-L9A", 1500),
        ("DeepCool Gammaxx 400", 2000),
        ("Arctic Freezer 34 eSports", 2200),
    ],
    "Материнская плата": [
        ("ASUS ROG Strix B660-A WIFI", 15000),
        ("MSI MAG B660M Mortar WiFi", 12000),
        ("Gigabyte Z790 AORUS Elite AX", 20000),
        ("ASRock X670E Taichi", 25000),
        ("ASUS TUF B660M-PLUS WIFI", 10000),
        ("MSI B660M PRO WIFI", 8000),
        ("Gigabyte B660M DS3H", 9000),
        ("ASRock B660M Pro RS", 7000),
    ],
    "Оперативная память": [
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", 6000),
        ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", 5000),
        ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        ("Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz", 3500),
    ],
    "SSD": [
        ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        ("WD Black SN850X 2TB NVMe M.2", 15000),
        ("Kingston KC2500 2TB NVMe M.2", 12000),
        ("Sabrent Rocket 4 Plus 2TB NVMe M.2", 13000),
        ("Samsung 870 QVO 500GB SATA III", 3000),
        ("WD Blue SN550 500GB NVMe M.2", 4000),
        ("Kingston A400 480GB SATA III", 2000),
        ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
    ],
    "Жесткий диск": [
        ("Seagate BarraCuda 4TB SATA III", 3500),
        ("Western Digital Blue 6TB SATA III", 5000),
        ("Toshiba P300 4TB SATA III", 4000),
        ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        ("Seagate Barracuda 2TB SATA III", 2500),
        ("Western Digital Blue 4TB SATA III", 4500),
        ("Toshiba P300 2TB SATA III", 3000),
        ("Hitachi GST Ultrastar 4TB SATA III", 5500),
    ],
    "Видеокарта": [
        ("NVIDIA GeForce RTX 4070 Ti", 45000),
        ("AMD Radeon RX 7900 XT", 50000),
        ("NVIDIA GeForce RTX 4080", 60000),
        ("AMD Radeon RX 7800 XT", 55000),
        ("NVIDIA GeForce GT 730 2GB", 1500),
        ("AMD Radeon R5 230 2GB", 2000),
        ("NVIDIA GeForce MX550 2GB", 2500),
        ("AMD Radeon RX 640 2GB", 3000),
    ],
    "Блок питания": [
        ("Corsair RMx 850W Gold", 4000),
        ("EVGA SuperNOVA 850 G3 850W", 5000),
        ("Seasonic PRIME TX 850W Gold", 4500),
        ("Thermaltake Toughpower GF1 850W Gold", 5500),
        ("Corsair RMx 550W Gold", 3000),
        ("EVGA SuperNOVA 550 G3 550W", 3500),
        ("Seasonic Prime TX 550W Gold", 3200),
        ("Thermaltake Toughpower GF1 550W Gold", 3800),
    ],
    "Корпус": [
        ("Fractal Design Define Mini XL", 3000),
        ("NZXT H510 Elite", 2500),
        ("BitFenix Aegis Mini", 2800),
        ("Phanteks Enthoo Pro Mini", 3500),
        ("Fractal Design Node 304", 2000),
        ("NZXT H440", 2200),
        ("BitFenix Aurora", 2500),
        ("Phanteks Eclipse P300", 2800),
    ],
}

def main(page: ft.Page):
    
    def open_helpdesk(e=None):
        if page.route == "/":
            help_file = "main_help.chm"
        elif page.route == "/create":
            help_file = "create_help.chm"
        elif page.route.startswith("/details/"):
            help_file = "details_help.chm"
        elif page.route == "/compare":
            help_file = "compare_help.chm"
        elif page.route == "/support":
            help_file = "support_help.chm"

        full_path = os.path.abspath(help_file)

        if not os.path.exists(full_path):
            print(f"Файл {full_path} не найден!")
            return

        try:
            subprocess.Popen(["hh.exe", full_path], shell=False)
        except Exception as ex:
            print(f"Ошибка при открытии файла справки: {ex}")

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "F1":
            open_helpdesk()

    page.title = "Конфигуратор ПК"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#E0E0E6"
    page.on_keyboard_event = on_keyboard

    builds_row = ft.Row(scroll="auto", spacing=10, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def create_buttons(build_list):
        return [
            ft.ElevatedButton(
                content=ft.Text(build, size=14),
                width=100,
                height=100,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    color={"": "white"},
                    bgcolor={"": "#ADD8E6"},
                ),
                on_click=lambda e, name=build: page.go(f"/details/{name}"),
            ) for build in build_list
        ]

    builds_row.controls = create_buttons(all_builds)
    builds_container = ft.Container(
        content=builds_row,
        padding=10,
        border=ft.border.all(1, "lightgray"),
        border_radius=10,
    )

    def set_filter(category):
        builds_row.controls.clear()
        if category == "Все":
            builds_row.controls.extend(create_buttons(all_builds))
        elif category == "Игровые":
            builds_row.controls.extend(create_buttons(gaming_builds))
        elif category == "Офисные":
            builds_row.controls.extend(create_buttons(office_builds))
        page.update()

    filter_controls = ft.Row(
        [
            ft.OutlinedButton("Все", on_click=lambda _: set_filter("Все")),
            ft.OutlinedButton("Офисные", on_click=lambda _: set_filter("Офисные")),
            ft.OutlinedButton("Игровые", on_click=lambda _: set_filter("Игровые")),
        ],
        spacing=10,
    )

    main_container = ft.Container(
        content=ft.Column([
            ft.Row([ft.Text("Конфигуратор ПК", size=20, weight=ft.FontWeight.BOLD), ft.IconButton(
                icon=ft.icons.POWER_SETTINGS_NEW,
                tooltip="Выйти из приложения",
                on_click=lambda e: page.window.close()
            )], alignment = ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=1, color="black"),
            ft.Row([
                ft.Text("Популярные сборки", size=16),
                ft.Row([
                    ft.ElevatedButton("Помощь", on_click=open_help_file),
                    ft.ElevatedButton("Создать сборку", on_click=lambda _: page.go("/create")),
                    ft.ElevatedButton("Сравнение комплектующих", on_click=lambda _: page.go("/compare")),
                ], spacing=10),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            filter_controls,
            builds_container,
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Хочу быть в курсе акций и новинок!", size=14),
                        ft.TextField(label="Введите адрес электронной почты", expand=True),
                        ft.ElevatedButton("Подписаться"),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=10),
                ], spacing=5),
                padding=10,
                border=ft.border.all(1, "lightgray"),
                border_radius=10,
            ),
            ft.Row([
                ft.ElevatedButton("Отзывы о сервисе"),
                ft.ElevatedButton("Служба поддержки", on_click=lambda _: page.go("/support")),
            ], alignment=ft.MainAxisAlignment.END, spacing=10),
        ], spacing=20),
        padding=20,
        border_radius=10,
        bgcolor="#F0F0F0",
    )

    # Обновляемая строка таблицы с кнопкой выбора
    def create_table_row(title, description, component_type, update_callback):
        label = ft.Text(description or "...", size=12)
        price_label = ft.Text("... рублей", size=12)

        menu_items = [
            ft.PopupMenuItem(
                text=f"{item[0]} ({item[1]} руб)",
                on_click=lambda e, item=item: update_callback(title, item, label, price_label)
            )
            for item in component_options.get(component_type, [])
        ]

        popup_menu = ft.PopupMenuButton(
            icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
            tooltip="Изменить комплектующую",
            items=menu_items,
            icon_size=20,
            bgcolor="#FFFFFF"
        )

        return ft.Row([
            ft.Container(
                content=ft.Text(title, size=14, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center_left,
                padding=ft.padding.only(left=10),
                width=150,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.Container(
                content=ft.Column([
                    label,
                    price_label,
                ], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=ft.padding.only(left=10),
                width=300,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.Container(
                content=popup_menu,
                alignment=ft.alignment.center_right,
                padding=ft.padding.only(right=10),
                width=50,
                height=50,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
        ], spacing=10, height=50)
    
    def build_details_page(page: ft.Page, build_name: str):
        details = build_details.get(build_name, {})

        total_price = 0
        total_cost_label = ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price

            # Если уже была выбрана другая комплектующая — убираем её цену из общей суммы
            if component_title in details:
                old_value = details[component_title]
                for item in component_options.get(component_title, []):
                    if item[0] == old_value:
                        total_price -= item[1]

            # Обновляем данные в словаре
            details[component_title] = new_value[0]
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        table = ft.Column([
            create_table_row("Процессор", details.get("Процессор", "..."), "Процессор", update_component),
            create_table_row("Охлаждение", details.get("Охлаждение", "..."), "Охлаждение", update_component),
            create_table_row("Материнская плата", details.get("Материнская плата", "..."), "Материнская плата", update_component),
            create_table_row("Оперативная память", details.get("Оперативная память", "..."), "Оперативная память", update_component),
            create_table_row("SSD", details.get("SSD", "..."), "SSD", update_component),
            create_table_row("Жесткий диск", details.get("Жесткий диск", "..."), "Жесткий диск", update_component),
            create_table_row("Видеокарта", details.get("Видеокарта", "..."), "Видеокарта", update_component),
            create_table_row("Блок питания", details.get("Блок питания", "..."), "Блок питания", update_component),
            create_table_row("Корпус", details.get("Корпус", "..."), "Корпус", update_component),
        ], spacing=10)

        right_section = ft.Column([
            ft.Container(
                content=total_cost_label,
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton("Сохранить сборку", width=300, height=50),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        details_content = ft.Container(
            content=ft.Row([table, right_section], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        main_content = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"Детали сборки: {build_name}", size=20, weight=ft.FontWeight.BOLD),
                    ft.Row([back_button, help_button], spacing=10),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(height=1, color="black"),
                details_content,
            ], spacing=20),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View(f"/details/{build_name}", controls=[main_content])

    def create_build_page(page: ft.Page):
        current_build = {
            "Процессор": "",
            "Охлаждение": "",
            "Материнская плата": "",
            "Оперативная память": "",
            "SSD": "",
            "Жесткий диск": "",
            "Видеокарта": "",
            "Блок питания": "",
            "Корпус": "",
        }

        total_price = 0
        # Объявление total_cost_label
        total_cost_label = ft.Text("Итоговая стоимость ПК\n... рублей", size=16, weight=ft.FontWeight.BOLD)

        def update_component(component_title, new_value, label, price_label):
            nonlocal total_price

            # Удаляем старое значение из общей суммы, если оно было
            if current_build.get(component_title):
                old_value = current_build[component_title]
                for item in component_options.get(component_title, []):
                    if item[0] == old_value:
                        total_price -= item[1]

            # Обновляем текущее значение
            current_build[component_title] = new_value[0]
            label.value = new_value[0]
            price_label.value = f"{new_value[1]} рублей"
            total_price += new_value[1]
            total_cost_label.value = f"Итоговая стоимость ПК\n{total_price} рублей"
            page.update()

        table = ft.Column([
            create_table_row("Процессор", current_build["Процессор"], "Процессор", update_component),
            create_table_row("Охлаждение", current_build["Охлаждение"], "Охлаждение", update_component),
            create_table_row("Материнская плата", current_build["Материнская плата"], "Материнская плата", update_component),
            create_table_row("Оперативная память", current_build["Оперативная память"], "Оперативная память", update_component),
            create_table_row("SSD", current_build["SSD"], "SSD", update_component),
            create_table_row("Жесткий диск", current_build["Жесткий диск"], "Жесткий диск", update_component),
            create_table_row("Видеокарта", current_build["Видеокарта"], "Видеокарта", update_component),
            create_table_row("Блок питания", current_build["Блок питания"], "Блок питания", update_component),
            create_table_row("Корпус", current_build["Корпус"], "Корпус", update_component),
        ], spacing=10)

        right_section = ft.Column([
            ft.Container(
                content=total_cost_label,
                padding=20,
                width=300,
                height=150,
                bgcolor="#FFFFFF",
                border_radius=5,
            ),
            ft.ElevatedButton("Сохранить сборку", width=300, height=50),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

        back_button = ft.ElevatedButton("Назад", on_click=lambda _: page.go("/"), width=100, height=40)
        help_button = ft.ElevatedButton("Помощь", width=100, height=40, on_click=open_help_file)

        top_row = ft.Row([
            ft.Text("Создание сборки", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([back_button, help_button], spacing=10),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        details_content = ft.Container(
            content=ft.Row([table, right_section], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        main_content = ft.Container(
            content=ft.Column([
                top_row,
                ft.Divider(height=1, color="black"),
                details_content,
            ], spacing=20),
            padding=20,
            border_radius=10,
            bgcolor="#F0F0F0",
        )

        return ft.View("/create", controls=[main_content])

    def compare_components_page(page: ft.Page):
        compare_component_options = {
            "Процессор": ["AMD Ryzen 7 7800X3D", "Intel Core i9-13900K"],
            "Охлаждение": ["Noctua NH-D15", "NZXT Kraken X73"],
            "SSD": ["Samsung 990 Pro", "Samsung 980 Pro"]
        }

        # Создаем элементы управления до их использования
        component1_dropdown = ft.Dropdown(width=200)
        component2_dropdown = ft.Dropdown(width=200)
        
        def update_component_fields(e):
            selected_type = component_type_dropdown.value
            if selected_type:
                components_row.controls[0].controls[0].value = f"{selected_type} 1"
                components_row.controls[1].controls[0].value = f"{selected_type} 2"
                
                options = compare_component_options.get(selected_type, [])
                component1_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
                component2_dropdown.options = [ft.dropdown.Option(opt) for opt in options]
                
                if options:
                    component1_dropdown.value = options[0]
                    component2_dropdown.value = options[1] if len(options) > 1 else options[0]
                
                page.update()
        
        header = ft.Row(
            controls=[
                ft.Text("Сравнение комплектующих", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda _: page.go("/"),
                    tooltip="Вернуться на главную"
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=page.width
        )
        
        # Создаем выпадающий список для выбора типа компонента
        component_type_dropdown = ft.Dropdown(
            label="Выберите комплектующие для сравнения",
            options=[
                ft.dropdown.Option("Процессор"),
                ft.dropdown.Option("Охлаждение"),
                ft.dropdown.Option("SSD"),
            ],
            width=400,
            on_change=update_component_fields
        )
        
        # Центрируем выпадающий список
        dropdown_container = ft.Container(
            content=ft.Column(
                [
                    component_type_dropdown  # Используем уже созданный элемент
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(bottom=20)
        )
        
        components_row = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text("Комплектующее 1", weight=ft.FontWeight.BOLD),
                        component1_dropdown
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Column(
                    controls=[
                        ft.Text("Комплектующее 2", weight=ft.FontWeight.BOLD),
                        component2_dropdown
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            ],
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        # Центрируем кнопку сравнения
        compare_button_container = ft.Container(
            content=ft.ElevatedButton(
                text="Сравнить",
                width=200,
                height=50
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=20)
        )
        
        content = ft.Column(
            controls=[
                header,
                dropdown_container,
                components_row,
                compare_button_container
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
        
        return ft.View("/compare", controls=[content], scroll=ft.ScrollMode.AUTO)

    def support_page(page: ft.Page):
        message_display = ft.Text("", color=ft.colors.RED, size=14)
        
        # Сначала создаем все элементы формы
        name_field = ft.TextField(label="Ваше имя", width=400)
        email_field = ft.TextField(label="Ваш email для связи", width=400)
        issue_field = ft.TextField(label="Тема проблемы", width=400)
        message_field = ft.TextField(
            label="Опишите Вашу проблему", 
            multiline=True, 
            min_lines=3,
            max_lines=5,
            width=400
        )
        
        def submit_form(e):
            if not name_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not email_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not issue_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
            if not message_field.value:
                message_display.value = "Вы заполнили не все поля!"
                message_display.color = ft.colors.RED
                page.update()
                return
                
            # Здесь должна быть реальная отправка формы
            print(f"Отправлено: {name_field.value}, {email_field.value}")
            
            message_display.value = "Заявка успешно отправлена! Ожидайте ответ от техподдержки"
            message_display.color = ft.colors.GREEN
            
            name_field.value = ""
            email_field.value = ""
            issue_field.value = ""
            message_field.value = ""
            page.update()
        
        # Создаем заголовок
        header = ft.Row(
            controls=[
                ft.Text("Служба поддержки", size=24, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    tooltip="Вернуться на главную",
                    on_click=lambda _: page.go("/")
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=page.width
        )
        
        # Создаем основную структуру страницы
        content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=20,
            controls=[
                header,  # Добавляем заголовок
                ft.Text("Часто задаваемые вопросы", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text("Как связаться с поддержкой?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Используйте форму ниже или контактные данные в конце страницы."))
                            ]
                        ),
                        ft.ExpansionTile(
                            title=ft.Text("Какие часы работы у поддержки?"),
                            controls=[
                                ft.ListTile(title=ft.Text("Мы работаем 24/7."))
                            ]
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(),
                
                ft.Text("Форма обращения в поддержку", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        name_field,
                        email_field,
                        issue_field,
                        message_field,
                        message_display,
                        ft.ElevatedButton(
                            "Отправить", 
                            on_click=submit_form,
                            width=400
                        )
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(),
                
                ft.Text("Контактная информация", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       text_align=ft.TextAlign.CENTER),
                
                ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PHONE),
                            title=ft.Text("Телефон: +7 (123) 456-78-90")
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.EMAIL),
                            title=ft.Text("Email: support@example.com")
                        ),
                    ],
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        return ft.View(
            "/support", 
            controls=[content],
            scroll=ft.ScrollMode.AUTO
        )

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/", controls=[main_container]))
        elif page.route.startswith("/details/"):
            build_name = page.route.split("/")[-1]
            page.views.append(build_details_page(page, build_name))
        elif page.route == "/create":
            page.views.append(create_build_page(page))
        elif page.route == "/compare":
            page.views.append(compare_components_page(page))
        elif page.route == "/support":
            page.views.append(support_page(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(target=main)
ft.app(target=main)