import json

with open('C:\\Users\\Kevin\\Desktop\\Albion API Market\\albion-market-django\\albion_django\\market_api\\items.json', 'r') as f:
    weapon = json.load(f)
    
    for data in weapon['items']['weapon']:
        if data['@shopcategory'] == 'melee':
            WeaponModel.objects.create(unique_name=data['@uniquename'], tier=data['@tier'], image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", weapon_class='melee')
        if data['@shopcategory'] == 'magic':
            WeaponModel.objects.create(unique_name=data['@uniquename'], tier=data['@tier'], image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", weapon_class='magic')
        if data['@shopcategory'] == 'ranged':
            WeaponModel.objects.create(unique_name=data['@uniquename'], tier=data['@tier'], image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", weapon_class='ranged')
