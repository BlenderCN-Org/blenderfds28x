"""BlenderFDS, preferences panel"""

import bpy
import logging

PKG = __package__

from bpy.types import AddonPreferences
from bpy.props import (
    BoolProperty,
    StringProperty,
    FloatProperty,
    IntProperty,
    EnumProperty,
)

# Get preference value like this:
# context.preferences.addons["blenderfds28x"].preferences.bf_pref_simplify_ui


class BFPreferences(AddonPreferences):
    bl_idname = "blenderfds28x"

    bf_pref_simplify_ui: BoolProperty(
        name="Simplify UI [Blender restart required]",
        description="Simplify BlenderFDS user interface, Blender restart required",
        default=True,
    )

    def update_loglevel(self, context):
        logger = logging.getLogger(PKG)
        logger.setLevel(logging.getLevelName(self.bf_loglevel))

    bf_loglevel: EnumProperty(
        name="Log Level",
        description="Select the log level",
        items=[
            ("DEBUG", "Debug", ""),
            ("INFO", "Info", ""),
            ("WARNING", "Warning", ""),
            ("ERROR", "Error", ""),
            ("CRITICAL", "Critical", ""),
        ],
        update=update_loglevel,
        default="INFO",
    )

    bf_quadriflow_filepath: StringProperty(
        name="Quadriflow",
        description="Quadriflow executable filepath (see: github.com/hjwdzh)",
        subtype="FILE_PATH",
    )

    bf_manifold_filepath: StringProperty(
        name="Manifold",
        description="Manifold executable filepath (see: github.com/hjwdzh)",
        subtype="FILE_PATH",
    )

    bf_simplify_filepath: StringProperty(
        name="Simplify",
        description="Simplify executable filepath (see: github.com/hjwdzh)",
        subtype="FILE_PATH",
    )

    def draw(self, context):
        paths = context.preferences.filepaths
        layout = self.layout
        box = layout.box()
        box.label(text="User Interface")
        # layout.operator("wm.bf_load_blenderfds_settings") # FIXME BF default settings
        box.prop(self, "bf_pref_simplify_ui")
        box.prop(paths, "use_load_ui")
        box.prop(paths, "use_relative_paths")
        box.prop(self, "bf_loglevel")
        box = layout.box()
        box.label(text="External Tools filepaths")
        box.prop(self, "bf_manifold_filepath")
        box.prop(self, "bf_quadriflow_filepath")
        box.prop(self, "bf_simplify_filepath")
        return layout


# Register


def register():
    bpy.utils.register_class(BFPreferences)


def unregister():
    bpy.utils.unregister_class(BFPreferences)
