
import bpy
from .ops import Install_pillow_ops,SetRenderBox,Switch_w_h

# 定义插件的首选项类
class Install_pillow_ui(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        try:
            from PIL import Image
            layout.label(text="The required dependencies have been installed, please restart Blender")
        except:
            layout.label(text="Please install the dependencies required by the plugin first, restart Blender after installation is complete")
            layout.operator(Install_pillow_ops.bl_idname, text="Install the Pillow library")
def sna_add_to_render_pt_format_E810E(self, context):
    if not (False):
        ps = bpy.context.scene.my_custom_properties
        layout = self.layout.box()
        on = layout.column().row(heading='', align=False)
        on.use_property_split = False
        on.use_property_decorate = False
        on.scale_x = 1.0
        on.scale_y = 1.0
        on.alignment = 'Expand'.upper()
        on.prop(ps, 'switch', text="Enable standard DPI output",emboss=True, toggle=True)
        root = layout.column(heading='', align=False)
        root.alert = False
        root.enabled = ps.switch
        root.active = ps.switch
        root.use_property_split = False
        root.use_property_decorate = False
        root.scale_x = 1.0
        root.scale_y = 1.0
        root.alignment = 'Expand'.upper()

        input=root.row(heading='', align=False)
        input.alignment = 'Expand'.upper()
        input.label(text='Input:')
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
        pre.label(text='Preset:')
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

        cm = root.row(heading='', align=False)
        cm.alert = False
        cm.enabled = True
        cm.active = True
        cm.use_property_split = False
        cm.use_property_decorate = False
        cm.scale_x = 1.0
        cm.scale_y = 1.0
        cm.alignment = 'Expand'.upper()
        cm.operator(Switch_w_h.bl_idname,text='Switch',emboss=True,)
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
        wh.prop(ps, 'width', text='Width:', icon_value=408, emboss=True,)
        wh.prop(ps, 'height', text='Height:', icon_value=408, emboss=True,)
        dpi = root.row(heading='', align=False)
        dpi.alert = False
        dpi.enabled = True
        dpi.active = True
        dpi.use_property_split = False
        dpi.use_property_decorate = False
        dpi.scale_x = 1.0
        dpi.scale_y = 1.0
        dpi.alignment = 'Expand'.upper()
        dpi.label(text='DPI:', icon_value=0)
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
        output.label(text='Pixels:', icon_value=0)
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
        method.label(text='Scale:', icon_value=0)
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
        output = root.row()
        output.label(text='Output:', icon_value=0)
        output_p=output.row(align=True)
        output_p.scale_x = 100.0
        output_p.scale_y = 1.0
        output_p_a=output_p.row(align=True)
        output_p_a.enabled = not ps.preset=='custom_1_1'
        output_p_a.active = not ps.preset=='custom_1_1'
        output_p_a.prop(ps, 'adaptive_scale', text="Proportional scaling", icon_value=408, emboss=True, toggle=True)

        output_p_o=output_p.row(align=True)
        output_p_o.operator(SetRenderBox.bl_idname,  text="Force synchronization", icon_value=692, emboss=True,)
        note = root.row()
        filepath = bpy.context.scene.render.filepath
        if not bpy.data.is_saved :
            note.label(text='Please save the file first and set the output path')
        elif bpy.context.scene.use_nodes:
            from .ops import check_cp_output_path
            if check_cp_output_path():
                node,path=check_cp_output_path()
                if node.base_path == '/tmp\\':
                    note.label(text='The output path is in c:/tmp/')
                elif node.base_path == '//':
                    note.label(text='The output path is in the current file directory')
            else:
                note.label(text='Please add an output node and set the output path')

        elif filepath=='/tmp\\':
            note.label(text='The output path is in c:/tmp/')
        elif filepath=='':
            note.label(text='Please set the output path')

# 注册和注销函数
def register():
    bpy.types.RENDER_PT_format.append(sna_add_to_render_pt_format_E810E)
    bpy.utils.register_class(Install_pillow_ui)

def unregister():
    bpy.types.RENDER_PT_format.remove(sna_add_to_render_pt_format_E810E)
    bpy.utils.unregister_class(Install_pillow_ui)
