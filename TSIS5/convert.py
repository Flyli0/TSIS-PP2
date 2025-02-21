import json
import re
data = dict({})
b = []
i=0
with open('row.txt',encoding="utf8") as f:
    text = f.read()
    data["Филиал"] = re.search(r'Филиал (.+)', text).group(1)
    data["БИН"] = re.search(r'БИН (\d+)', text).group(1)
    data["Чек №"] = re.search(r'Чек №(\d+)', text).group(1)
    data["Дата и время"] = re.search(r'Время: (.+)', text).group(1)
    data["Адрес"] = re.search(r'г\. .+?, (.+)', text).group(1)
    data["Оператор фискальных данных"] = re.search(r'Оператор фискальных данных: (.+)', text).group(1)
    itms = re.findall(r'\d+\.\n(.+)\n(\d+,\d+) x (\d+,\d+)\n\d+,\d+\n.*\n(\d+,\d+)',text)
    for item in itms:
        name, quantity, price, total = item
        b.append({
            "Название": name.strip(),
            "Кол-во": float(quantity.replace(',', '.')),
            "Цена за единицу": float(price.replace(' ', '').replace(',', '.')),
            "Общая стоимость": float(total.replace(' ', '').replace(',', '.'))
        })
    data["Товары"] = b
    print(data['Товары'])
    data["Итого"] = float(re.search(r'ИТОГО:\n([\d\s]+,\d+)', text).group(1).replace(' ', '').replace(',', '.'))
    data["НДС 12%"] = float(re.search(r'в т\.ч\. НДС 12%:\n([\d\s]+,\d+)', text).group(1).replace(' ', '').replace(',', '.'))
    with open('a.json','w',encoding="utf8") as a:
        json.dump(data,a,indent=4,ensure_ascii=False)