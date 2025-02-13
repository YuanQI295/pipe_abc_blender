import bpy
import os

# Iterate through all objects in the view layer
for obj in bpy.context.view_layer.objects:
    # Check if the object is a mesh
    if obj.type == 'MESH':
        # Get the list of modifiers to avoid modifying the list during iteration
        modifiers_to_remove = [mod for mods in obj.modifiers if mod.type == 'MESH_SEQUENCE_CACHE']
        
        # Remove each MeshSequenceCache modifier
        for mod in modifiers_to_remove:
            obj.modifiers.remove(mod)
            print(f"Removed MeshSequenceCache modifier from {obj.name}")
