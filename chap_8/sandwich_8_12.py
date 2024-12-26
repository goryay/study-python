def make_sandwich(name, *ingredients):
    print(f"Lets make a sandwich: {name}")
    for ingredient in ingredients:
        print(f"\t{ingredient}")


make_sandwich('Бутер с икрой', 'хлеб', 'масло', 'икра')
make_sandwich('С колбасой и сыром', 'хлеб', 'масло', 'колбаса', 'сыр')
make_sandwich('С зеленью', 'сыр плавленный', 'лист салата', 'помидоры')
