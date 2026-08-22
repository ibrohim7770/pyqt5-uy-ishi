def function(shops):
    if not shops:
        return " "

    ls = shops[0]
    maks = len(shops[0]["products"])
    
    for x in shops:
        a = len(x["products"])
        if a > maks:
            maks = a
            ls = x
            
    return ls["name"]

if __name__ == "__main__":
    shops = [
        {"name": "Shop1", "products": ["apple"]},
        {"name": "Shop2", "products": ["apple", "banana"]},
        {"name": "Shop3", "products": ["apple", "banana", "kiwi"]}
    ]

    print(function(shops))

