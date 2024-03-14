import bpy,math
import numpy
import numpy as np
from bpy.props import IntProperty, BoolProperty, EnumProperty, StringProperty,FloatProperty
from bpy.types import PropertyGroup
paper_presets = (
    ("custom_1_1", "custom(cm)", ""),
    ("A0_84.1_118.9", "A0 (84.1x118.9 cm)", ""),
    ("A1_59.4_84.1", "A1 (59.4x84.1 cm)", ""),
    ("A2_42.0_59.4", "A2 (42.0x59.4 cm)", ""),
    ("A3_29.7_42.0", "A3 (29.7 42.0 cm)", ""),
    ("A4_21.0_29.7", "A4 (21.0x29.7 cm)", ""),
    ("A5_14.8_21.0", "A5 (14.8x21.0 cm)", ""),
    ("A6_10.5_14.8", "A6 (10.5x14.8 cm)", ""),
    ("A7_7.4_10.5", "A7 (7.4x10.5 cm)", ""),
    ("A8_5.2_7.4", "A8 (5.2x7.4 cm)", ""),
    ("A9_3.7_5.2", "A9 (3.7x5.2 cm)", ""),
    ("A10_2.6_3.7", "A10 (2.6x3.7 cm)", ""),

    ("B0_100.0_141.4", "B0 (100.0x141.4 cm)", ""),
    ("B1_70.7_100.0", "B1 (70.7x100.0 cm)", ""),
    ("B2_50.0_70.7", "B2 (50.0x70.7 cm)", ""),
    ("B3_35.3_50.0", "B3 (35.3x50.0 cm)", ""),
    ("B4_25.0_35.3", "B4 (25.0x35.3 cm)", ""),
    ("B5_17.6_25.0", "B5 (17.6x25.0 cm)", ""),
    ("B6_12.5_17.6", "B6 (12.5x17.6 cm)", ""),
    ("B7_8.8_12.5", "B7 (8.8x12.5 cm)", ""),
    ("B8_6.2_8.8", "B8 (6.2x8.8 cm)", ""),
    ("B9_4.4_6.2", "B9 (4.4x6.2 cm)", ""),
    ("B10_3.1_4.4", "B10 (3.1x4.4 cm)", ""),

    ("C0_91.7_129.7", "C0 (91.7x129.7 cm)", ""),
    ("C1_64.8_91.7", "C1 (64.8x91.7 cm)", ""),
    ("C2_45.8_64.8", "C2 (45.8x64.8 cm)", ""),
    ("C3_32.4_45.8", "C3 (32.4x45.8 cm)", ""),
    ("C4_22.9_32.4", "C4 (22.9x32.4 cm)", ""),
    ("C5_16.2_22.9", "C5 (16.2x22.9 cm)", ""),
    ("C6_11.4_16.2", "C6 (11.4x16.2 cm)", ""),
    ("C7_8.1_11.4", "C7 (8.1x11.4 cm)", ""),
    ("C8_5.7_8.1", "C8 (5.7x8.1 cm)", ""),
    ("C9_4.0_5.7", "C9 (4.0x5.7 cm)", ""),
    ("C10_2.8_4.0", "C10 (2.8x4.0 cm)", ""),

    ("Letter_21.6_27.9", "Letter (21.6x27.9 cm)", ""),
    ("Legal_21.6_35.6", "Legal (21.6x35.6 cm)", ""),
    ("Legal junior_20.3_12.7", "Legal junior (20.3x12.7 cm)", ""),
    ("Ledger_43.2_27.9", "Ledger (43.2x27.9 cm)", ""),
    ("Tabloid_27.9_43.2", "Tabloid (27.9x43.2 cm)", ""),

    ("ANSI C_43.2_55.9", "ANSI C (43.2x55.9 cm)", ""),
    ("ANSI D_55.9_86.4", "ANSI D (55.9x86.4 cm)", ""),
    ("ANSI E_86.4_111.8", "ANSI E (86.4x111.8 cm)", ""),

    ("Arch A_22.9_30.5", "Arch A (22.9x30.5 cm)", ""),
    ("Arch B_30.5_45.7", "Arch B (30.5x45.7 cm)", ""),
    ("Arch C_45.7_61.0", "Arch C (45.7x61.0 cm)", ""),
    ("Arch D_61.0_91.4", "Arch D (61.0x91.4 cm)", ""),
    ("Arch E_91.4_121.9", "Arch E (91.4x121.9 cm)", ""),
    ("Arch E1_76.2_106.7", "Arch E1 (76.2x106.7 cm)", ""),
    ("Arch E2_66.0_96.5", "Arch E2 (66.0x96.5 cm)", ""),
    ("Arch E3_68.6_99.1", "Arch E3 (68.6x99.1 cm)", ""),
    )


