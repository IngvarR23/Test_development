geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def geo_logs_list(test_list):
    for geo in reversed(geo_logs):
        visit_values = list(geo.values())
        if 'Россия' not in visit_values[0]:
            geo_logs.remove(geo)
        return test_list

    # Не понял , что именно сдесь нужно делать
    # Отправляю в таком виде , потому-что нужно уезжать
    

