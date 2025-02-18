# pipe_abc_blender

This repository contains a quick and simple solution for exporting and importing Alembic animation data, I worked on this project during my internship at Shards Animation. We needed to 'bake' the animations to ABC files for our pipeline.

It was for a trailer of a serie made in blender.

````
export_abc.py
````
exporting Alembics from the animated scenes

````
mesh_graber.py
````
finding the non animated meshes of characters

````
import_abc.py
````
importing the Abcs into meshes's mesh sequencer
