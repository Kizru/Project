from DataBaseClass import ComponentDB

db = ComponentDB()


def check_processor_compatibility(processor, build):
    """
    Проверяет совместимость процессора с остальными комплектующими в сборке.

    :param processor: Словарь с характеристиками процессора.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы
        # Сокет
        if processor["socket"] != motherboard_details["socket"]:
            compatibility_issues.append(
                f"Сокет процессора ({processor['socket']}) не совместим с материнской платой ({motherboard_details['socket']}).")

        # Чипсет (поколение процессора)
        supported_generations = motherboard_details.get("supported_generations", "").split(", ")
        if str(processor["generation"]) not in supported_generations:
            compatibility_issues.append(
                f"Поколение процессора ({processor['generation']}) не поддерживается чипсетом материнской платы.")
        # Тип оперативной памяти
        if processor["memory_type"] != motherboard_details["memory_type"]:
            compatibility_issues.append(
                f"Тип памяти процессора ({processor['memory_type']}) не совместим с материнской платой ({motherboard_details['memory_type']}).")

        # Количество каналов памяти
        if processor["memory_channels"] > motherboard_details["memory_slots"]:
            compatibility_issues.append(
                f"Количество каналов памяти процессора ({processor['memory_channels']}) превышает количество слотов на материнской плате ({motherboard_details['memory_slots']}).")

        # Максимальная частота памяти
        max_memory_frequency = int(motherboard_details["supported_ram_frequencies"].split(", ")[-1])
        if int(processor["supported_ram_frequencies"].split(", ")[-1]) > max_memory_frequency:
            compatibility_issues.append(
                f"Максимальная частота памяти процессора ({int(processor["supported_ram_frequencies"].split(", ")[-1])} МГц) превышает поддерживаемую материнской платой ({max_memory_frequency} МГц).")

        # Максимальный объем оперативной памяти
        if processor["max_memory"] > motherboard_details["max_memory_capacity"]:
            compatibility_issues.append(
                f"Максимальный объем памяти процессора ({processor['max_memory']} ГБ) превышает поддерживаемый материнской платой ({motherboard_details['max_memory_capacity']} ГБ).")

        # Версия PCI Express
        if processor["pci_express_version"] != motherboard_details["pci_express_version"]:
            compatibility_issues.append(
                f"Версия PCI Express процессора ({processor['pci_express_version']}) не совместима с материнской платой ({motherboard_details['pci_express_version']}).")

    # 2. Проверка совместимости с оперативной памятью
    ram = build.get("Оперативная память")
    if ram[0]:
        ram_details = db.get_component_details(db.get_id_by_name(ram[0]))  # Получаем данные оперативной памяти
        if processor["memory_type"] != ram_details["type"]:
            compatibility_issues.append(
                f"Тип памяти процессора ({processor['memory_type']}) не совместим с оперативной памятью ({ram_details['type']}).")

        if ram_details["frequency"] > int(processor["supported_ram_frequencies"].split(", ")[-1]):
            compatibility_issues.append(
                f"Частота оперативной памяти ({ram_details['frequency']} МГц) превышает поддерживаемую процессором ({int(processor["supported_ram_frequencies"].split(", ")[-1])} МГц).")

    # 3. Проверка совместимости с охлаждением
    cooler = build.get("Охлаждение")
    if cooler[0]:
        cooler_details = db.get_component_details(db.get_id_by_name(cooler[0]))  # Получаем данные охлаждения
        if processor["tdp"] > cooler_details["tdp_support"]:
            compatibility_issues.append(
                f"TDP процессора ({processor['tdp']} Вт) превышает поддерживаемое охлаждением ({cooler_details['tdp_support']} Вт).")

    # 4. Проверка совместимости с блоком питания
    psu = build.get("Блок питания")
    if psu[0]:
        psu_details = db.get_component_details(db.get_id_by_name(psu[0]))  # Получаем данные блока питания
        total_power_consumption = sum(
            db.get_component_details(db.get_id_by_name(component[0])).get("tdp", 0)
            for component in build.values()
            if isinstance(component, tuple) and len(component) == 2
        )
        if total_power_consumption > psu_details["power"]:
            compatibility_issues.append(
                f"Общее энергопотребление системы ({total_power_consumption} Вт) превышает мощность блока питания ({psu_details['power']} Вт).")

    # 5. Проверка наличия интегрированной графики (если видеокарты нет)
    gpu = build.get("Видеокарта")
    if not gpu[0] and not processor["integrated_graphics"]:
        compatibility_issues.append("Видеокарта отсутствует, но процессор не имеет интегрированной графики.")

    return compatibility_issues

def check_graphics_card_compatibility(graphics_card, build):
    """
    Проверяет совместимость видеокарты с остальными комплектующими в сборке.

    :param graphics_card: Словарь с характеристиками видеокарты.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с корпусом
    case = build.get("Корпус")
    if case[0]:
        case_details = db.get_component_details(db.get_id_by_name(case[0]))  # Получаем данные корпуса

        # Длина видеокарты
        if graphics_card["length"] > case_details["gpu_max_length"]:
            compatibility_issues.append(
                f"Длина видеокарты ({graphics_card['length']} мм) превышает допустимую длину для корпуса ({case_details['gpu_max_length']} мм).")

    # 2. Проверка совместимости с блоком питания
    psu = build.get("Блок питания")
    if psu[0]:
        psu_details = db.get_component_details(db.get_id_by_name(psu[0]))  # Получаем данные блока питания

        # Требуемые разъемы питания
        required_connectors = graphics_card["power_connectors"].split(", ")
        available_connectors = psu_details["pci_e_connectors"].split(", ")
        for connector in required_connectors:
            if connector not in available_connectors:
                compatibility_issues.append(
                    f"Требуемый разъем питания видеокарты ({connector}) отсутствует в блоке питания.")

        # Рекомендуемая мощность блока питания
        total_power_consumption = sum(
            db.get_component_details(db.get_id_by_name(component[0])).get("tdp", 0)
            for component in build.values()
            if isinstance(component, tuple) and len(component) == 2
        )
        if total_power_consumption > psu_details["power"]:
            compatibility_issues.append(
                f"Общее энергопотребление системы ({total_power_consumption} Вт) превышает мощность блока питания ({psu_details['power']} Вт).")

    # 3. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы

        # Версия PCI Express
        if graphics_card["pci_express_version"] != motherboard_details["pci_express_version"]:
            compatibility_issues.append(
                f"Версия PCI Express видеокарты ({graphics_card['pci_express_version']}) не совместима с материнской платой ({motherboard_details['pci_express_version']}).")

    return compatibility_issues

