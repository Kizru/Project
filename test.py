import json
from DataBaseClass import ComponentDB

db = ComponentDB()

# Старые данные сборок
old_build_details = {
    "Игровая сборка 1": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 RGB", 1200),
        "Материнская плата": ("ASUS ROG Strix B660-A WIFI", 15000),
        "Оперативная память": ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", 6000),
        "SSD": ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        "Жесткий диск": ("Western Digital Blue 6TB SATA III", 4500),
        "Видеокарта": ("NVIDIA GeForce RTX 4070 Ti", 45000),
        "Блок питания": ("Corsair RMx 850W Gold", 4000),
        "Корпус": ("Fractal Design Define Mini XL", 3000),
    },
    "Игровая сборка 2": {
        "Процессор": ("AMD Ryzen 7 7800X", 28000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("MSI MAG B660M Mortar WiFi", 12000),
        "Оперативная память": ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        "SSD": ("WD Black SN850X 2TB NVMe M.2", 15000),
        "Жесткий диск": ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        "Видеокарта": ("AMD Radeon RX 7900 XT", 50000),
        "Блок питания": ("EVGA SuperNOVA 850 G3 850W", 5000),
        "Корпус": ("NZXT Kraken X73", 3000),
    },
    "Игровая сборка 3": {
        "Процессор": ("Intel Core i9-13900KF", 35000),
        "Охлаждение": ("Corsair Hydro X Series H115i RGB Platinum", 4000),
        "Материнская плата": ("Gigabyte Z790 AORUS Elite AX", 20000),
        "Оперативная память": ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", 5000),
        "SSD": ("Kingston KC2500 2TB NVMe M.2", 12000),
        "Жесткий диск": ("Seagate BarraCuda 4TB SATA III", 3500),
        "Видеокарта": ("NVIDIA GeForce RTX 4080", 60000),
        "Блок питания": ("Seasonic PRIME TX 850W Gold", 4500),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
    "Игровая сборка 4": {
        "Процессор": ("AMD Ryzen 9 7900X", 40000),
        "Охлаждение": ("NZXT Kraken X73", 3000),
        "Материнская плата": ("ASRock X670E Taichi", 25000),
        "Оперативная память": ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        "SSD": ("Sabrent Rocket 4 Plus 2TB NVMe M.2", 13000),
        "Жесткий диск": ("Toshiba P300 4TB SATA III", 4000),
        "Видеокарта": ("AMD Radeon RX 7800 XT", 55000),
        "Блок питания": ("Thermaltake Toughpower GF1 850W Gold", 5500),
        "Корпус": ("Phanteks Enthoo Pro Mini", 3500),
    },
    "Игровая сборка 5": {
        "Процессор": ("Intel Core i7-13700", 22000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Hitachi GST Ultrastar 4TB SATA III", 5500),
        "Видеокарта": ("NVIDIA GeForce GT 730 2GB", 1500),
        "Блок питания": ("Corsair RMx 550W Gold", 3000),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Игровая сборка 6": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("WD Blue SN550 500GB NVMe M.2", 4000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("AMD Radeon R5 230 2GB", 1000),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("NZXT H440", 2200),
    },
    "Игровая сборка 7": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("DeepCool Gammaxx 400", 2000),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("AMD Radeon RX 640 2GB", 3000),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("BitFenix Aurora", 2500),
    },
    "Игровая сборка 8": {
        "Процессор": ("AMD Ryzen 7 7700", 20000),
        "Охлаждение": ("Arctic Freezer 34 eSports", 2200),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz", 3500),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("NVIDIA GeForce MX550 2GB", 2500),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    "Игровая сборка 9": {
        "Процессор": ("Intel Core i7-13700", 22000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("ASUS ROG Strix B660-A WIFI", 15000),
        "Оперативная память": ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000),
        "SSD": ("WD Black SN850X 2TB NVMe M.2", 15000),
        "Жесткий диск": ("Hitachi GST Ultrastar 6TB SATA III", 6000),
        "Видеокарта": ("NVIDIA GeForce RTX 4070 Ti", 45000),
        "Блок питания": ("Corsair RMx 850W Gold", 4000),
        "Корпус": ("NZXT H510 Elite", 2500),
    },
    "Игровая сборка 10": {
        "Процессор": ("AMD Ryzen 9 7900X", 40000),
        "Охлаждение": ("NZXT Kraken X73", 3000),
        "Материнская плата": ("ASRock X670E Taichi", 25000),
        "Оперативная память": ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000),
        "SSD": ("Samsung 980 Pro 1TB NVMe M.2", 10000),
        "Жесткий диск": ("Seagate BarraCuda 4TB SATA III", 3500),
        "Видеокарта": ("AMD Radeon RX 7800 XT", 55000),
        "Блок питания": ("Seasonic PRIME TX 850W Gold", 4500),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    # Офисные сборки
    "Офисная сборка 1": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 2": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 3": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 RGB", 1200),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Integrated Graphics", 12000),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
    "Офисная сборка 4": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-U12A", 2500),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Intel HD Graphics 630", 0),
        "Блок питания": ("Corsair RMx 550W Gold", 3000),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 5": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("WD Blue SN550 500GB NVMe M.2", 3000),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 6": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("BitFenix Aurora", 2500),
    },
    "Офисная сборка 7": {
        "Процессор": ("Intel Core i5-13400", 18000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("Gigabyte B660M DS3H", 9000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("Phanteks Eclipse P300", 2800),
    },
    "Офисная сборка 8": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("ASRock B660M Pro RS", 7000),
        "Оперативная память": ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000),
        "SSD": ("Samsung 870 QVO 500GB SATA III", 3000),
        "Жесткий диск": ("Western Digital Blue 4TB SATA III", 4500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Seasonic Prime TX 550W Gold", 3200),
        "Корпус": ("NZXT H440", 2200),
    },
    "Офисная сборка 9": {
        "Процессор": ("Intel Core i5-13600K", 25000),
        "Охлаждение": ("Cooler Master Hyper 212 EVO", 1000),
        "Материнская плата": ("ASUS TUF B660M-PLUS WIFI", 10000),
        "Оперативная память": ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000),
        "SSD": ("Kingston A400 480GB SATA III", 2000),
        "Жесткий диск": ("Toshiba P300 2TB SATA III", 3000),
        "Видеокарта": ("Intel UHD Graphics 730", 0),
        "Блок питания": ("EVGA SuperNOVA 550 G3 550W", 3500),
        "Корпус": ("Fractal Design Node 304", 2000),
    },
    "Офисная сборка 10": {
        "Процессор": ("AMD Ryzen 5 7600", 15000),
        "Охлаждение": ("Noctua NH-L9A", 1500),
        "Материнская плата": ("MSI B660M PRO WIFI", 8000),
        "Оперативная память": ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000),
        "SSD": ("Sabrent Rocket 4 500GB NVMe M.2", 3500),
        "Жесткий диск": ("Seagate Barracuda 2TB SATA III", 2500),
        "Видеокарта": ("Integrated Graphics", 0),
        "Блок питания": ("Thermaltake Toughpower GF1 550W Gold", 3800),
        "Корпус": ("BitFenix Aegis Mini", 2800),
    },
}

# Функция для получения ID компонента по его названию
def get_component_id(component_name):
    cursor = db.conn.cursor()
    cursor.execute("SELECT id FROM components WHERE name = ?", (component_name,))
    row = cursor.fetchone()
    return row[0] if row else None

# Обновление сборок
updated_builds = {}

for build_name, components in old_build_details.items():
    updated_components = {}
    for category, component_data in components.items():
        component_name = component_data[0]  # Название компонента
        component_id = get_component_id(component_name)
        if component_id:
            updated_components[category] = component_id
        else:
            print(f"Компонент '{component_name}' не найден в базе данных!")
    updated_builds[build_name] = updated_components

# Сохранение обновленных сборок в файл
output_file = "updated_builds.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(updated_builds, f, indent=4, ensure_ascii=False)

print(f"Обновленные сборки сохранены в файл: {output_file}")