def paper_enum_parse(idname):
    tipo, dim_w, dim_h = idname.split("_")
    return tipo, float(dim_w), float(dim_h)


paper_presets_data = {
    idname: paper_enum_parse(idname)
    for idname, name, descr in paper_presets
    }

def pixels_from_print(ps):
    tipo, dim_w, dim_h = paper_presets_data[ps.preset]
    px=bpy.context.scene.render
    if ps.unit_from == "CM_TO_PIXELS":
        if tipo == "custom":
            dim_w = ps.width
            dim_h = ps.height
            ps.width = dim_w
            ps.height = dim_h

            ps.px_x = math.ceil((ps.width * ps.dpi) / 2.54)
            ps.px_y = math.ceil((ps.height * ps.dpi) / 2.54)
        elif tipo != "custom" and ps.orientation == "Horizontal":#横宽
            if ps.adaptive_scale:
                if px.resolution_y>=px.resolution_x or px.resolution_y/px.resolution_x>=dim_h/dim_w:
                    ps.px_x = round(np.prod(np.array([ps.width ,ps.dpi,px.resolution_x])) / np.multiply(2.54,px.resolution_y))
                    ps.px_y = round(np.multiply(ps.height ,ps.dpi) / numpy.array(2.54)) #先求y
                    ps.width = np.multiply(dim_h, px.resolution_x) / np.array(px.resolution_y)
                    ps.height = dim_h
                elif px.resolution_y/px.resolution_x<dim_h/dim_w:
                    # ps.px_y = round(np.multiply(ps.height , ps.dpi) / np.array(2.54))
                    ps.px_y = round(np.prod(np.array([ps.width , ps.dpi,px.resolution_y])) / np.multiply(2.54 , px.resolution_x))
                    ps.px_x = round(np.multiply(ps.width , ps.dpi) / np.array(2.54))
                    # ps.px_x = round((ps.height * ps.dpi) / 2.54 * px.resolution_x / px.resolution_y)
                    ps.height = dim_h * px.resolution_y / px.resolution_x
                    ps.width = dim_w
            else:
                ps.width = dim_h
                ps.height = dim_w
                ps.px_x = math.ceil((ps.width * ps.dpi) / 2.54)
                ps.px_y = math.ceil((ps.height * ps.dpi) / 2.54)
        elif tipo != "custom" and ps.orientation == "Vertical":#竖
            if ps.adaptive_scale:
                if px.resolution_x>=px.resolution_y or px.resolution_x/px.resolution_y>=dim_w/dim_h:
                    ps.px_x=round(np.multiply(ps.width ,ps.dpi) / numpy.array(2.54))
                    ps.px_y=round(np.prod(np.array([ps.width ,ps.dpi,px.resolution_y])) / np.multiply(2.54,px.resolution_x))
                    ps.width = dim_w
                    ps.height = np.multiply(dim_w,px.resolution_y) / np.array(px.resolution_x)

                elif px.resolution_x/px.resolution_y<dim_w/dim_h:
                    pass
                    ps.px_y=round((ps.height * ps.dpi) / 2.54)
                    ps.px_x=round((ps.height * ps.dpi) / 2.54*px.resolution_x/px.resolution_y)
                    ps.width = dim_h* px.resolution_x / px.resolution_y
                    ps.height = dim_h
            else:
                ps.width = dim_w
                ps.height = dim_h
                ps.px_x = math.ceil((ps.width * ps.dpi) / 2.54)
                ps.px_y = math.ceil((ps.height * ps.dpi) / 2.54)

    else:
        if tipo=='custom':
            ps.width = (ps.px_x / ps.dpi) * 2.54
            ps.height = (ps.px_y / ps.dpi) * 2.54

        if tipo != "custom" and ps.orientation == "Horizontal":#横
            if ps.adaptive_scale:
                if px.resolution_y >= px.resolution_x or px.resolution_y / px.resolution_x >= dim_h / dim_w:
                    ps.px_x = round(
                        np.prod(np.array([ps.width, ps.dpi, px.resolution_x])) / np.multiply(2.54, px.resolution_y))
                    ps.px_y = round(np.multiply(ps.height, ps.dpi) / numpy.array(2.54))  # 先求y
                    ps.width = np.multiply(dim_h, px.resolution_x) / np.array(px.resolution_y)
                    ps.height = dim_h
                elif px.resolution_y / px.resolution_x < dim_h / dim_w:
                    # ps.px_y = round(np.multiply(ps.height , ps.dpi) / np.array(2.54))
                    ps.px_y = round(
                        np.prod(np.array([ps.width, ps.dpi, px.resolution_y])) / np.multiply(2.54, px.resolution_x))
                    ps.px_x = round(np.multiply(ps.width, ps.dpi) / np.array(2.54))
                    # ps.px_x = round((ps.height * ps.dpi) / 2.54 * px.resolution_x / px.resolution_y)
                    ps.height = dim_h * px.resolution_y / px.resolution_x
                    ps.width = dim_w
            else:
                ps.width = dim_h
                ps.height = dim_w
                ps.px_x = math.ceil((ps.width * ps.dpi) / 2.54)
                ps.px_y = math.ceil((ps.height * ps.dpi) / 2.54)
        elif tipo != "custom" and ps.orientation == "Vertical":#竖
            if ps.adaptive_scale:
                if px.resolution_x>=px.resolution_y or px.resolution_x/px.resolution_y>=dim_w/dim_h:
                    ps.px_x=round(np.multiply(ps.width ,ps.dpi) / numpy.array(2.54))
                    ps.px_y=round(np.prod(np.array([ps.width ,ps.dpi,px.resolution_y])) / np.multiply(2.54,px.resolution_x))
                    ps.width = dim_w
                    ps.height = np.multiply(dim_w,px.resolution_y) / np.array(px.resolution_x)

                elif px.resolution_x/px.resolution_y<dim_w/dim_h:
                    pass
                    ps.px_y=round((ps.height * ps.dpi) / 2.54)
                    ps.px_x=round((ps.height * ps.dpi) / 2.54*px.resolution_x/px.resolution_y)
                    ps.width = dim_h* px.resolution_x / px.resolution_y
                    ps.height = dim_h
            else:
                ps.width = dim_w
                ps.height = dim_h
                ps.px_x = math.ceil((ps.width * ps.dpi) / 2.54)
                ps.px_y = math.ceil((ps.height * ps.dpi) / 2.54)

        # ps.width = (ps.px_x / ps.dpi) * 2.54
        # ps.height = (ps.px_y / ps.dpi) * 2.54


