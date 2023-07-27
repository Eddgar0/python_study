import csv

cars = [
    ('año', 'marca','modelo', 'transmision'),
    (2016, 'Hyundai', 'Sonata', 'tritonica'),
    (2015, 'Ford','Escape', 'manual'),
    (2012, 'Honda','Civic', 'manual')
]

with open('carros.csv', 'w',newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(cars)

with open('carros.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for l in reader:
        print(f'tengo un carro {l[1]} {l[2]} de año {l[0]} con transmision {l[3]}')
