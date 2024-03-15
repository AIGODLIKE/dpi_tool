import os

from bpy.types import Panel,Operator
from .ops import SetRenderBox

bl_info = {
    "name" : "dpi_tool",
    "author" : "AIGODLIKE Community:cupcko",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "",
    "tracker_url": "",
    "category" : "render"
}
import bpy
import subprocess
import sys


def render_complete(scene):
    bpy.ops.file.process_images()

from bpy.app.handlers import persistent
@persistent
def pre_load_handler(dummy):
    #
    print('---------------------------------')
    try:
        bpy.app.handlers.render_complete.remove(render_complete)
    except:
        pass


@persistent
def post_load_handler(dummy):
    try:
        bpy.app.handlers.render_complete.remove(render_complete)
    except:
        pass
    bpy.app.handlers.render_complete.append(render_complete)



from . import prop,ops,ui
def register():

    bpy.app.handlers.load_pre.append(pre_load_handler)
    bpy.app.handlers.load_post.append(post_load_handler)
    ui.register()
    prop.register()
    ops.register()



def unregister():
    ui.unregister()
    prop.unregister()
    ops.unregister()


    bpy.app.handlers.load_pre.remove(pre_load_handler)
    bpy.app.handlers.load_post.remove(post_load_handler)
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


