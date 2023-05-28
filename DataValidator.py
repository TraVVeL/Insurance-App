import datetime
import re


class DataValidator:
    def __init__(self, *arg, n=4):
        self.arg = arg
        self.n = n

    def is_date(self):
        date = str(*self.arg)
        try:
            datetime.datetime.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    def is_full_name(self):
        full_name = str(*self.arg)
        # Проверяем, что в строке только буквы и пробелы
        if not all(char.isalpha() or char.isspace() for char in full_name):
            return False

        # Проверяем, что в строке минимум два слова
        words = full_name.split()
        if len(words) != 3:
            return False

        if len(words) < 2:
            return False
        return True

    def is_vin(self):
        """
        Функция для проверки VIN-номера.
        :return: True, если VIN-номер верный, False - в противном случае
        """
        vin = str(*self.arg)
        return len(vin) == 17

    def is_grz(self):
        """
        Проверяет корректность государственного регистрационного знака (ГРЗ)
        :return: bool - True, если ГРЗ корректный, иначе False
        """
        grz = str(*self.arg).upper()
        pattern = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
        return bool(re.match(pattern, grz))

    def is_digit(self, n):
        # Проверка максимальной длины строки числа
        digit = str(*self.arg)
        if len(digit) != n:
            return False
        try:
            # Преобразование input в число
            float(digit)
            return True
        except ValueError:
            # Если не удалось преобразовать input в число, возвращаем False
            return False

    def is_driver_license(self):
        # Проверка длины серии и номера ВУ
        try_split = str(*self.arg)

        if ' ' in try_split and len(list(try_split.split())) == 2:
            series, number = try_split.split()
            if len(series) != 4 or len(number) != 6:
                return False

            # Проверка, что номер ВУ состоит только из цифр
            if not number.isdigit():
                return False

            # Проверка первых двух символов серии ВУ
            first_two_symbols = series[:2]
            if first_two_symbols not in ('01', '02', '03', '04', '05', '06', '07', '08',
                                         '09', '10', '11', '12', '13', '14', '15', '16',
                                         '17', '18', '19', '20', '21', '22', '23', '24',
                                         '25', '26', '27', '28', '29', '30', '31', '32',
                                         '33', '34', '35', '36', '37', '38', '39', '40'):
                return False

            # Проверка, что остальные символы серии ВУ состоят только из букв
            if not series[2:].isalpha():
                return False

            # Если все проверки пройдены успешно, возвращаем True
            return True

    def is_float(self):
        float_n = str(*self.arg)
        try:
            # Преобразование введенного значения в float
            float(float_n)

            # Проверка, что значение представляет собой число с двумя знаками после точки
            if float(float_n) > 1:
                return False
            # Если все проверки пройдены успешно, возвращаем True
            return True
        except ValueError:
            # Если не удалось преобразовать введенное значение в float, возвращаем False
            return False

    def is_date_by_words(self):
        date = str(*self.arg)
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября', 'декабря']
        try:
            day, month, year = date.split()
            if int(day) < 1 or int(day) > 31:
                return False
            if month not in months:
                return False
            if int(year) < datetime.datetime.now().year:
                return False
        except ValueError:
            return False

        return True

    def is_phone(self):
        phone_number = str(*self.arg)
        digits = [char for char in phone_number if char.isdigit()]
        if len(digits) != 11:
            return False
        formatted_number = "".join(digits)
        if formatted_number.startswith("0") or formatted_number.startswith("1"):
            return False
        return True

    def simple_valid(self):
        return True
