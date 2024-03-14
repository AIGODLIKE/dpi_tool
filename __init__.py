from bpy.types import Panel,Operator
from .ops import SetRenderBox
bl_info = {
    "name": "Install Pillow Library",
    "blender": (2, 80, 0),
    "category": "Object",
}
# bl_info = {
#     "name" : "My Addon",
#     "author" : "Your Name",
#     "description" : "",
#     "blender" : (3, 0, 0),
#     "version" : (1, 0, 0),
#     "location" : "",
#     "warning" : "",
#     "doc_url": "",
#     "tracker_url": "",
#     "category" : "3D View"
# }
import bpy
import subprocess
import sys
def sna_add_to_render_pt_format_E810E(self, context):
    if not (False):
        ps = bpy.context.scene.my_custom_properties
        layout = self.layout.box()
        root = layout.column(heading='', align=False)
        root.alert = False
        root.enabled = True
        root.active = True
        root.use_property_split = False
        root.use_property_decorate = False
        root.scale_x = 1.0
        root.scale_y = 1.0
        root.alignment = 'Expand'.upper()
        if not True: root.operator_context = "EXEC_DEFAULT"
        pre = root.row(heading='', align=True)
        pre.alert = False
        pre.enabled = True
        pre.active = True
        pre.use_property_split = False
        pre.use_property_decorate = False
        pre.scale_x = 1.0
        pre.scale_y = 1.0
        pre.alignment = 'Expand'.upper()
        if not True: pre.operator_context = "EXEC_DEFAULT"
        pre.prop(ps, 'unit_from', text='')
        # button=pre.row()
        # button.enabled = ps.method=='Accurate'
        # button.active = ps.method=='Accurate'
        pre.operator(SetRenderBox.bl_idname,  text='同步', icon_value=692, emboss=True,)
        ad=pre.row()
        ad.enabled = not ps.preset=='custom_1_1'
        ad.active = not ps.preset=='custom_1_1'
        ad.prop(ps, 'adaptive_scale', text='', icon_value=408, emboss=True, toggle=ps.adaptive_scale)
        pre.prop(ps, 'preset', text='')
        cm = root.row(heading='', align=False)
        cm.alert = False
        cm.enabled = True
        cm.active = True
        cm.use_property_split = False
        cm.use_property_decorate = False
        cm.scale_x = 1.0
        cm.scale_y = 1.0
        cm.alignment = 'Expand'.upper()
        if not True: cm.operator_context = "EXEC_DEFAULT"
        cm.prop(ps, 'orientation',text='')
        wh = cm.row(heading='', align=True)
        wh.alert = False
        wh.enabled = (ps.unit_from=='CM_TO_PIXELS') and ps.preset=='custom_1_1'
        wh.active = (ps.unit_from=='CM_TO_PIXELS') and ps.preset=='custom_1_1'
        wh.use_property_split = False
        wh.use_property_decorate = False
        wh.scale_x = 100.0
        wh.scale_y = 1.0
        wh.alignment = 'Expand'.upper()
        if not True: wh.operator_context = "EXEC_DEFAULT"
        wh.prop(ps, 'width', text='width:', icon_value=408, emboss=True,)
        wh.prop(ps, 'height', text='height:', icon_value=408, emboss=True,)
        dpi = root.row(heading='', align=False)
        dpi.alert = False
        dpi.enabled = True
        dpi.active = True
        dpi.use_property_split = False
        dpi.use_property_decorate = False
        dpi.scale_x = 1.0
        dpi.scale_y = 1.0
        dpi.alignment = 'Expand'.upper()
        if not True: dpi.operator_context = "EXEC_DEFAULT"
        dpi.label(text='分辨率:', icon_value=0)
        dpi_p = dpi.row(heading='', align=False)
        dpi_p.alert = False
        dpi_p.enabled = True
        dpi_p.active = True
        dpi_p.use_property_split = False
        dpi_p.use_property_decorate = False
        dpi_p.scale_x = 100.0
        dpi_p.scale_y = 1.0
        dpi_p.alignment = 'Expand'.upper()
        if not True: dpi_p.operator_context = "EXEC_DEFAULT"
        dpi_p.prop(ps,'dpi', text='', icon_value=0, emboss=True)

        output = root.row(heading='', align=False)
        output.alert = False
        output.enabled = True
        output.active = True
        output.use_property_split = False
        output.use_property_decorate = False
        output.scale_x = 1.0
        output.scale_y = 1.0
        output.alignment = 'Expand'.upper()
        if not True: output.operator_context = "EXEC_DEFAULT"
        output.label(text='像素:', icon_value=0)
        output_p = output.row(heading='', align=True)
        output_p.alert = False
        output_p.enabled = (ps.unit_from=='PIXELS_TO_CM') and ps.preset=='custom_1_1'
        output_p.active = (ps.unit_from=='PIXELS_TO_CM') and ps.preset=='custom_1_1'
        output_p.use_property_split = False
        output_p.use_property_decorate = False
        output_p.scale_x = 100.0
        output_p.scale_y = 1.0
        output_p.alignment = 'Expand'.upper()
        if not True: output_p.operator_context = "EXEC_DEFAULT"
        output_p.prop(ps,'px_x',text='width:', icon_value=0)
        output_p.prop(ps,'px_y',text='height:', icon_value=0)
        method = root.row(heading='', align=False)
        method.alert = False
        method.enabled = True
        method.active = True
        method.use_property_split = False
        method.use_property_decorate = False
        method.scale_x = 1.0
        method.scale_y = 1.0
        method.alignment = 'Expand'.upper()
        if not True: method.operator_context = "EXEC_DEFAULT"
        method.label(text='方法:', icon_value=0)
        method_p = method.row(heading='', align=True)
        method_p.alert = False
        method_p.enabled = True
        method_p.active = True
        method_p.use_property_split = False
        method_p.use_property_decorate = False
        method_p.scale_x = 100.0
        method_p.scale_y = 1.0
        method_p.alignment = 'Expand'.upper()
        if not True: method_p.operator_context = "EXEC_DEFAULT"
        method_p.prop(ps, 'method',  expand=True,)

