def typeBasedTransformer(informatsiya):
    converted = {}
    
    for kalita, qiymatb in informatsiya.items():
        
        if isinstance(kalita, (int, float)):
            converted[kalita] = qiymatb ** 2
        elif isinstance(kalita, bool):
            converted[kalita] = not qiymatb
        elif isinstance(qiymatb, (list, tuple)):
            converted[kalita] = qiymatb[::-1]
        elif isinstance(qiymatb, dict):
            converted[kalita] = {s: t for t, s in qiymatb.items()}
        elif isinstance(qiymatb, str):
            converted[kalita] = qiymatb[::-1]
        
        else:
            converted[kalita] = qiymatb
            
    return converted

# Example usage:
informatsiya = {
    'a3': 3,
    'b3': 1.5,
    'c3': "Come",
    'd3': False,
    'e3': [3, 76, 2],
    'f3': {"mb": 3, "tm": 8},
    'g3': None,
    'h3': (1, 9, 2)
}

returning1 = typeBasedTransformer(informatsiya)
print(returning1)
