bl_info = {
	"name": "Setup materials for SpellForce skin mesh (.msb)",
	"description": "Set up nodes for msb materials",
	"author": "ZarimSF",
	"blender": (2, 80, 0),
	"location": "Material",
	"warning": "totally untested...", # used for warning icon and text in addons panel
	"category": "Material",
}

import bpy
from bpy.props import (
	StringProperty,
	FloatProperty,
	IntProperty,
	BoolProperty,
	EnumProperty,
)
from bpy_extras.io_utils import (
	orientation_helper,
	axis_conversion,
)
from mathutils import *
from struct import unpack

def main(context):
	object = context.object
	mesh = object.data
	
	mesh.use_auto_smooth = True
	objName = object.name
	
	# rename UVMaps
	for uvmap in mesh.uv_layers:
		uvmap.name = objName

	# set up materials
	for m in mesh.materials:
		m.use_nodes = True
		# reset tree
		nodes = m.node_tree.nodes
		links = m.node_tree.links
		for node in nodes:
			if node.name != 'Image Texture':
				nodes.remove(node)
			else:
				# needed because otherwise blender might look for '.dds.dds' files
				node.image.name = node.image.name.split('.dds')[0]
		for link in links:
			links.remove(link)
		
		# create nodes
		uvmap_node = nodes.new(type = 'ShaderNodeUVMap')
		uvmap_node.location = (-300, 100)
		imtex_node = nodes.get('Image Texture') or nodes.new(type = 'ShaderNodeTexImage')
		imtex_node.name = 'Image Texture'
		imtex_node.location = (-100, 200)
		tbsdf_node = nodes.new(type = 'ShaderNodeBsdfTransparent')
		tbsdf_node.location = (200, 100)
		dbsdf_node = nodes.new(type = 'ShaderNodeBsdfDiffuse')
		dbsdf_node.location = (200, 0)
		mixsh_node = nodes.new(type = 'ShaderNodeMixShader')
		mixsh_node.location = (400, 100)
		output_node = nodes.new(type = 'ShaderNodeOutputMaterial')
		output_node.location = (600, 100)
		diffuse_node = nodes.new(type = 'ShaderNodeRGB')
		diffuse_node.name = 'Diffuse Color'
		diffuse_node.location = (-500, 300)
		specular_node = nodes.new(type = 'ShaderNodeRGB')
		specular_node.name = 'Specular Color'
		specular_node.location = (-500, 100)
		# set node parameters
		uvmap_node.uv_map = objName
		#imtex_node.image = img_per_material[i]
		diffuse_color = [0.5, 0.5, 0.5, 1]
		diffuse_node.outputs[0].default_value = diffuse_color
		specular_color = [0, 0, 0, 1]
		specular_node.outputs[0].default_value = specular_color
		# connect nodes
		links.new(uvmap_node.outputs['UV'], imtex_node.inputs['Vector'])
		links.new(imtex_node.outputs['Color'], dbsdf_node.inputs['Color'])
		links.new(imtex_node.outputs['Alpha'], mixsh_node.inputs['Fac'])
		links.new(tbsdf_node.outputs['BSDF'], mixsh_node.inputs[1])
		links.new(dbsdf_node.outputs['BSDF'], mixsh_node.inputs[2])
		links.new(mixsh_node.outputs['Shader'], output_node.inputs['Surface'])
		
	# final set up, all is ready
	mesh.update()

	return 0


class SetupMSBMaterials(bpy.types.Operator):
	"""Set up nodes for msb materials"""
	bl_idname = "import.msb_static_skin"#"materials.msb_material_setup"
	bl_label = "Set up SpellForce materials"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		if main(context) == 0:
			return {'FINISHED'}
		return {'CANCELLED'}



def menu_func(self, context):
	self.layout.operator(SetupMSBMaterials.bl_idname)


def register():
	bpy.utils.register_class(SetupMSBMaterials)
	bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
	bpy.utils.unregister_class(SetupMSBMaterials)
	bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
	register()
