def make_car(model, type, *price, **kwargs):
    print('Making a car for', model)
    kwargs['model'] = model
    kwargs['type'] = type
    if price:
        kwargs['price'] = price[0]
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)