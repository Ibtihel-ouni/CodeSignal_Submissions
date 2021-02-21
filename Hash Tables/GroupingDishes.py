def groupingDishes(dishes):
    d = {}
    for dish in dishes:
        dish_name = dish.pop(0)
        for ingd in dish:
            d[ingd] = d.get(ingd, []) + [dish_name]
            
    return sorted([i] + sorted(v) for i,v in d.items() if len(v) > 1)
