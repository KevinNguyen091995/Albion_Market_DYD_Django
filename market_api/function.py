import json

def put_item_map():
    with open('assets/items_map.json', 'r') as f:
        data = json.load(f)

        for key, value in data.items():
            ItemDescriptionModel.objects.create(unique_name=key, item_name=value)


put_item_map()


data_categories = ['weapon', 'mount', 'equipmentitem', 'consumableitem', 'consumablefrominventoryitem', 'simpleitem', 'trackingitem' 'farmableitem', 'hideoutitem']

def put_item_db():
    with open('assets/items.json', 'r') as f:
        weapon = json.load(f)
        
        for data in weapon['items']:
            if data in data_categories:
                for item in weapon['items'][data]:
                    if (type(item)) == dict:
                        try:
                            print(item['@uniquename'])
                            ItemModel.objects.create(unique_name=item['@uniquename'], 
                                                    tier=item['@tier'], 
                                                    image_url=f"https://render.albiononline.com/v1/item/{item['@uniquename']}", 
                                                    item_class=data.replace('item', ""), 
                                                    item_category=item['@shopcategory'],
                                                    item_sub_category = item['@shopsubcategory1'])
                        except (IntegrityError, DataError):
                            pass
                                        
                
put_item_db()