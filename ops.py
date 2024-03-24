import bpy,subprocess,sys,os
import numpy as np
from bpy.types import Operator
import importlib.util

def check_pillow_installed():
    pillow_spec = importlib.util.find_spec("PIL")
    if pillow_spec is not None:
        print("Pillow is installed.")
        return True
    else:
        print("Pillow is not installed.")
        return False

# 调用函数检查Pillow是否安装
if check_pillow_installed():
    from PIL import Image
# 更改DPI的函数
def change_image_dpi(image_path, new_dpi=(300, 300)):
    with Image.open(image_path) as img:
        img.save(image_path, dpi=new_dpi)
def change_image_size(image_path,size):
    with Image.open(image_path) as img:
        img=img.resize(size, Image.LANCZOS)
        img.save(image_path)
def check_cp_output_path():
    '''返回nodes{'节点名':路径},如果没有输出节点返回False'''
    if bpy.context.scene.use_nodes and len(bpy.context.scene.node_tree.nodes):
        nodes = {}
        for i in bpy.context.scene.node_tree.nodes:

            if i.type == 'OUTPUT_FILE':
                if  i.base_path=='/tmp\\':
                    nodes[i.name]='C:'+i.base_path
                    # return [i,'C://'+i.base_path]
                elif i.base_path=='':
                    nodes[i.name]='C:\\'
                    # return False
                else:
                    nodes[i.name]=i.base_path
                    # return [i,i.base_path]
                # print(i.base_path)
                # print(i.name)
        return nodes
    else:
        return False
def check_pn_output_path():
    '''没有时返回False'''
    filepath=bpy.context.scene.render.filepath
    if filepath == '/tmp\\':
        return 'C://' + filepath
    elif filepath == '':
        return False
    else:
        return filepath
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
                if os.path.isdir(nodes[node]):

                    path = nodes[node] + 'Image' + str(10000 + num)[1:] + ext[node]
                    image_path.append(path)
            # base_name, extension = os.path.splitext(check_cp_output_path()[1])
            # if os.path.isdir(check_cp_output_path()[1]):
            #     image_path = check_cp_output_path()[1] + 'Image' + str(10000 + num)[1:] + get_file_extension()
            # elif extension == get_file_extension():
            #     image_path = check_cp_output_path()[1]
        elif check_pn_output_path():
            base_name, extension = os.path.splitext(check_pn_output_path())
            if os.path.isdir(check_pn_output_path()):
                path = check_pn_output_path() + 'Image' + str(10000 + num)[
                                                                1:] + bpy.context.scene.render.file_extension
            elif extension == bpy.context.scene.render.file_extension:
                path = check_pn_output_path()
            image_path.append(path)
        else:
            # print('先设置图片路径')
            self.report({'WARNING'}, "先设置图片路径")
            return {'CANCELLED'}
        ps = bpy.context.scene.my_custom_properties
        # 设置想要的DPI值
        new_dpi = (ps.dpi, ps.dpi)
        for i in image_path:
            if not check_cp_output_path():
                image = bpy.data.images['Render Result']
                try:
                    image.save_render(filepath=i)
                except:
                    print('图片保存失败')

            # 缩放
            if ps.adaptive_scale or ps.method == 'Simple':
                change_image_size(i, (ps.px_x, ps.px_y))
            # 更改图片DPI
            change_image_dpi(i, new_dpi)
            print(f'Rendered image DPI changed to {ps.dpi}')



        return {'FINISHED'}


class Install_pillow_ops(Operator):
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
    bpy.utils.register_class(Install_pillow_ops)
def unregister():
    bpy.utils.unregister_class(Switch_w_h)
    bpy.utils.unregister_class(Process_images)
    bpy.utils.unregister_class(SetRenderBox)
    bpy.utils.unregister_class(Install_pillow_ops)