def update_settings_cb(self, context):
    # annoying workaround for recursive call
    if update_settings_cb.level is False:
        update_settings_cb.level = True
        pixels_from_print(self)
        update_settings_cb.level = False

update_settings_cb.level = False

class MyCustomProperties(PropertyGroup):
    unit_from: EnumProperty(
            name="Set from",
            description="Set from",
            items=(
                ("CM_TO_PIXELS", "CM -> Pixel", "Centermeters to Pixels"),
                ("PIXELS_TO_CM", "Pixel -> CM", "Pixels to Centermeters")
                ),
            default="CM_TO_PIXELS",
            )
    # 定义两个整型属性
    px_x: IntProperty(
        name="",
        description="Expected pixel size",
        default=1920,
        min=1,
        max=999999,
        update=update_settings_cb,
    )

    px_y: IntProperty(
        name="",
        description="Expected pixel size",
        default=1080,
        min=1,
        max=999999,
        update=update_settings_cb,
    )
    dpi: IntProperty(
        name="",
        description="Expected pixel size",
        default=72,
        min=1,
        max=2000,
        soft_min = 0,
        step=3,
        soft_max = 300,
        update=update_settings_cb,
    )
    width: FloatProperty(
        name="",
        description="",
        default=21.0,
        min=0.001,
        max=999999.0,
        soft_min = 0.0,
        soft_max = 99.0,
        step = 3,
        precision = 2,
        update=update_settings_cb,
    )

    height: FloatProperty(
        name="",
        description="",
        default=29.7,
        min=0.001,
        max=999999.0,
        soft_min=0.0,
        soft_max=99.0,
        step=3,
        precision=2,
        update=update_settings_cb,
    )
    # 定义一个布尔型属性
    adaptive_scale: BoolProperty(
        name="Adaptive scaling",
        description="Adaptive scaling according to the selected preset",
        default=False
    )
    # turn_on: BoolProperty(
    #     name="Adaptive scaling",
    #     description="Adaptive scaling according to the selected preset",
    #     default=False
    # )
    # 定义一个枚举型属性
    preset: EnumProperty(
        name="Preset",
        description="Rendering preset",
        items=paper_presets,
        default="custom_1_1",
        update=update_settings_cb,
    )
    orientation: EnumProperty(
        name="Page Orientation",
        description="Rendering preset",
        items=[
            ('Vertical', "纵", "Description of option A"),
            ('Horizontal', "横", "Description of option B"),
        ],
        default="Vertical",
        update=update_settings_cb,
    )

    method: EnumProperty(
        name="Method",
        description="Rendering preset",
        items=[
            ('Simple', "简易", "Description of option A"),
            ('Accurate', "精确", "Description of option B"),
        ],
        default="Simple",
    )


# 注册这个属性组
def register():
    bpy.utils.register_class(MyCustomProperties)
    bpy.types.Scene.my_custom_properties = bpy.props.PointerProperty(type=MyCustomProperties)


# 注销这个属性组
def unregister():
    del bpy.types.Scene.my_custom_properties
    bpy.utils.unregister_class(MyCustomProperties)


if __name__ == "__main__":
    register()
