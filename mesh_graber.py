import bpy
import pathlib



wanted_chars_list = ["billie", "woolfred", "miss_shearlington" ]
import_list = []
obj_path = "N:\\01_ASSETS\CHARACTERS\\"
scene_collection = bpy.context.scene.collection

def add_object_to_collection(obj_name, obj, scene_collection):
    new_collection_name = obj_name
    new_collection = bpy.data.collections.get(new_collection_name)
    
    if new_collection is None:
        new_collection = bpy.data.collections.new(new_collection_name)
        scene_collection.children.link(new_collection)

    new_collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.make_local(type='SELECT_OBJECT')
    
for obj in bpy.context.scene.objects:
    # Vérifier si le nom de l'objet contient l'un des mots dans search_list
    for mot in wanted_chars_list:
        if mot.lower() in obj.name.lower():
            if mot.lower() not in import_list:
                import_list.append(mot)
            else:
                continue

print(import_list)
for obj_name in import_list:
    blend_file_path = obj_path + str(obj_name.upper()) + "\\05_RENDER\\" + f"{obj_name}-1-1.blend"
    print(blend_file_path)

    # Load and link the objects from the Blender file
    with bpy.data.libraries.load(blend_file_path, link=True) as (data_from, data_to):
        data_to.objects = data_from.objects

    # Add objects to the scene collection if their names start with the corresponding object name"
    scene = bpy.context.scene

    for obj in data_to.objects:
        print(obj.name)
        # Filter objects that start with the capitalized obj_name"
        if obj.name.lower().startswith(obj_name.lower()):
            add_object_to_collection(obj_name, obj, scene_collection)
            

            
    
    