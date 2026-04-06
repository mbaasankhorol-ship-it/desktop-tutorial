def cargo_price_calculator(height, depth, length, weight, kg_price=3500 ,m3_price=3000):
    
    if height <= 0 or depth <= 0 or length <= 0:
        raise ValueError("Hemjee buruu")
    
    if weight <= 0:
        raise ValueError("Jin buruu")
    
    volume = (height * depth * length) / 5000
    chargeable_weight = max(volume, weight)
    
    return chargeable_weight * kg_price