def check_motherboard_compatibility(motherboard, build):
    """
    Проверяет совместимость материнской платы с остальными комплектующими в сборке.

    :param motherboard: Словарь с характеристиками материнской платы.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с процессором
    processor = build.get("Процессор")
    if processor[0]:
        processor_details = db.get_component_details(db.get_id_by_name(processor[0]))  # Получаем данные процессора

        # Сокет
        if motherboard["socket"] != processor_details["socket"]:
            compatibility_issues.append(
                f"Сокет материнской платы ({motherboard['socket']}) не совместим с процессором ({processor_details['socket']}).")

        # Тип оперативной памяти
        if motherboard["memory_type"] != processor_details["memory_type"]:
            compatibility_issues.append(
                f"Тип памяти материнской платы ({motherboard['memory_type']}) не совместим с процессором ({processor_details['memory_type']}).")

        # Версия PCI Express
        if motherboard["pci_express_version"] != processor_details["pci_express_version"]:
            compatibility_issues.append(
                f"Версия PCI Express материнской платы ({motherboard['pci_express_version']}) не совместима с процессором ({processor_details['pci_express_version']}).")

    # 2. Проверка совместимости с оперативной памятью
    ram = build.get("Оперативная память")
    if ram[0]:
        ram_details = db.get_component_details(db.get_id_by_name(ram[0]))  # Получаем данные оперативной памяти

        # Количество слотов RAM
        if ram_details["modules_count"] > motherboard["memory_slots"]:
            compatibility_issues.append(
                f"Количество модулей оперативной памяти ({ram_details['modules_count']}) превышает количество слотов на материнской плате ({motherboard['memory_slots']}).")

        # Максимальная частота памяти
        max_memory_frequency = int(motherboard["supported_ram_frequencies"].split(", ")[-1])
        if ram_details["frequency"] > max_memory_frequency:
            compatibility_issues.append(
                f"Частота оперативной памяти ({ram_details['frequency']} МГц) превышает поддерживаемую материнской платой ({max_memory_frequency} МГц).")

        # Максимальный объем оперативной памяти
        total_ram_capacity = ram_details["capacity"]
        if total_ram_capacity > motherboard["max_memory_capacity"]:
            compatibility_issues.append(
                f"Общий объем оперативной памяти ({total_ram_capacity} ГБ) превышает поддерживаемый материнской платой ({motherboard['max_memory_capacity']} ГБ).")

    # 3. Проверка совместимости с видеокартой
    gpu = build.get("Видеокарта")
    if gpu[0]:
        gpu_details = db.get_component_details(db.get_id_by_name(gpu[0]))  # Получаем данные видеокарты

        # Версия PCI Express
        if motherboard["pci_express_version"] != gpu_details["pci_express_version"]:
            compatibility_issues.append(
                f"Версия PCI Express материнской платы ({motherboard['pci_express_version']}) не совместима с видеокартой ({gpu_details['pci_express_version']}).")

    # 4. Проверка совместимости с корпусом
    case = build.get("Корпус")
    if case[0]:
        case_details = db.get_component_details(db.get_id_by_name(case[0]) ) # Получаем данные корпуса

        # Форм-фактор
        supported_form_factors = case_details["form_factor_support"].split(", ")
        if motherboard["form_factor"] not in supported_form_factors:
            compatibility_issues.append(
                f"Форм-фактор материнской платы ({motherboard['form_factor']}) не поддерживается корпусом.")

    return compatibility_issues

def check_ram_compatibility(ram, build):
    """
    Проверяет совместимость оперативной памяти с остальными комплектующими в сборке.

    :param ram: Словарь с характеристиками оперативной памяти.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы

        # Тип памяти
        if ram["type"] != motherboard_details["memory_type"]:
            compatibility_issues.append(
                f"Тип памяти ({ram['type']}) не совместим с материнской платой ({motherboard_details['memory_type']}).")

        # Общий объем памяти
        if ram["capacity"] > motherboard_details["max_memory_capacity"]:
            compatibility_issues.append(
                f"Общий объем памяти ({ram['capacity']} ГБ) превышает поддерживаемый материнской платой ({motherboard_details['max_memory_capacity']} ГБ).")

        # Количество модулей
        if ram["modules_count"] > motherboard_details["memory_slots"]:
            compatibility_issues.append(
                f"Количество модулей памяти ({ram['modules_count']}) превышает количество слотов на материнской плате ({motherboard_details['memory_slots']}).")

        # Частота памяти
        max_memory_frequency = int(motherboard_details["supported_ram_frequencies"].split(", ")[-1])
        if ram["frequency"] > max_memory_frequency:
            compatibility_issues.append(
                f"Частота памяти ({ram['frequency']} МГц) превышает поддерживаемую материнской платой ({max_memory_frequency} МГц).")

    # 2. Проверка совместимости с процессором
    processor = build.get("Процессор")
    if processor[0]:
        processor_details = db.get_component_details(db.get_id_by_name(processor[0]))  # Получаем данные процессора

        # Тип памяти
        if ram["type"] != processor_details["memory_type"]:
            compatibility_issues.append(
                f"Тип памяти ({ram['type']}) не совместим с процессором ({processor_details['memory_type']}).")

    return compatibility_issues

