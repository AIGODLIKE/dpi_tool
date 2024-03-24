

bl_info = {
    "name" : "DPI_tool",
    "author" : "AIGODLIKE Community:cupcko",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 2),
    "location" : "",
    "warning" : "",
    "doc_url": "",
    "tracker_url": "",
    "category" : "render"
}
import bpy

def render_complete(scene):
    ps = bpy.context.scene.my_custom_properties
    if ps.switch:
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

class TranslationHelper():
    def __init__(self, name: str, data: dict, lang='zh_CN'):
        self.name = name
        self.translations_dict = dict()

        for src, src_trans in data.items():
            key = ("Operator", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans
            key = ("*", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans

    def register(self):
        try:
            bpy.app.translations.register(self.name, self.translations_dict)
        except(ValueError):
            pass

    def unregister(self):
        bpy.app.translations.unregister(self.name)


from . import zh_CN

Dpi_toolzh_CN = TranslationHelper('Dpi_toolzh_CN', zh_CN.data)
Dpi_toolzh_HANS = TranslationHelper('Dpi_toolzh_HANS', zh_CN.data, lang='zh_HANS')

from . import prop,ops,ui
def register():
    if bpy.app.version < (4, 0, 0):
        Dpi_toolzh_CN.register()
    else:
        Dpi_toolzh_CN.register()
        Dpi_toolzh_HANS.register()
    bpy.app.handlers.load_pre.append(pre_load_handler)
    bpy.app.handlers.load_post.append(post_load_handler)
    ui.register()
    prop.register()
    ops.register()



def unregister():
    if bpy.app.version < (4, 0, 0):
        Dpi_toolzh_CN.unregister()
    else:
        Dpi_toolzh_CN.unregister()
        Dpi_toolzh_HANS.unregister()
    ui.unregister()
    prop.unregister()
    ops.unregister()


    bpy.app.handlers.load_pre.remove(pre_load_handler)
    bpy.app.handlers.load_post.remove(post_load_handler)
if __name__ == "__main__":
    register()




