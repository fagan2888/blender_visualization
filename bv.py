import bpy
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.world.horizon_color = (1, 1, 1)
bpy.ops.object.delete(use_global=False)
bpy.ops.mesh.primitive_uv_sphere_add(size=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.ops.transform.resize(value=(0.306602, 0.306602, 0.306602), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

