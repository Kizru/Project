import sqlite3
from email.contentmanager import raw_data_manager


class ComponentDB:
    def __init__(self, db_name="components.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()
        self.populate_if_empty()

    def create_tables(self):
        # Основная таблица для общих данных комплектующих
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS components (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    description TEXT,
                    manufacturer TEXT,
                    category TEXT NOT NULL  -- Добавлено поле "category"
                )
            ''')

        # Таблица для процессоров
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS processors (
                    component_id INTEGER NOT NULL,
                    socket TEXT NOT NULL,
                    generation INTEGER NOT NULL,
                    cores INTEGER NOT NULL,
                    threads INTEGER NOT NULL,
                    base_clock REAL NOT NULL,
                    turbo_clock REAL NOT NULL,
                    integrated_graphics BOOLEAN NOT NULL,
                    tdp INTEGER NOT NULL,
                    memory_type TEXT NOT NULL,
                    memory_channels INTEGER NOT NULL,
                    max_memory INTEGER NOT NULL,
                    pci_express_version TEXT NOT NULL,
                    supported_ram_frequencies TEXT NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для видеокарт
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS graphics_cards (
                    component_id INTEGER NOT NULL,
                    vram_capacity INTEGER NOT NULL,
                    vram_type TEXT NOT NULL,
                    memory_interface_width INTEGER NOT NULL,
                    base_clock REAL NOT NULL,
                    boost_clock REAL NOT NULL,
                    tdp INTEGER NOT NULL,
                    pci_express_version TEXT NOT NULL,
                    length INTEGER NOT NULL,
                    height INTEGER NOT NULL,
                    width_slots INTEGER NOT NULL,
                    power_connectors TEXT NOT NULL,
                    recommended_power_supply INTEGER NOT NULL,
                    directx_support TEXT NOT NULL,
                    cooling_solution TEXT NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для охлаждения
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS coolers (
                    component_id INTEGER NOT NULL,
                    sockets_compatibility TEXT NOT NULL,
                    tdp_support INTEGER NOT NULL,
                    fans_count INTEGER NOT NULL,
                    noise_level INTEGER NOT NULL,
                    size TEXT NOT NULL,
                    radiator_size INTEGER,
                    pump_dimensions TEXT,
                    fan_connector TEXT NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для материнских плат
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS motherboards (
                    component_id INTEGER NOT NULL,
                    form_factor TEXT NOT NULL,
                    socket TEXT NOT NULL,
                    chipset TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    max_memory_capacity INTEGER NOT NULL,
                    memory_slots INTEGER NOT NULL,
                    supported_ram_frequencies TEXT NOT NULL,
                    pci_express_version TEXT NOT NULL,
                    pci_express_slots TEXT NOT NULL,
                    m2_slots INTEGER NOT NULL,
                    sata_ports INTEGER NOT NULL,
                    usb_ports TEXT NOT NULL,
                    fan_headers INTEGER NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для оперативной памяти
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS ram (
                    component_id INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    modules_count INTEGER NOT NULL,
                    module_capacity INTEGER NOT NULL,
                    frequency INTEGER NOT NULL,
                    voltage REAL NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для накопителей
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS storage (
                    component_id INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    interface TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    form_factor TEXT NOT NULL,
                    rpm INTEGER,
                    cache_size INTEGER,
                    power_consumption REAL,
                    read_speed INTEGER,
                    write_speed INTEGER,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для блоков питания
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS power_supplies (
                    component_id INTEGER NOT NULL,
                    power INTEGER NOT NULL,
                    certification TEXT NOT NULL,
                    modularity TEXT NOT NULL,
                    form_factor TEXT NOT NULL,
                    dimensions TEXT NOT NULL,
                    main_connector TEXT NOT NULL,
                    cpu_connectors TEXT NOT NULL,
                    pci_e_connectors TEXT NOT NULL,
                    sata_connectors INTEGER NOT NULL,
                    molex_connectors INTEGER NOT NULL,
                    fan_size INTEGER NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

        # Таблица для корпусов
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS cases (
                    component_id INTEGER NOT NULL,
                    form_factor_support TEXT NOT NULL,
                    dimensions TEXT NOT NULL,
                    gpu_max_length INTEGER NOT NULL,
                    cpu_cooler_max_height INTEGER NOT NULL,
                    psu_form_factor TEXT NOT NULL,
                    drive_bays_3_5 INTEGER NOT NULL,
                    drive_bays_2_5 INTEGER NOT NULL,
                    expansion_slots INTEGER NOT NULL,
                    front_panel_ports TEXT NOT NULL,
                    fans_preinstalled TEXT NOT NULL,
                    fan_mounts TEXT NOT NULL,
                    radiator_support TEXT NOT NULL,
                    FOREIGN KEY (component_id) REFERENCES components(id)
                )
            ''')

    def populate_if_empty(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM components")
        if cursor.fetchone()[0] > 0:
            print("База данных уже заполнена.")
            return

        # SQL-запросы для добавления данных
        populate_data_request = """
        -- Добавление процессоров
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Intel Core i5-13600K', 25000, 'Intel', 'Процессор для игр и работы', 'processor'),
            ('AMD Ryzen 7 7800X', 30000, 'AMD', 'Мощный процессор для гейминга', 'processor'),
            ('Intel Core i9-13900KF', 35000, 'Intel', 'Флагманский процессор Intel', 'processor');

        INSERT INTO processors (component_id, socket, generation, cores, threads, base_clock, turbo_clock, integrated_graphics, tdp, memory_type, memory_channels, max_memory, pci_express_version, supported_ram_frequencies)
        SELECT id, 'LGA1700', 13, 14, 20, 3.5, 5.1, 1, 125, 'DDR4', 2, 128, 'PCIe 5.0', '3200, 3600, 4000' FROM components WHERE name = 'Intel Core i5-13600K';
        INSERT INTO processors (component_id, socket, generation, cores, threads, base_clock, turbo_clock, integrated_graphics, tdp, memory_type, memory_channels, max_memory, pci_express_version, supported_ram_frequencies)
        SELECT id, 'AM5', 7000, 8, 16, 4.0, 5.0, 0, 105, 'DDR5', 2, 128, 'PCIe 5.0', '4800, 5200, 6000' FROM components WHERE name = 'AMD Ryzen 7 7800X';
        INSERT INTO processors (component_id, socket, generation, cores, threads, base_clock, turbo_clock, integrated_graphics, tdp, memory_type, memory_channels, max_memory, pci_express_version, supported_ram_frequencies)
        SELECT id, 'LGA1700', 13, 24, 32, 3.0, 5.8, 0, 150, 'DDR5', 2, 192, 'PCIe 5.0', '4800, 5600, 6400' FROM components WHERE name = 'Intel Core i9-13900KF';

        -- Добавление видеокарт
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('NVIDIA GeForce RTX 4070 Ti', 45000, 'NVIDIA', 'Видеокарта для 2K/4K-гейминга', 'graphics_card'),
            ('AMD Radeon RX 7800 XT', 55000, 'AMD', 'Флагман AMD для игр', 'graphics_card');

        INSERT INTO graphics_cards (component_id, vram_capacity, vram_type, memory_interface_width, base_clock, boost_clock, tdp, pci_express_version, length, height, width_slots, power_connectors, recommended_power_supply, directx_support, cooling_solution)
        SELECT id, 12, 'GDDR6X', 192, 1605, 2610, 285, 'PCIe 4.0', 310, 130, 3, '2x 8-pin', 750, 'DirectX 12 Ultimate', 'Air Cooling' FROM components WHERE name = 'NVIDIA GeForce RTX 4070 Ti';
        INSERT INTO graphics_cards (component_id, vram_capacity, vram_type, memory_interface_width, base_clock, boost_clock, tdp, pci_express_version, length, height, width_slots, power_connectors, recommended_power_supply, directx_support, cooling_solution)
        SELECT id, 16, 'GDDR6', 256, 1800, 2430, 263, 'PCIe 4.0', 287, 110, 3, '2x 8-pin', 700, 'DirectX 12 Ultimate', 'Air Cooling' FROM components WHERE name = 'AMD Radeon RX 7800 XT';

        -- Добавление охлаждения
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Cooler Master Hyper 212 RGB', 1200, 'Cooler Master', 'Недорогое воздушное охлаждение', 'cooler'),
            ('Noctua NH-U12A', 2500, 'Noctua', 'Высококачественное воздушное охлаждение', 'cooler');

        INSERT INTO coolers (component_id, sockets_compatibility, tdp_support, fans_count, noise_level, size, radiator_size, pump_dimensions, fan_connector)
        SELECT id, 'LGA1700, AM4, AM5', 150, 1, 28, '120x120x150', NULL, '80x80x50', '4-pin PWM' FROM components WHERE name = 'Cooler Master Hyper 212 RGB';
        INSERT INTO coolers (component_id, sockets_compatibility, tdp_support, fans_count, noise_level, size, radiator_size, pump_dimensions, fan_connector)
        SELECT id, 'LGA1700, AM4, AM5', 200, 1, 25, '150x120x150', NULL, '80x80x50', '4-pin PWM' FROM components WHERE name = 'Noctua NH-U12A';

        -- Добавление материнских плат
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('ASUS ROG Strix B660-A WIFI', 15000, 'ASUS', 'Материнская плата для игр', 'motherboard'),
            ('Gigabyte B660M DS3H', 9000, 'Gigabyte', 'Бюджетная материнская плата', 'motherboard');

        INSERT INTO motherboards (component_id, form_factor, socket, chipset, memory_type, max_memory_capacity, memory_slots, supported_ram_frequencies, pci_express_version, pci_express_slots, m2_slots, sata_ports, usb_ports, fan_headers)
        SELECT id, 'ATX', 'LGA1700', 'B660', 'DDR4', 128, 4, '3200, 3600, 4000', 'PCIe 5.0', '1x PCIe 5.0 x16', 3, 6, '4x USB 3.2 Gen 1, 2x USB-C', 4 FROM components WHERE name = 'ASUS ROG Strix B660-A WIFI';
        INSERT INTO motherboards (component_id, form_factor, socket, chipset, memory_type, max_memory_capacity, memory_slots, supported_ram_frequencies, pci_express_version, pci_express_slots, m2_slots, sata_ports, usb_ports, fan_headers)
        SELECT id, 'microATX', 'LGA1700', 'B660', 'DDR4', 64, 2, '3200, 3600', 'PCIe 4.0', '1x PCIe 4.0 x16', 2, 4, '4x USB 3.2 Gen 1', 2 FROM components WHERE name = 'Gigabyte B660M DS3H';

        -- Добавление оперативной памяти
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz', 6000, 'Corsair', 'Оперативная память для игр', 'ram'),
            ('G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz', 4000, 'G.Skill', 'Оперативная память для офиса', 'ram');

        INSERT INTO ram (component_id, type, capacity, modules_count, module_capacity, frequency, voltage)
        SELECT id, 'DDR4', 32, 2, 16, 3600, 1.35 FROM components WHERE name = 'Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz';
        INSERT INTO ram (component_id, type, capacity, modules_count, module_capacity, frequency, voltage)
        SELECT id, 'DDR5', 16, 2, 8, 5600, 1.25 FROM components WHERE name = 'G.Skill Ripjaws S 16GB (2x8GB) DDR5 5600MHz';

        -- Добавление накопителей
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Samsung 980 Pro 1TB NVMe M.2', 10000, 'Samsung', 'SSD с высокой скоростью', 'storage'),
            ('Western Digital Blue 6TB SATA III', 4500, 'WD', 'Жесткий диск для хранения данных', 'storage');

        INSERT INTO storage (component_id, type, interface, capacity, form_factor, rpm, cache_size, power_consumption, read_speed, write_speed)
        SELECT id, 'SSD', 'NVMe PCIe 4.0', 1000, 'M.2 2280', NULL, NULL, NULL, 7000, 6000 FROM components WHERE name = 'Samsung 980 Pro 1TB NVMe M.2';
        INSERT INTO storage (component_id, type, interface, capacity, form_factor, rpm, cache_size, power_consumption, read_speed, write_speed)
        SELECT id, 'HDD', 'SATA III', 6000, '3.5"', 7200, 256, 6.0, NULL, NULL FROM components WHERE name = 'Western Digital Blue 6TB SATA III';

        -- Добавление блоков питания
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Seasonic PRIME TX 850W Gold', 4500, 'Seasonic', 'Мощный блок питания', 'power_supply'),
            ('Corsair RMx 550W Gold', 3000, 'Corsair', 'Надежный блок питания', 'power_supply');

        INSERT INTO power_supplies (component_id, power, certification, modularity, form_factor, dimensions, main_connector, cpu_connectors, pci_e_connectors, sata_connectors, molex_connectors, fan_size)
        SELECT id, 850, '80 Plus Gold', 'полностью модульный', 'ATX', '150x140x86', '24-pin ATX', '2x 8-pin EPS', '3x 8-pin PCIe', 8, 4, 120 FROM components WHERE name = 'Seasonic PRIME TX 850W Gold';
        INSERT INTO power_supplies (component_id, power, certification, modularity, form_factor, dimensions, main_connector, cpu_connectors, pci_e_connectors, sata_connectors, molex_connectors, fan_size)
        SELECT id, 550, '80 Plus Gold', 'полностью модульный', 'ATX', '150x140x86', '24-pin ATX', '1x 8-pin EPS', '2x 8-pin PCIe', 6, 3, 120 FROM components WHERE name = 'Corsair RMx 550W Gold';

        -- Добавление корпусов
        INSERT INTO components (name, price, manufacturer, description, category) VALUES
            ('Fractal Design Node 304', 2000, 'Fractal Design', 'Компактный корпус', 'case'),
            ('NZXT H440', 2200, 'NZXT', 'Стильный корпус', 'case');

        INSERT INTO cases (component_id, form_factor_support, dimensions, gpu_max_length, cpu_cooler_max_height, psu_form_factor, drive_bays_3_5, drive_bays_2_5, expansion_slots, front_panel_ports, fans_preinstalled, fan_mounts, radiator_support)
        SELECT id, 'microATX, mini-ITX', '350x200x380', 320, 160, 'ATX', 3, 2, 7, '2x USB 3.0, 1x USB-C', '2x 120mm', '2x 120mm, 1x 140mm', '240mm' FROM components WHERE name = 'Fractal Design Node 304';
        INSERT INTO cases (component_id, form_factor_support, dimensions, gpu_max_length, cpu_cooler_max_height, psu_form_factor, drive_bays_3_5, drive_bays_2_5, expansion_slots, front_panel_ports, fans_preinstalled, fan_mounts, radiator_support)
        SELECT id, 'ATX, microATX, mini-ITX', '450x230x470', 400, 170, 'ATX', 3, 2, 7, '2x USB 3.0, 1x USB-C', '1x 120mm', '3x 120mm, 2x 140mm', '360mm' FROM components WHERE name = 'NZXT H440';
        """

        try:
            # Выполнение запросов
            cursor.executescript(populate_data_request)
            self.conn.commit()
            print("Данные успешно добавлены в базу данных.")
        except Exception as e:
            print(f"Ошибка при добавлении данных: {e}")

    def add_component(self, name, price, description, category):
        with self.conn:
            self.conn.execute('''
                INSERT INTO components (name, price, description, category)
                VALUES (?, ?, ?, ?)
            ''', (name, price, description, category))

    def get_by_category(self, category):
        cursor = self.conn.cursor()
        if category == "processor":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN processors p ON c.id = p.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "graphics_card":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN graphics_cards g ON c.id = g.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "cooler":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN coolers cl ON c.id = cl.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "motherboard":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN motherboards m ON c.id = m.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "ram":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN ram r ON c.id = r.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "storage":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN storage s ON c.id = s.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "power_supply":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN power_supplies ps ON c.id = ps.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "case":
            cursor.execute('''
                SELECT c.name, c.price
                FROM components c
                JOIN cases cs ON c.id = cs.component_id
                WHERE c.category = ?
            ''', (category,))
        return cursor.fetchall()

    def get_full_by_category(self, category):
        cursor = self.conn.cursor()
        if category == "processor":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, p.*
                FROM components c
                JOIN processors p ON c.id = p.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "graphics_card":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, g.*
                FROM components c
                JOIN graphics_cards g ON c.id = g.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "cooler":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, cl.*
                FROM components c
                JOIN coolers cl ON c.id = cl.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "motherboard":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, m.*
                FROM components c
                JOIN motherboards m ON c.id = m.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "ram":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, r.*
                FROM components c
                JOIN ram r ON c.id = r.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "storage":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, s.*
                FROM components c
                JOIN storage s ON c.id = s.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "power_supply":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, ps.*
                FROM components c
                JOIN power_supplies ps ON c.id = ps.component_id
                WHERE c.category = ?
            ''', (category,))
        elif category == "case":
            cursor.execute('''
                SELECT c.id, c.name, c.price, c.description, cs.*
                FROM components c
                JOIN cases cs ON c.id = cs.component_id
                WHERE c.category = ?
            ''', (category,))
        return cursor.fetchall()

    def get_component_details(self, component_id):
        cursor = self.conn.cursor()
        category = self.get_category_by_id(component_id) + "s"
        if category == "rams": category = "ram"
        if category == "storages": category = "storage"
        if category == "power_supplys": category = "power_supplies"
        cursor.execute(f'''
            SELECT c.id, c.name, c.price, c.description, c.manufacturer, p.*
            FROM components c
            LEFT JOIN {category} p ON c.id = p.component_id
            WHERE c.id = ?
        ''', (component_id,))
        row = cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return {}

    def get_id_by_name(self, component_name):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT c.id
            FROM components c
            WHERE c.name = ?
        ''', (component_name,))

        result = cursor.fetchone()
        if result:
            return result[0]  # Возвращаем первый элемент кортежа (ID)
        return None  # Если компонент не найден, возвращаем None

    def get_category_by_id(self, component_id):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT c.category
        FROM components c
        WHERE c.id = ?
        ''', (component_id,))

        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def close(self):
        self.conn.close()
