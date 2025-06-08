import sqlite3

component_options = {
    "Процессор": [
        ("Intel Core i5-13600K", 25000, "13-е поколение, 14 потоков, высокопроизводительный процессор"),
        ("AMD Ryzen 7 7800X", 28000, "8 ядер, высокая частота, идеален для игр"),
        ("Intel Core i9-13900KF", 35000, "Флагман Intel, 24 потока, без встроенной графики"),
        ("AMD Ryzen 9 7900X", 40000, "12 ядер, высокая производительность в многозадачности"),
        ("Intel Core i5-13400", 18000, "10 потоков, отличное решение для дома и офиса"),
        ("AMD Ryzen 5 7600", 15000, "6 ядер, отличное соотношение цена/производительность"),
        ("Intel Core i7-13700", 22000, "16 потоков, подходит для игр и рабочих задач"),
        ("AMD Ryzen 7 7700", 20000, "8 ядер, универсальный и сбалансированный процессор"),
    ],
    "Охлаждение": [
        ("Cooler Master Hyper 212 RGB", 1200, "Классическое воздушное охлаждение с RGB-подсветкой"),
        ("Noctua NH-U12A", 2500, "Мощное и тихое охлаждение от Noctua"),
        ("Corsair Hydro X Series H115i RGB Platinum", 4000, "Жидкостная система охлаждения с RGB"),
        ("NZXT Kraken X73", 3000, "AIO жидкостное охлаждение с отличной производительностью"),
        ("Cooler Master Hyper 212 EVO", 1000, "Бюджетное воздушное охлаждение"),
        ("Noctua NH-L9A", 1500, "Компактное и тихое охлаждение для малых корпусов"),
        ("DeepCool Gammaxx 400", 2000, "Доступное и эффективное охлаждение"),
        ("Arctic Freezer 34 eSports", 2200, "Мощный кулер с тихой работой и доступной ценой"),
    ],
    "Материнская плата": [
        ("ASUS ROG Strix B660-A WIFI", 15000, "Материнская плата для геймеров с Wi-Fi и RGB"),
        ("MSI MAG B660M Mortar WiFi", 12000, "Компактная плата с поддержкой DDR4 и Wi-Fi"),
        ("Gigabyte Z790 AORUS Elite AX", 20000, "Премиальная Z790 плата с мощной подсистемой питания"),
        ("ASRock X670E Taichi", 25000, "Флагманская плата для Ryzen с богатой комплектацией"),
        ("ASUS TUF B660M-PLUS WIFI", 10000, "Надёжная microATX плата с Wi-Fi"),
        ("MSI B660M PRO WIFI", 8000, "Бюджетное решение с Wi-Fi"),
        ("Gigabyte B660M DS3H", 9000, "Хорошее решение для среднего бюджета"),
        ("ASRock B660M Pro RS", 7000, "Доступная и стабильная плата с базовым функционалом"),
    ],
    "Оперативная память": [
        ("Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz", 6000, "Высокочастотная память для гейминга и рендера"),
        ("G.Skill Trident Z Neo 32GB (2x16GB) DDR5 6000MHz", 8000, "DDR5 память с высокой пропускной способностью"),
        ("Kingston FURY Beast 32GB (2x16GB) DDR4 3200MHz", 5000, "Надёжная память от Kingston для игр и работы"),
        ("Crucial Ballistix 32GB (2x16GB) DDR5 6400MHz", 7000, "Оверклокерская память с высокой частотой"),
        ("Corsair Value Select 16GB (2x8GB) DDR4 3200MHz", 3000, "Бюджетный комплект памяти для повседневных задач"),
        ("G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz", 4000, "Современная DDR5 память по разумной цене"),
        ("Kingston ValueRAM 16GB (2x8GB) DDR4 2666MHz", 2000, "Простая память для офисных задач"),
        ("Crucial Ballistix 16GB (2x8GB) DDR5 5200MHz", 3500, "Баланс цены и скорости для новых сборок"),
    ],
    "SSD": [
        ("Samsung 980 Pro 1TB NVMe M.2", 10000, "Высокоскоростной SSD от Samsung на PCIe 4.0"),
        ("WD Black SN850X 2TB NVMe M.2", 15000, "Быстрый и надёжный SSD для гейминга"),
        ("Kingston KC2500 2TB NVMe M.2", 12000, "Эффективное NVMe-решение с хорошей ценой"),
        ("Sabrent Rocket 4 Plus 2TB NVMe M.2", 13000, "Мощный SSD для профессионалов"),
        ("Samsung 870 QVO 500GB SATA III", 3000, "Надёжный SATA SSD для повседневной работы"),
        ("WD Blue SN550 500GB NVMe M.2", 4000, "Бюджетный NVMe SSD от WD"),
        ("Kingston A400 480GB SATA III", 2000, "Недорогой SATA SSD для офиса"),
        ("Sabrent Rocket 4 500GB NVMe M.2", 3500, "Быстрый и компактный NVMe SSD"),
    ],
    "Жесткий диск": [
        ("Seagate BarraCuda 4TB SATA III", 3500, "Накопитель большого объема для хранения данных"),
        ("Western Digital Blue 6TB SATA III", 5000, "Надёжный HDD для хранения фото, видео и архивов"),
        ("Toshiba P300 4TB SATA III", 4000, "Сбалансированный диск по объёму и скорости"),
        ("Hitachi GST Ultrastar 6TB SATA III", 6000, "Промышленный HDD с высокой надёжностью"),
        ("Seagate Barracuda 2TB SATA III", 2500, "Базовое решение для хранения данных"),
        ("Western Digital Blue 4TB SATA III", 4500, "WD Blue — стандарт качества для HDD"),
        ("Toshiba P300 2TB SATA III", 3000, "Компактный и недорогой накопитель"),
        ("Hitachi GST Ultrastar 4TB SATA III", 5500, "Быстрый и надёжный HDD для серверов и рабочих станций"),
    ],
    "Видеокарта": [
        ("NVIDIA GeForce RTX 4070 Ti", 45000, "Мощная видеокарта для 2K/4K-гейминга и работы"),
        ("AMD Radeon RX 7900 XT", 50000, "Флагман AMD для игр и рендеринга"),
        ("NVIDIA GeForce RTX 4080", 60000, "Премиум-графика от NVIDIA для энтузиастов"),
        ("AMD Radeon RX 7800 XT", 55000, "Производительная видеокарта для современных игр"),
        ("NVIDIA GeForce GT 730 2GB", 1500, "Офисная видеокарта для простых задач"),
        ("AMD Radeon R5 230 2GB", 2000, "Базовая графика для повседневных нужд"),
        ("NVIDIA GeForce MX550 2GB", 2500, "Экономичный вариант для ноутбуков и офисных ПК"),
        ("AMD Radeon RX 640 2GB", 3000, "Лёгкий игровой уровень и мультимедиа"),
    ],
    "Блок питания": [
        ("Corsair RMx 850W Gold", 4000, "Мощный и надёжный БП с сертификацией Gold"),
        ("EVGA SuperNOVA 850 G3 850W", 5000, "Компактный БП с высокой мощностью"),
        ("Seasonic PRIME TX 850W Gold", 4500, "Топовое качество и стабильность питания"),
        ("Thermaltake Toughpower GF1 850W Gold", 5500, "Тихий и надёжный блок с длинной гарантией"),
        ("Corsair RMx 550W Gold", 3000, "Подходит для большинства систем среднего уровня"),
        ("EVGA SuperNOVA 550 G3 550W", 3500, "Эффективный и компактный БП"),
        ("Seasonic Prime TX 550W Gold", 3200, "Премиум блок питания для небольших сборок"),
        ("Thermaltake Toughpower GF1 550W Gold", 3800, "Надёжный блок питания с защитой и сертификацией"),
    ],
    "Корпус": [
        ("Fractal Design Define Mini XL", 3000, "Стильный корпус с отличной шумоизоляцией"),
        ("NZXT H510 Elite", 2500, "Современный корпус с закалённым стеклом"),
        ("BitFenix Aegis Mini", 2800, "Компактный корпус для microATX сборок"),
        ("Phanteks Enthoo Pro Mini", 3500, "Хорошее охлаждение и модульная система"),
        ("Fractal Design Node 304", 2000, "Миниатюрный корпус для домашних сборок"),
        ("NZXT H440", 2200, "Надёжный и вместительный корпус"),
        ("BitFenix Aurora", 2500, "Корпус с подсветкой и стеклом по бокам"),
        ("Phanteks Eclipse P300", 2800, "Бюджетный и функциональный корпус для сборки"),
    ],
}


class ComponentDB:
    def __init__(self, db_name="components.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()
        self.populate_if_empty()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS components (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    description TEXT,
                    category TEXT NOT NULL
                )
            ''')

    def populate_if_empty(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM components")
        if cursor.fetchone()[0] == 0:
            for category, items in component_options.items():
                for name, price, description in items:
                    self.add_component(name, price, description, category)

    def add_component(self, name, price, description, category):
        with self.conn:
            self.conn.execute('''
                INSERT INTO components (name, price, description, category)
                VALUES (?, ?, ?, ?)
            ''', (name, price, description, category))

    def get_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT name, price FROM components WHERE category = ?
        ''', (category,))
        return cursor.fetchall()

    def get_full_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT id, name, price, description FROM components WHERE category = ?
        ''', (category,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
