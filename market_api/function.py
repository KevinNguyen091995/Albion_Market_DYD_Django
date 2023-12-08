import json

def put_item_map():
    with open('C:\\Users\\Kevin\\Desktop\\Albion API Market\\albion-market-django\\albion_django\\assets\\items_map.json', 'r') as f:
        data = json.load(f)

        for key, value in data.items():
            ItemDescriptionModel.objects.create(unique_name=key, description=value)



def put_weapon_db():
    with open('C:\\Users\\Kevin\\Desktop\\Albion API Market\\albion-market-django\\albion_django\\assets\\items.json', 'r') as f:
        weapon = json.load(f)
        
        for data in weapon['items']['weapon']:
            item_instance = ItemDescriptionModel.objects.get(unique_name=data['@uniquename'])

            if data['@shopcategory'] == 'melee':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           weapon_class='melee', 
                                           weapon_category=data['@shopsubcategory1'],)
                
            if data['@shopcategory'] == 'magic':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           weapon_class='magic',
                                           weapon_category=data['@shopsubcategory1'],)
                
            if data['@shopcategory'] == 'ranged':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           weapon_class='ranged',
                                           weapon_category=data['@shopsubcategory1'],)

