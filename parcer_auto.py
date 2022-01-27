from openpyxl import load_workbook

wb = load_workbook('avtovoz_cars.xlsx')
sheet = wb["Лист1"]

cells = sheet['A1':'B2155']

marka = input('Введите марку автомобиля:')
est = []
for marka_model in cells:
    marka_in_doc, model = marka_model
    if marka == marka_in_doc.value:
        est.append(f'{marka_in_doc.value} {model.value}')

if est:
    print(*est, sep='\n')

else:
    print('К сожалению, данная марка автомобиля не найдена')