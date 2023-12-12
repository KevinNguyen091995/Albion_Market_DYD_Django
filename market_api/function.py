import json

def put_item_map():
    with open('assets/items.json', 'r') as f:
        data = json.load(f)

        for key, value in data.items():
            ItemDescriptionModel.objects.create(unique_name=key, description=value)



def put_weapon_db():
    with open('assets/items.json', 'r') as f:
        weapon = json.load(f)
        
        for data in weapon['items']['weapon']:
            item_instance = ItemDescriptionModel.objects.get(unique_name=data['@uniquename'])

            if data['@shopcategory'] == 'melee':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           item_class='melee', 
                                           item_category=data['@shopsubcategory1'],)
                
            if data['@shopcategory'] == 'magic':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           item_class='magic',
                                           item_category=data['@shopsubcategory1'],)
                
            if data['@shopcategory'] == 'ranged':
                WeaponModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           item_class='ranged',
                                           item_category=data['@shopsubcategory1'],)
                
put_weapon_db()
                
def put_offhand_db():
    with open('assets/items.json', 'r') as f:
        offhand = json.load(f)
        for data in offhand['items']['equipmentitem']:
            item_instance = ItemDescriptionModel.objects.get(unique_name=data['@uniquename'])

            if data['@shopcategory'] == 'offhand':
                OffHandModel.objects.create(unique_name=item_instance, 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           item_class='ranged',
                                           item_category=data['@shopsubcategory1'],)
                
def put_mount_db():
    with open('assets/items.json', 'r') as f:
        offhand = json.load(f)
        for data in offhand['items']['mount']:
            if data['@shopcategory'] == 'mounts':
                print(data)
                MountModel.objects.create(unique_name=data['@uniquename'], 
                                           tier=data['@tier'], 
                                           image_url=f"https://render.albiononline.com/v1/item/{data['@uniquename']}", 
                                           item_class='mount',
                                           item_category=data['@shopsubcategory1'],)

with open('assets/items.json', 'r') as f:
    offhand = json.load(f)
    for data in offhand['items']['mount']:
        if data['@shopcategory'] == 'mounts':
            print(data)