def check_storage_compatibility(storage, build):
    """
    Проверяет совместимость накопителя (SSD/HDD) с остальными комплектующими в сборке.

    :param storage: Словарь с характеристиками накопителя.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы

        # Интерфейс подключения
        supported_interfaces = motherboard_details["m2_slots"] > 0 and "NVMe PCIe" or "SATA III"
        if storage["interface"] not in supported_interfaces:
            compatibility_issues.append(
                f"Интерфейс накопителя ({storage['interface']}) не совместим с материнской платой ({supported_interfaces}).")

        # Форм-фактор (для M.2)
        if storage["form_factor"].startswith("M.2") and motherboard_details["m2_slots"] <= 0:
            compatibility_issues.append(
                f"Накопитель форм-фактора {storage['form_factor']} не поддерживается материнской платой.")

    # 2. Проверка совместимости с корпусом
    case = build.get("Корпус")
    if case[0]:
        case_details = db.get_component_details(db.get_id_by_name(case[0]))  # Получаем данные корпуса

        # Форм-фактор
        if storage["form_factor"] == "3.5\"" and case_details["drive_bays_3_5"] <= 0:
            compatibility_issues.append(f"Накопитель форм-фактора {storage['form_factor']} не поддерживается корпусом.")
        elif storage["form_factor"] == "2.5\"" and case_details["drive_bays_2_5"] <= 0:
            compatibility_issues.append(f"Накопитель форм-фактора {storage['form_factor']} не поддерживается корпусом.")


    # 3. Проверка совместимости с блоком питания (для HDD)
    psu = build.get("Блок питания")
    if psu[0] and storage["type"] == "HDD":
        psu_details = db.get_component_details(db.get_id_by_name(psu[0]))  # Получаем данные блока питания

        # Потребление энергии
        total_power_consumption = sum(
            db.get_component_details(db.get_id_by_name(component[0])).get("tdp", 0)
            for component in build.values()
            if isinstance(component, tuple) and len(component) == 2
        )
        if storage["power_consumption"] + total_power_consumption > psu_details["power"]:
            compatibility_issues.append(
                f"Общее энергопотребление системы ({total_power_consumption} Вт) превышает мощность блока питания ({psu_details['power']} Вт).")

    return compatibility_issues

def check_power_supply_compatibility(power_supply, build):
    """
    Проверяет совместимость блока питания с остальными комплектующими в сборке.

    :param power_supply: Словарь с характеристиками блока питания.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с корпусом
    case = build.get("Корпус")
    if case[0]:
        case_details = db.get_component_details(db.get_id_by_name(case[0]))  # Получаем данные корпуса

        # Форм-фактор
        if power_supply["form_factor"] not in case_details["psu_form_factor"].split(", "):
            compatibility_issues.append(
                f"Форм-фактор блока питания ({power_supply['form_factor']}) не совместим с корпусом.")

    # 2. Проверка мощности блока питания
    total_power_consumption = sum(
        db.get_component_details(db.get_id_by_name(component[0])).get("tdp", 0)
        for component in build.values()
        if isinstance(component, tuple) and len(component) == 2
    )
    if total_power_consumption > power_supply["power"]:
        compatibility_issues.append(
            f"Общее энергопотребление системы ({total_power_consumption} Вт) превышает мощность блока питания ({power_supply['power']} Вт).")

    # 3. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        # Разъемы питания материнской платы
        if power_supply["main_connector"] != "24-pin ATX":
            compatibility_issues.append(
                f"Основной разъем блока питания ({power_supply['main_connector']}) не совместим с материнской платой.")

    # 4. Проверка совместимости с видеокартой
    gpu = build.get("Видеокарта")
    if gpu[0]:
        gpu_details = db.get_component_details(db.get_id_by_name(gpu[0]))  # Получаем данные видеокарты

        # Разъемы питания видеокарты
        required_gpu_connectors = gpu_details["power_connectors"].split(", ")
        available_gpu_connectors = power_supply["pci_e_connectors"].split(", ")
        for connector in required_gpu_connectors:
            if connector not in available_gpu_connectors:
                compatibility_issues.append(
                    f"Требуемый разъем питания видеокарты ({connector}) отсутствует в блоке питания.")

    # 5. Проверка количества SATA разъемов
    storage = build.get("SSD") or build.get("Жесткий диск")
    if storage[0]:
        storage_details = db.get_component_details(db.get_id_by_name(storage[0]))  # Получаем данные накопителя

        # Количество SATA разъемов
        if storage_details["type"] == "HDD" or storage_details["interface"] == "SATA III":
            if power_supply["sata_connectors"] < 1:
                compatibility_issues.append(f"Недостаточно SATA разъемов для подключения накопителя.")

    return compatibility_issues

