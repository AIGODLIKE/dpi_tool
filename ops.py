import bpy


class SetRenderBox(bpy.types.Operator):
    """设置渲染框大小"""
    bl_idname = "view3d.set_render_box"
    bl_label = "Set Render box"

    @classmethod
    def poll(cls, context):
        ps = bpy.context.scene.my_custom_properties
        return ps.method=='Accurate' or ps.preset=='custom_1_1'

    def execute(self, context):
        ps = bpy.context.scene.my_custom_properties
        px=bpy.context.scene.render
        px.resolution_x =ps.px_x
        px.resolution_y=ps.px_y
        self.report({'INFO'}, "已同步")
        return {'FINISHED'}
def register():
    bpy.utils.register_class(SetRenderBox)
def unregister():
    bpy.utils.unregister_class(SetRenderBox)