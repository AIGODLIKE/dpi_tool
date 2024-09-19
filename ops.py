import bpy,subprocess,sys,os
import numpy as np
from bpy.types import Operator
from .extern.PIL import Image
# 更改DPI的函数
def change_image_dpi(image_path, new_dpi=(300, 300)):
    with Image.open(image_path) as img:
        img.save(image_path, dpi=new_dpi)
def change_image_size(image_path,size):
    with Image.open(image_path) as img:
        img=img.resize(size, Image.LANCZOS)
        img.save(image_path)
def check_cp_output_path():
    # print('check_cp_output_path')
    '''返回nodes{'节点名':路径},如果没有输出节点返回False'''
    if bpy.context.scene.use_nodes and len(bpy.context.scene.node_tree.nodes):
        nodes = {}
        for i in bpy.context.scene.node_tree.nodes:
            if i.type == 'OUTPUT_FILE' and i.inputs['Image'].is_linked:
                if  i.base_path=='/tmp\\':
                    nodes[i.name]=Path(Path.home().anchor)/i.base_path
                elif i.base_path=='':
                    nodes[i.name]=Path(Path.home().anchor)
                else:

                    if Path(i.base_path).is_dir():
                        #如果是路径，判断是否是c盘下的文件夹
                        if Path.home().anchor in i.base_path:
                            nodes[i.name] = Path(i.base_path)
                        else:
                            filepath = Path(Path.home().anchor) / i.base_path
                            filepath.mkdir(exist_ok=True)
                            nodes[i.name] = filepath
                        continue
                    Path(i.base_path).mkdir(exist_ok=True)

                    nodes[i.name]=Path(i.base_path)
        if len(nodes):
            return nodes
        else:
            return False
    else:
        return False
from pathlib import Path

def check_pn_output_path():
    '''没有时返回False'''
    filepath=bpy.context.scene.render.filepath
    if filepath[:5] == '/tmp\\':
        root_path = Path(Path.home().anchor)/filepath[:5]
        root_path.mkdir(exist_ok=True)
        return str(root_path)

    elif Path(filepath).is_dir():
        return filepath
    else:
        Path(filepath).mkdir(exist_ok=True)
        if Path(filepath).is_dir():
            return str(filepath)
        return False
def get_file_extension():
    '''获取输出节点的文件格式字符串.xxx else None 返回ext{'节点名':后缀名}'''
    temp=bpy.context.scene.render.image_settings.file_format
    res=check_cp_output_path()
    if res:
        extension= {}
        for i in res:
            # res[i]
            # bpy.context.scene.render.image_settings.file_format=res[0].format.file_format
            bpy.context.scene.render.image_settings.file_format=bpy.context.scene.node_tree.nodes[i].format.file_format
            ex=bpy.context.scene.render.file_extension
            bpy.context.scene.render.image_settings.file_format=temp
            extension[i]=ex
        return extension
    else:
        return False

class Switch_w_h(bpy.types.Operator):
    """长和宽互换"""
    bl_idname = "render.switch_w_h"
    bl_label = "switch_w_h"

    def execute(self, context):
        ps=bpy.context.scene.my_custom_properties
        opposite=None
        if ps.width>=ps.height:
            ps.orientation='Horizontal'
            opposite='Vertical'
        else:
            ps.orientation = 'Vertical'
            opposite = 'Horizontal'
        if ps.unit_from=='CM_TO_PIXELS':
            temp=ps.width
            ps.width=ps.height
            ps.height=temp
        else:
            temp=ps.px_x
            ps.px_x=ps.px_y
            ps.px_y=temp
        ps.orientation=opposite
        return {'FINISHED'}
class Process_images(bpy.types.Operator):
    """设置路径,dpi"""
    bl_idname = "file.process_images"
    bl_label = "Process_images"

    def execute(self, context):
        # 获取渲染图片的路径
        image_path = []
        num = bpy.context.scene.frame_current
        if check_cp_output_path():
            nodes=check_cp_output_path()
            ext = get_file_extension()
            for node in nodes:
                # if not nodes[node]:
                    #切换节点
                    #检测是否路径
                if Path(nodes[node]).is_dir():
                    path = Path(nodes[node])  /('Image' + str(10000 + num)[1:] + ext[node])
                    image_path.append(path)
            if not len(image_path):
                self.report({'WARNING'}, "Set the output node image path first")
                return {'CANCELLED'}
        elif check_pn_output_path():
            base_name, extension = os.path.splitext(check_pn_output_path())
            if os.path.isdir(check_pn_output_path()):
                path = Path(check_pn_output_path()) / ('Image' + str(10000 + num)[
                                                                1:] + bpy.context.scene.render.file_extension)
            elif extension == bpy.context.scene.render.file_extension:
                path = check_pn_output_path()
            try:
                image_path.append(path)
            except:
                self.report({'WARNING'}, "The output path format is unrecognizable, please check the output path")
                return {'CANCELLED'}
        else:
            # print('先设置图片路径')
            self.report({'WARNING'}, "Set the image path first")
            return {'CANCELLED'}
        ps = bpy.context.scene.my_custom_properties
        # 设置想要的DPI值
        new_dpi = (ps.dpi, ps.dpi)
        print('new_dpi',new_dpi)
        for i in image_path:
            print('image_path',i)
            if not check_cp_output_path():
                '''合成节点不需要保存图片'''
                image = bpy.data.images['Render Result']
                print("Render Result")
                try:
                    image.save_render(filepath=i)
                    print("image saved")
                except:
                    print("Failed to save the image")

            # 缩放
            if ps.adaptive_scale or ps.method == 'Simple':
                change_image_size(i, (ps.px_x, ps.px_y))
                print("change_image_size")
            # 更改图片DPI
            change_image_dpi(i, new_dpi)
            print(f'Rendered image DPI changed to {ps.dpi}')



        return {'FINISHED'}



class SetRenderBox(bpy.types.Operator):
    """无视当前比例直接设置渲染框大小为目标大小(可能会改变比例)"""
    bl_idname = "view3d.set_render_box"
    bl_label = "Set Render box"

    @classmethod
    def poll(cls, context):
        ps = bpy.context.scene.my_custom_properties
        return ps.method=='Accurate' or ps.preset=='custom_1_1' or (ps.method=='Simple' and not ps.adaptive_scale)

    def execute(self, context):
        ps = bpy.context.scene.my_custom_properties
        px=bpy.context.scene.render
        if px.resolution_percentage !=100:
            px.resolution_x =round(np.multiply(ps.px_x,100)/px.resolution_percentage)
            px.resolution_y =round(np.multiply(ps.px_y,100)/px.resolution_percentage)
            # px.resolution_y=ps.px_y
        else:
            px.resolution_x = ps.px_x
            px.resolution_y = ps.px_y
        self.report({'INFO'}, "已同步")
        return {'FINISHED'}
def register():
    bpy.utils.register_class(Switch_w_h)
    bpy.utils.register_class(Process_images)
    bpy.utils.register_class(SetRenderBox)

def unregister():
    bpy.utils.unregister_class(Switch_w_h)
    bpy.utils.unregister_class(Process_images)
    bpy.utils.unregister_class(SetRenderBox)
