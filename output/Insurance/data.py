from datetime import datetime

########################################################################################################################
########################################################################################################################

""" ЗАДАНИЕ ЦВЕТОВ ДЛЯ ИСПОЛЬЗОВАНИЯ В ГЛАВНОМ ОКНЕ ПРОГРАММЫ"""

########################################################################################################################
########################################################################################################################

LIGHT_GRAY = '#c3c3c3'
AQUA = '#009999'
BACKGROUND_MAIN = '#999999'
BACKGROUND_MENU = '#c3c3c3'
RED = "#990000"
GREEN = '#336600'
ENTRY_W, ENTRY_H = 400, 45
LABEL_W = 250

########################################################################################################################
########################################################################################################################

""" ENTRY, PLACEHOLDER, FRAME DATA ЗАПОЛНЕНИЯ ДЛЯ ОФОМЛЕНИЯ ПОЛИСА"""

########################################################################################################################
########################################################################################################################

cday = datetime.now().day
cmonth = datetime.now().month - 1
cyear = datetime.now().year
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
          'августа', 'сентября', 'октября', 'ноября', 'декабря']

LABEL_POLICY_1 = ["Дата начала действия",
                  "Дата окончания действия",
                  "Дата начала страхования",
                  "Дата окончания страхования",
                  "ФИО",
                  "Владелец автомобиля",
                  "Марка автомобиля",
                  "Модель автомобиля",
                  "Идентификационный номер автомобиля",
                  "Государственный регистрационный номер",
                  "Вид документа"]

LABEL_POLICY_2 = ["Серия",
                  "Номер",
                  "Допущенный к управлению",
                  "Водительское удостоверение",
                  "Коэффициент бонус-малус",
                  "Дата заключения договора"
                  ]

PLACEHOLDER_POLICY_1 = ['ДД.ММ.ГГГГ',
                        'ДД.ММ.ГГГГ',
                        'ДД.ММ.ГГГГ',
                        'ДД.ММ.ГГГГ',
                        'Фамилия Имя Отчество',
                        'Фамилия Имя Отчество',
                        'Марка',
                        'Модель',
                        'XXX0-X00X-XXX0-00000',
                        'XOOOXXOO',
                        'Свидетельство о регистрации ТС']
PLACEHOLDER_POLICY_2 = ['XXXX',
                        '260548',
                        'Фамилия Имя Отчество',
                        '00XX 000000',
                        '0.7',
                        f"{cday} {months[cmonth]} {cyear}г."]

ENTRIES_POLICY_DATA = {
    "!entry":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry2":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry3":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry4":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry5":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry6":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry7":
        ['simple_valid', 'Ошибка'],
    "!entry8":
        ['simple_valid', 'Ошибка'],
    "!entry9":
        ['is_vin', 'ВИН имеет неверный синтаксис, используйте формат: XXX0-X00X-XXX0-00000'],
    "!entry10":
        ['is_grz', 'ГРН имеет неверный синтаксис, используйте формат: X000XX00, используйте русские буквы'],
    "!entry11":
        ['simple_valid', 'Ошибка'],

    "!entry12":
        [{'is_digit': dict(n=4)}, 'Серия имеет неверный синтаксис, серия состоит как минимум из 4 цифр'],
    "!entry13":
        [{'is_digit': dict(n=6)}, 'Номер имеет неверный синтаксис, номер состоит как минимум из 6 цифр'],
    "!entry14":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry15":
        ['is_driver_license', 'ВУ имеет неверный синтаксис, используйте формат: 00XX 000000'],
    "!entry16":
        ['is_float', 'Коэффициент имеет неверный синтаксис, используйте формат 0.7'],
    "!entry17":
        ['is_date_by_words',
         'Дата имеет неверный синтаксис, используйте формат: ЧИСЛО МЕСЯЦ ГОД, где месяц прописывается буквенно']
}

# LIST OF DATA WE WILL NEED TO SORT
SQL_COLUMN_POLICY = ['start_date',
                     'end_date',
                     'insurance_start_date',
                     'insurance_end_date',
                     'full_name',
                     'car_owner',
                     'car_brand',
                     'car_model',
                     'car_id',
                     'car_reg_number',
                     'doc_type',
                     'doc_series',
                     'doc_number',
                     'allowed_to_drive',
                     'driver_license',
                     'bonus_malus',
                     'contract_date']

########################################################################################################################
########################################################################################################################

""" ENTRY, PLACEHOLDER, FRAME DATA ЗАПОЛНЕНИЯ ДЛЯ ОБРАБОТКИ СТРАХОВЫХ СЛУЧАЕВ"""

########################################################################################################################
########################################################################################################################


LABEL_INSURANCE_1 = ["Потерпевший/Выгодоприобретатель",
                     "Адрес (почтовый индекс)",
                     "Государство (РФ для жителей России)",
                     "Населенный пункт, Дом, корпус, квартира",
                     "Номер телефона",
                     "Собственник (ФИО)",
                     "Марка, модель ТС",
                     "Гос. рег. знак ТС",
                     "Идентификационный номер ТС",
                     "Год изготовления",
                     "Серия"]

LABEL_INSURANCE_2 = ["Номер",
                     "Дата выдачи",
                     "Лицо, жизни/здоровью которого \nпричинен вред",
                     "Хар-ер и степень повреждения здоровья",
                     "Дата и время страхового случая",
                     "Адрес места ДТП",
                     "Водитель, управляющий ТС, \nпричинивший вред",
                     "Потерпевший (выгодоприобретатель)",
                     "Дата составления документа"
                     ]

