
import bpy
from .ops import Install_pillow_ops,SetRenderBox

# 定义插件的首选项类
class Install_pillow_ui(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        try:
            from PIL import Image
            layout.label(text="所需依赖已安装,请重启blender")
        except:
            layout.label(text="请先安装插件所需依赖,安装完成后重启blender")
            layout.operator(Install_pillow_ops.bl_idname, text="安装pillow库")
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
        input=root.row(heading='', align=False)
        input.alignment = 'Expand'.upper()
        input.label(text='输入:')
        input_p = input.row(heading='', align=False)
        input_p.alert = False
        input_p.enabled = True
        input_p.active = True
        input_p.use_property_split = False
        input_p.use_property_decorate = False
        input_p.scale_x = 100.0
        input_p.scale_y = 1.0
        input_p.alignment = 'Expand'.upper()
        # input_p.prop(ps, 'dpi', text='', icon_value=0, emboss=True)
        input_p.prop(ps, 'unit_from', text='')
        pre = root.row(heading='', align=False)
        pre.label(text='预设:')
        pre_p = pre.row(heading='', align=False)
        pre_p.alert = False
        pre_p.enabled = True
        pre_p.active = True
        pre_p.use_property_split = False
        pre_p.use_property_decorate = False
        pre_p.scale_x = 100.0
        pre_p.scale_y = 1.0
        pre_p.alignment = 'Expand'.upper()
        pre_p.prop(ps, 'preset', text='')
        # pre.alert = False
        # pre.enabled = True
        # pre.active = True
        # pre.use_property_split = False
        # pre.use_property_decorate = False
        # pre.scale_x = 1.0
        # pre.scale_y = 1.0
        # pre.alignment = 'Expand'.upper()
        # if not True: pre.operator_context = "EXEC_DEFAULT"
        # pre.prop(ps, 'unit_from', text='')
        # # button=pre.row()
        # # button.enabled = ps.method=='Accurate'
        # # button.active = ps.method=='Accurate'
        # pre.operator(SetRenderBox.bl_idname,  text='同步', icon_value=692, emboss=True,)
        # ad=pre.row()
        # ad.enabled = not ps.preset=='custom_1_1'
        # ad.active = not ps.preset=='custom_1_1'
        # ad.prop(ps, 'adaptive_scale', text='', icon_value=408, emboss=True, toggle=ps.adaptive_scale)
        # pre.prop(ps, 'preset', text='')
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
        wh.prop(ps, 'width', text='横宽:', icon_value=408, emboss=True,)
        wh.prop(ps, 'height', text='竖长:', icon_value=408, emboss=True,)
        dpi = root.row(heading='', align=False)
        dpi.alert = False
        dpi.enabled = True
        dpi.active = True
        dpi.use_property_split = False
        dpi.use_property_decorate = False
        dpi.scale_x = 1.0
        dpi.scale_y = 1.0
        dpi.alignment = 'Expand'.upper()
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
        output_p.prop(ps,'px_x',text='x:', icon_value=0)
        output_p.prop(ps,'px_y',text='y:', icon_value=0)
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
        method.label(text='缩放:', icon_value=0)
        method_p = method.row(heading='', align=True)
        method_p.alert = False
        method_p.enabled = not ps.preset=='custom_1_1'
        method_p.active = not ps.preset=='custom_1_1'
        method_p.use_property_split = False
        method_p.use_property_decorate = False
        method_p.scale_x = 100.0
        method_p.scale_y = 1.0
        method_p.alignment = 'Expand'.upper()
        if not True: method_p.operator_context = "EXEC_DEFAULT"
        method_p.prop(ps, 'method',  expand=True,)
        note = root.row()
        filepath = bpy.context.scene.render.filepath
        if not bpy.data.is_saved :
            note.label(text='请先保存文件,并设置输出路径')
        elif filepath=='/tmp\\':
            note.label(text='初始输出路径在c:/tmp/')
        elif filepath=='':
            note.label(text='请设置输出路径')

# 注册和注销函数
def register():
    bpy.types.RENDER_PT_format.append(sna_add_to_render_pt_format_E810E)
    bpy.utils.register_class(Install_pillow_ui)

def unregister():
    bpy.types.RENDER_PT_format.remove(sna_add_to_render_pt_format_E810E)
    bpy.utils.unregister_class(Install_pillow_ui)
