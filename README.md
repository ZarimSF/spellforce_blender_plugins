# spellforce_blender_plugins
All blender plugins I came up with regarding import/export of 3D stuff from SpellForce 1

All of those should work with blender 2.78, probably some earlier versions too

#### New:
There's also a set of plugins for 2.8, they are much better than the plugins below, so I recommend using those; read the readme file in the 2.8 directory above

**Everything below only applies to plugins in this directory, not to the 2.8 plugins**

# How to install plugins
Open blender -> User Preferences... -> Add-ons -> Install add-on from file... -> Choose plugin file (.py extension) -> Enable plugin by checking the checkbox

Read further for specific usage of each plugin

# spellforce_import.py
You can choose any .msb file to import (and edit) in blender

#### Requirements:
- Textures have to be in the same directory as the .msb file (pulling them from SpellForce data is enough, look for texture names that are suspiciously similar to the .msb file name)

#### Usage:
File -> Import...

# spellforce_export.py
Any edited model can be exported to .msb file

#### Requirements:
- All faces must be triangles
- No two points on any single UV map may overlap (edges and faces can intersect alright though)

#### Usage:
File -> Export...

# spellforce_import_with_skeleton
If you have .bor file to associate with the .msb mesh file, you can import both as a mesh and skeleton

#### Requirements:
- Skeleton file (.bor) is in the same folder as mesh file (.msb)
- Both files have the same name (except file extension)
- Mesh is in original, unedited form (as in, exact same mesh as it was bundled with SpellForce)
- Same requirements as with base mesh import plugin

#### Usage:
File -> Import... (only select .msb file)

#### WARNING:
Meshes loaded with skeleton are no longer editable due to mesh transformations required for animations to work (more work on it in the future)

#### Note:
Bone orientations do not look right in blender for now, but the model and skeleton receive transformations properly

# spellforce_import_animation
You can choose any .bob file to open and edit in blender

#### Requirements:
- Selected object in blender is armature (skeleton)
- Number of bones in skeleton and animation must match

For obvious reasons, animations only work with skeleton files imported with the spellforce_import_with_skeleton plugin

#### Usage:
File -> Imoprt...

# spellforce_export_animation
Any edited animation can be exported to .bob animation file

For same reasons, this will work properly only if animation was first imported using the plugin mentioned above

#### Requirements:
- Selected object in blender is armature (skeleton)

#### Usage:
File -> Export...