def check_case_compatibility(case, build):
    """
    Проверяет совместимость корпуса с остальными комплектующими в сборке.

    :param case: Словарь с характеристиками корпуса.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы

        # Форм-фактор
        supported_form_factors = case["form_factor_support"].split(", ")
        if motherboard_details["form_factor"] not in supported_form_factors:
            compatibility_issues.append(
                f"Форм-фактор материнской платы ({motherboard_details['form_factor']}) не поддерживается корпусом.")

    # 2. Проверка совместимости с видеокартой
    gpu = build.get("Видеокарта")
    if gpu[0]:
        gpu_details = db.get_component_details(db.get_id_by_name(gpu[0]))  # Получаем данные видеокарты

        # Максимальная длина видеокарты
        if gpu_details["length"] > case["gpu_max_length"]:
            compatibility_issues.append(
                f"Длина видеокарты ({gpu_details['length']} мм) превышает допустимую длину для корпуса ({case['gpu_max_length']} мм).")

    # 3. Проверка совместимости с системой охлаждения
    cooler = build.get("Охлаждение")
    if cooler[0]:
        cooler_details = db.get_component_details(db.get_id_by_name(cooler[0]))  # Получаем данные системы охлаждения

        # Максимальная высота кулера
        if int(cooler_details["size"].split("x")[2]) > case["cpu_cooler_max_height"]:
            compatibility_issues.append(
                f"Высота системы охлаждения ({cooler_details['size'].split('x')[2]} мм) превышает допустимую высоту для корпуса ({case['cpu_cooler_max_height']} мм).")

    # 4. Проверка совместимости с блоком питания
    psu = build.get("Блок питания")
    if psu[0]:
        psu_details = db.get_component_details(db.get_id_by_name(psu[0]))  # Получаем данные блока питания

        # Форм-фактор блока питания
        if psu_details["form_factor"] not in case["psu_form_factor"].split(", "):
            compatibility_issues.append(
                f"Форм-фактор блока питания ({psu_details['form_factor']}) не поддерживается корпусом.")

    # 5. Проверка количества отсеков для накопителей
    storage = build.get("SSD") or build.get("Жесткий диск")
    if storage[0]:
        storage_details = db.get_component_details(db.get_id_by_name(storage[0]))  # Получаем данные накопителя

        # Количество отсеков для SSD/HDD
        if storage_details["form_factor"] == "3.5\"" and case["drive_bays_3_5"] <= 0:
            compatibility_issues.append(f"Недостаточно отсеков для накопителя форм-фактора 3.5\".")
        elif storage_details["form_factor"] == "2.5\"" and case["drive_bays_2_5"] <= 0:
            compatibility_issues.append(f"Недостаточно отсеков для накопителя форм-фактора 2.5\".")

    return compatibility_issues

def check_cooler_compatibility(cooler, build):
    """
    Проверяет совместимость системы охлаждения с остальными комплектующими в сборке.

    :param cooler: Словарь с характеристиками системы охлаждения.
    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    # 1. Проверка совместимости с процессором
    processor = build.get("Процессор")
    if processor[0]:
        processor_details = db.get_component_details(db.get_id_by_name(processor[0]))  # Получаем данные процессора

        # Совместимость сокетов
        compatible_sockets = cooler["sockets_compatibility"].split(", ")
        if processor_details["socket"] not in compatible_sockets:
            compatibility_issues.append(f"Кулер не поддерживает сокет процессора ({processor_details['socket']}).")

        # Поддерживаемый TDP
        if processor_details["tdp"] > cooler["tdp_support"]:
            compatibility_issues.append(
                f"TDP процессора ({processor_details['tdp']} Вт) превышает поддерживаемое охлаждением ({cooler['tdp_support']} Вт).")

    # 2. Проверка совместимости с корпусом
    case = build.get("Корпус")
    if case[0]:
        case_details = db.get_component_details(db.get_id_by_name(case[0]))  # Получаем данные корпуса

        # Максимальная высота кулера
        if int(cooler["size"].split("x")[2])     > case_details["cpu_cooler_max_height"]:
            compatibility_issues.append(
                f"Высота кулера ({cooler['size'].split('x')[2]} мм) превышает допустимую высоту для корпуса ({case_details['cpu_cooler_max_height']} мм).")

    # 3. Проверка совместимости с материнской платой
    motherboard = build.get("Материнская плата")
    if motherboard[0]:
        motherboard_details = db.get_component_details(db.get_id_by_name(motherboard[0]))  # Получаем данные материнской платы

        # Разъемы вентиляторов
        fan_connector = cooler["fan_connector"]
        supported_connectors = motherboard_details["fan_headers"]
        if fan_connector != supported_connectors:
            compatibility_issues.append(f"Тип разъема вентилятора ({fan_connector}) не совместим с материнской платой.")

    return compatibility_issues

