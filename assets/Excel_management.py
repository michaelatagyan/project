import pandas as pd
import xlwings as xw


# from main import tools_w

class Excel_management():
    def __init__(self):
        self.wb = None
        self.sheet = None

    def to_excel(self, data):
        df = pd.DataFrame(data)
        df.columns = ['Слово', 'Правило', 'С пропущенной буквой', 'Буква']
        self.wb = xw.Book()
        self.sheet = self.wb.sheets.active
        # sheet.range('A1').value = df

        self.sheet.range('A1').value = df.to_numpy()  # Записываем только значения
        self.sheet.range('A1').value = df.columns.tolist()  # Записываем заголовки
        self.sheet.range('A2').value = df.values

    def check_excel_data(self, data):
        errors = {}
        indexation_d = {}
        required_headers = ['Слово', 'Правило', 'С пропущенной буквой', 'Буква']
        df = pd.DataFrame(data.value)
        cols = df.shape[1]
        # Проверяю количество столбцов
        # Если меньше 4, то ошибка
        if cols < 4:
            return  # ERROR

        # Если больше или равно, то проверяем на наличие нужных заголовков
        # В цикле проверяем наличие значения текущей ячейки в списке заголовков
        headers = df.iloc[0]
        for i, value in enumerate(headers):
            if value in required_headers:
                indexation_d[value] = i
                required_headers.remove(value)

        # Проверить сколько столбцов осталось в DataFrame, а также их порядок
        if required_headers or not (indexation_d['Слово'] < indexation_d['Правило']
                                    < indexation_d['С пропущенной буквой'] < indexation_d['Буква']):
            return  # ERROR

        cols = dict.fromkeys(list(range(len(df.columns))))
        for i in range(len(headers)):
            if i == indexation_d['Слово']:
                cols[i] = notEmpty(df[i], 1)
                errors[i] = get_incorrect_indices(cols[i])
                pass
            elif i == indexation_d['Правило']:
                cols[i] = ISrule(df[i])
                errors[i] = get_incorrect_indices(cols[i])
                errors[i].pop(0)
                pass
            elif i == indexation_d['С пропущенной буквой']:
                cols[i] = notEmpty(df[i], 1)
                errors[i] = get_incorrect_indices(cols[i])
                pass
            elif i == indexation_d['Буква']:
                cols[i] = oneORempty(df[i], 1)
                errors[i] = get_incorrect_indices(cols[i])
                errors[i].pop(0)
                pass
        self.highlightErrors(data, errors)

    def from_excel(self):
        if self.sheet:
            ws = self.sheet
            data = ws.used_range
            # # Получаем данные
            # df = pd.DataFrame(data)  # Используем первую строку как заголовки
            self.check_excel_data(data)
            # print(df)

    def highlightErrors(self, data, err):
        hide = True

        if data is not None:
            data.api.EntireRow.Hidden = True

        first_row = data.rows[0]
        first_row.api.EntireRow.Hidden = False

        # Создаем пустой список для хранения ссылок на ячейки
        ranges = []

        # Добавляем каждую ячейку из err в список
        for col in err.keys():
            for row in err[col]:
                cell = data(1 + row, 1 + col).api
                ranges.append(cell)

        # Создаем список ranges с помощью генератора списка
        # ranges = [data(1 + row, 1 + col).api for row in err.keys() for col in err[row]]

        # Создаем несвязанный диапазон с помощью метода Union
        union_range = None
        xl = data.sheet.book.app
        for i in range(0, len(ranges), 29):  # Изменено на 29
            try:
                if union_range is None:
                    union_range = xl.api.Union(*ranges[i:i + 29])
                else:
                    union_range = xl.api.Union(union_range, *ranges[i:i + 29])
            except Exception as e:
                print(str(e))

        # Применяем изменения к диапазону
        union_range.Interior.Color = 0x0000ff
        union_range.Font.Color = 0xffffff
        union_range.EntireRow.Hidden = False



Excel = Excel_management()


# Функция проверки, является ли значение целым числом
def notEmpty(df, val):
    return df.apply(lambda x: len(x) >= val if x is not None else False)


def get_incorrect_indices(col):
    return col[col == False].index.tolist()


def ISrule(df):
    return df.apply(lambda x: x in ['Ъ или Ь', 'И или Е', 'Ы или И', 'З или С'])


def oneORempty(df, val):
    return df.apply(lambda x: len(x) <= val if x is not None else False)
