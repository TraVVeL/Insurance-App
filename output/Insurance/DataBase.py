import sqlite3


def insert_data(data, db_path):
    # создание соединения с базой данных и курсора для выполнения SQL-запросов
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print(db_path)
    if db_path == 'policy.db':
        # создание таблицы, если её нет
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS policy (
            start_date TEXT,
            end_date TEXT,
            insurance_start_date TEXT, 
            insurance_end_date TEXT, 
            full_name TEXT, 
            car_owner TEXT, 
            car_brand TEXT, 
            car_model TEXT, 
            car_id TEXT, 
            car_reg_number TEXT, 
            doc_type TEXT, 
            doc_series TEXT, 
            doc_number TEXT, 
            allowed_to_drive TEXT, 
            driver_license TEXT, 
            bonus_malus TEXT, 
            contract_date TEXT
             );'''
        )

        # добавление данных в таблицу
        for row in data:
            cursor.execute(
                '''INSERT INTO policy 
                (start_date, end_date, insurance_start_date, insurance_end_date, full_name, car_owner, car_brand, 
                car_model, car_id, car_reg_number, doc_type, doc_series, doc_number, allowed_to_drive, driver_license, 
                bonus_malus, contract_date) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
    elif db_path == 'insurance.db':

        cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS insurance (
            injured TEXT,
            postcode TEXT,
            country TEXT,
            address TEXT,
            phone_number TEXT,
            owner TEXT,
            mark_model TEXT,
            vehicle_registration_plate TEXT,
            vehicle_identification_number TEXT,
            manufacture TEXT,
            series TEXT,
            number TEXT,
            date_issue TEXT,
            person_harmed TEXT,
            health_damage TEXT,
            insurance_event TEXT,
            location_accident TEXT,
            harm_driver TEXT,
            claimant_beneficiary TEXT,
            document_creation TEXT
            );'''
        )

        # добавление данных в таблицу
        for row in data:
            cursor.execute(
                '''INSERT INTO insurance (
                injured, postcode, country, address, phone_number, owner, mark_model, vehicle_registration_plate, 
                vehicle_identification_number, manufacture, series, number, date_issue, person_harmed, health_damage, 
                insurance_event, location_accident, harm_driver, claimant_beneficiary, document_creation) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)



    else:
        cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS claim (dfrom, dto, claim);'''
        )

        # добавление данных в таблицу
        for row in data:
            cursor.execute(
                '''INSERT INTO claim (dfrom, dto, claim) VALUES (?, ?, ?)''', row)

    # сохранение изменений и закрытие соединения с базой данных
    conn.commit()
    conn.close()
