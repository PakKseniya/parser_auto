from openpyxl import load_workbook

wb = load_workbook('avtovoz_cars.xlsx')
sheet = wb["Лист1"]

cells = sheet['A1':'B2155']

marka = input('Введите марку автомобиля:')

for marka_model in cells:
    if marka == marka_model[0].value:
        print(marka_model[0].value, marka_model[1].value)
    else:
        print('К сожалению, данная марка автомобиля не найдена')
        break