PLACEHOLDER_INSURANCE_1 = ['Иванов Иван сергеевич',
                           '000000',
                           'РФ',
                           'г. Москва ул.Семеновская д.33 к.1 кв.5',
                           '7-XXX-XXX-XX-XX',
                           'Иванов Иван Сергеевич',
                           'ВАЗ 2101',
                           'А001АА777',
                           'XT2106000Y4256418',
                           '1971',
                           '0000']
PLACEHOLDER_INSURANCE_2 = ['000000',
                           'ДД.ММ.ГГГГ',
                           'Иванов Иван Сергеевич',
                           'Перелом руки',
                           "ДД.ММ.ГГГГ",
                           'г. Москва, ул. 7-я Парковая д.7',
                           "Сергеев Степан Афанасьевич",
                           "Иванов И.С",
                           f"{cday} {months[cmonth]} {cyear}г."]

ENTRIES_INSURANCE_DATA = {
    "!entry":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry2":
        [{'is_digit': dict(n=6)}, 'Почтовый адрес имеет неверный синтаксис, используйте формат 000000'],
    "!entry3":
        ['simple_valid', 'Ошибка'],
    "!entry4":
        ['simple_valid', 'Ошибка'],
    "!entry5":
        ['is_phone', 'Телефон имеет неправильный синтаксис, используйте формат: 7-XXX-XXXX-XX-XX'],
    "!entry6":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry7":
        ['simple_valid', 'Ошибка'],
    "!entry8":
        ['is_grz', 'ГРН имеет неверный синтаксис, используйте формат: X000XX00, используйте русские буквы'],
    "!entry9":
        ['is_vin', 'ВИН имеет неверный синтаксис, используйте формат: XXX0-X00X-XXX0-00000'],
    "!entry10":
        [{'is_digit': dict(n=4)}, 'Год изготовления имеет неверный синтаксис, год, должен состоять из 4 цифр'],
    "!entry11":
        [{'is_digit': dict(n=4)}, 'Серия имеет неверный синтаксис, серия состоит как минимум из 4 цифр'],
    "!entry12":
        [{'is_digit': dict(n=6)}, 'Номер имеет неверный синтаксис, номер состоит как минимум из 6 цифр'],
    "!entry13":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry14":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry15":
        ['simple_valid', 'Ошибка'],
    "!entry16":
        ['is_date', 'Дата имеет неверный синтаксис, используйте формат ДД.ММ.ГГГГ'],
    "!entry17":
        ['simple_valid', 'Ошибка'],
    "!entry18":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry19":
        ['is_full_name', 'Имя, Фамилия, Имя имеет неправильный синтаксис, используйте формат: Фамилия Имя Отчество'],
    "!entry20":
        ['is_date_by_words',
         'Дата имеет неверный синтаксис, используйте формат: ЧИСЛО МЕСЯЦ ГОД, где месяц прописывается буквенно']
}

SQL_COLUMN_INSURANCE = ['injured',
                        'postcode',
                        'country',
                        'address',
                        'phone_number',
                        'owner',
                        'mark_model',
                        'vehicle_registration_plate',
                        'vehicle_identification_number',
                        'manufacture',
                        'series',
                        'number',
                        'date_issue',
                        'person_harmed',
                        'health_damage',
                        'insurance_event',
                        'location_accident',
                        'harm_driver',
                        'claimant_beneficiary',
                        'document_creation']

########################################################################################################################
########################################################################################################################

""" ENTRY, PLACEHOLDER, FRAME DATA ЗАПОЛНЕНИЯ ДЛЯ ОФОМЛЕНИЯ ПРЕТЕНЗИЙ"""

########################################################################################################################
########################################################################################################################

LABEL = ['Куда', 'Кому', "Письмо"]

SQL_COLUMN_CLAIM = ['dfrom', 'dto', 'claim']

INSURANCE_TEXT = """
Страхование - это процесс защиты себя, своего имущества и своих близких от потенциальных рисков и потерь. 
Страховая компания предлагает своим клиентам определенные услуги в обмен на плату, которая называется страховой премией.

В настоящее время страхование является обязательным для многих видов деятельности и объектов, таких как автомобили, 
здания и предприятия. Кроме того, страхование может быть полезно для личного использования, например, для защиты 
здоровья, жизни и имущества.

Основная цель страхования - это предотвращение финансовых потерь при возникновении непредвиденных событий, таких как 
аварии, кражи, пожары и травмы. Страховые компании используют математические модели и статистические данные, 
чтобы оценить вероятность возникновения таких событий и установить адекватный уровень страховой премии.

Страхование выполняет несколько функций. Во-первых, оно защищает от финансовых потерь, которые могут быть значительными 
и даже катастрофическими. Например, без страхования автомобиля владелец может быть вынужден заплатить большую сумму за 
ремонт после аварии или замену украденного автомобиля.

Во-вторых, страхование позволяет распределять риски между различными людьми и компаниями. Все клиенты страховой компании 
платят премию, независимо от того, насколько вероятно возникновение непредвиденных событий. Таким образом, риски 
распределяются между всеми клиентами компании, что позволяет снизить финансовое бремя для каждого из них.

Третья функция страхования - это улучшение безопасности. Когда люди знают, что они застрахованы, они могут быть более 
осторожны и предусмотрительны в своих действиях. Например, автомобильные водители могут ездить более аккуратно, зная, 
что они застрахованы, а владельцы домов могут устанавливать системы безопасности, чтобы снизить риск кражи.

Наконец, страхование может помочь в снижении потерь. Например, если дом владельца был поврежден при пожаре, страховая 
компания может оплатить ремонт, что позволит избежать больших финансовых потерь для владельца.

Таким образом, страхование играет важную роль в обществе, помогая людям и компаниям защитить свое имущество и здоровье 
от непредвиденных рисков и потерь, а также улучшить безопасность и снизить потери в случае возникновения этих рисков.
"""
