# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Hy Console",
    "description": "Interactive Hy Console integration for Blender",
    "author": "Kenan Bölükbaşı (kenanb)",
    "version": (0, 1, 0, 'Stable'),
    "blender": (2, 6, 9),
    "location": "Console > Languages menu",
    "wiki_url": "http://www.kenanb.com/lisp-in-blender",
    "tracker_url": "",
    "category": "Development"
    }

def register():
    if "bpy" in locals():
        import imp
        imp.reload(console_hy)	
    else:
        import console_hy

def unregister():
    return {'FINISHED'}

if __name__ == '__main__':
    register()
