import bpy
import os

# Création du chemin vers le niveau précédent et recherche de l'exportation de l'animation
blend_file_path = bpy.path.abspath('//')
blend_file_path = blend_file_path.replace('\\', '/')
folder_path_niveau_moins_un = blend_file_path.rsplit("/", 2)[0]
export_abc_path = folder_path_niveau_moins_un + "/Animation/Export"
print(export_abc_path)

# Définir les personnages pour récupérer leurs Abc
view_layer = bpy.context.view_layer
wanted_chars_list = ["Billie", "Woolfred", "Miss_Shearlington"]

# Fonction pour ajouter le modificateur Mesh Sequence Cache
def add_mesh_sequence_cache_modifier(obj, alembic_data):
    bpy.ops.object.modifier_add(type='MESH_SEQUENCE_CACHE')
    obj.modifiers["MeshSequenceCache"].cache_file = alembic_data
    obj.modifiers["MeshSequenceCache"].read_data = {'VERT'}

# Itérer à travers tous les objets de la couche de vue pour rechercher les destinataires des fichiers Abc
for obj in view_layer.objects:
    if obj.type == 'MESH':
        if any(mot.lower() in obj.name.lower() for mot in wanted_chars_list):  # Recherche des noms dans wanted_chars_list
            # Vérifier si l'objet a déjà un modificateur Mesh Sequence Cache avec un fichier de cache assigné
            has_mesh_sequence_cache_modifier = any(modifier.type == 'MESH_SEQUENCE_CACHE' for modifier in obj.modifiers)

            # Si aucun modificateur Mesh Sequence Cache avec des données n'est trouvé, en ajouter un
            if not has_mesh_sequence_cache_modifier:
                # Définir l'objet courant comme objet actif
                bpy.context.view_layer.objects.active = obj
                bpy.context.view_layer.update()
                # Construire le nom de fichier Alembic attendu en fonction du nom de l'objet
                alembic_file_name = f"{obj.name}.abc"
                alembic_file_path = os.path.join(export_abc_path, alembic_file_name)
                alembic_file_path = alembic_file_path.replace('\\', '/')

                # Importer le fichier Alembic
                bpy.ops.cachefile.open(filepath=alembic_file_path)
                cache_file = bpy.data.cache_files.get(alembic_file_name)

                if cache_file:
                    if cache_file.object_paths:
                        bpy.ops.object.select_all(action='DESELECT')
                        obj.select_set(True)
                        bpy.context.view_layer.objects.active = obj
                        add_mesh_sequence_cache_modifier(obj, cache_file)
                        bpy.ops.object.modifier_move_to_index(modifier="MeshSequenceCache", index=0)
                        obj.modifiers["MeshSequenceCache"].object_path = cache_file.object_paths[0].path
                        print(f"Added MeshSequenceCache modifier to {obj.name} using {alembic_file_name}")
                else:
                    print(f"No cache file found for {alembic_file_name}")