class InstallPillowOperator(Operator):
    """Install Pillow Library"""
    bl_idname = "object.install_pillow"
    bl_label = "Install Pillow"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            import pip
            # 安装Pillow库
            subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
            self.report({'INFO'}, "Pillow installed successfully.")
        except Exception as e:
            self.report({'ERROR'}, str(e))
        return {'FINISHED'}

def add_object_button(self, context):
    self.layout.operator(
        InstallPillowOperator.bl_idname,
        text=InstallPillowOperator.bl_label,
        icon='PLUGIN')
class SET_DPI_PT_ui(Panel):
    bl_label = "set dpi"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    def draw(self,context):
        ps=bpy.context.scene.my_custom_properties
        layout = self.layout
        box = layout.box()

        row = box.row(heading='')
        row.alignment = 'LEFT'
        row.prop(ps,'adaptive_scale')
        row_prop=row.prop(ps,'preset')
        # row_prop.expand(True)
        row2=box.row()
        row2.prop(ps,'dpi')
        # row2.prop(ps,'dpi_scale')
from . import prop,ops
def register():
    prop.register()
    ops.register()
    bpy.types.RENDER_PT_format.append(sna_add_to_render_pt_format_E810E)
    bpy.utils.register_class(InstallPillowOperator)
    bpy.utils.register_class(SET_DPI_PT_ui)
    bpy.types.VIEW3D_MT_object.append(add_object_button)

def unregister():
    prop.unregister()
    ops.unregister()
    bpy.utils.unregister_class(InstallPillowOperator)
    bpy.utils.unregister_class(SET_DPI_PT_ui)
    bpy.types.VIEW3D_MT_object.remove(add_object_button)
    bpy.types.RENDER_PT_format.remove(sna_add_to_render_pt_format_E810E)
if __name__ == "__main__":
    register()

# from PIL import Image
#
# def change_image_dpi(image_path, output_path, new_dpi=(300, 300)):
#     # 打开图像
#     with Image.open(image_path) as img:
#         # 更改图像的DPI
#         img.save(output_path, dpi=new_dpi)
#
# # 使用函数更改图像的DPI
# image_path = "C:\\Users\\Administrator\\Desktop\\a65682f7646304718857857981fe203e.jpg"
# output_path = "C:\\Users\\Administrator\\Desktop\\output_image.jpg"
#
# change_image_dpi(image_path, output_path)
#


