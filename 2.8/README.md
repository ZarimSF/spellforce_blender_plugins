# spellforce_blender_plugins
All blender plugins I came up with regarding import/export of 3D stuff from SpellForce 1

All of those should work from blender 2.8 onwards

# How to install plugins
Open blender -> Edit -> User Preferences... -> Add-ons -> Install... -> Choose plugin file (.py extension) -> Enable plugin by checking the checkbox

Read further for specific usage of each plugin

# import_static_msb.py
You can choose any .msb file to import (and edit) in blender

#### Requirements:
- Textures have to be in the same directory as the .msb file (pulling them from SpellForce data is enough, look for texture names that are suspiciously similar to the .msb file name)

#### Usage:
File -> Import...

# export_static_msb.py
Any edited model can be exported to .msb file

#### Requirements:
- All faces must be triangles
- All materials in a mesh must have an exact node layout (import_static/skinned_msb.py takes care of that, you can look up models loaded through that plugin to see how it looks like)
	- Update: You can now omit the 'Diffuse Color' and 'Specular Color' nodes, they will automatically be added with default values

#### Usage:
File -> Export...

# import_skinned_msb.py
If you have a .bor file to associate with the .msb mesh file, you can import both as a mesh and skeleton

#### Requirements:
- Skeleton file (.bor) is in the same folder as mesh file (.msb)
- Both files have the same name (except file format)
- Both .msb and .bor file must be either original ones, or ones generated with export_skinned_msb.py plugin
- Same requirements as with base mesh import plugin

#### Usage:
File -> Import... (only select .msb file)

#### Note:
Bone orientations do not look right in blender for now, but the model and skeleton receive transformations properly

# export_skinned_msb.py
After editing models/skeletons loaded in through import_skinned_msb.py, you can save the changes using this plugin

#### Requirements:
- Selected object in blender is mesh object, and it has a parent, which is the skeleton
- Mesh vertex groups and skeleton bones are in a 1:1 relation (one vertex group per bone, both have the same name) (files loaded via import_skinned_msb.py are already set up for that)
- All vertices are assigned to at least one vertex group
- All requirements for exporting static models also apply here

#### Usage:
File -> Export... (only specify .msb file)

#### Note:
4 files will be generated upon using this plugin: name.msb, name.bor, name.bsi and name_SKIN.msb
- name.msb goes to mesh folder
- name.bor goes to animation folder
- name.bsi goes to skinning/b20 folder
- name_SKIN.msb goes to skinning/b20 folder, and you must REMOVE the _SKIN part of the filename

# import_animation_bob.py
Selecting a skeleton in 3D view allows you to open animation file that matches the skeleton

#### Requirements:
- Selected skeleton has the same number of bones as the chosen animation file

#### Usage:
File -> Import...

# export_animation_bob.py
If your skeleton has any animation data (position/rotation keyframes), you should be able to export that data as a SpellForce-compatible .bob animation file

#### Requirements:
- Selected object is a skeleton and it has animation keyframes

#### Usage:
File -> Export...

#### Note:
.bob animation files go to animation folder in SpellForce directory

# import_static_skin_msb.py
This is something you can use on original SKIN .msb files, to see how they look like (specifically normals, since they differ from the STATIC .msb file normals, sometimes significantly)

Files imported with this plugin are not very good for anything else, so don't get any ideas :^)

#### Usage:
File -> Import...

# setup_msb_materials.py
Use this to make a custom mesh (e.g. exported from SF2) exportable as .msb and thus compatible with SpellForce.
Select the mesh before applying (and not the skeleton)

#### Usage:
Object -> Set up SpellForce materials