def check_full_build_compatibility(build):
    """
    Проверяет совместимость всей сборки.

    :param build: Словарь текущей сборки.
    :return: Список проблем совместимости.
    """
    compatibility_issues = []

    for category, component in build.items():
        if isinstance(component, tuple) and len(component) == 2:
            component_name = component[0]
            component_id = db.get_id_by_name(component_name)

            if component_id is None:
                return

            component_details = db.get_component_details(component_id)
            print(build)
            if category == "Процессор":
                compatibility_issues.extend(check_processor_compatibility(component_details, build))
            elif category == "Видеокарта":
                compatibility_issues.extend(check_graphics_card_compatibility(component_details, build))
            elif category == "Материнская плата":
                compatibility_issues.extend(check_motherboard_compatibility(component_details, build))
            elif category == "Оперативная память":
                compatibility_issues.extend(check_ram_compatibility(component_details, build))
            elif category in ["SSD", "Жесткий диск"]:
                compatibility_issues.extend(check_storage_compatibility(component_details, build))
            elif category == "Блок питания":
                compatibility_issues.extend(check_power_supply_compatibility(component_details, build))
            elif category == "Корпус":
                compatibility_issues.extend(check_case_compatibility(component_details, build))
            elif category == "Охлаждение":
                compatibility_issues.extend(check_cooler_compatibility(component_details, build))

    return compatibility_issues
