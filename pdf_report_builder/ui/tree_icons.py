import wx
import os
from pathlib import Path

ICONS_FOLDER = Path(os.getcwd()) / 'pdf_report_builder' \
    / 'data' / 'icons_tree'

def get_tree_images():
    image_list = wx.ImageList(width=24, height=24)
    for file in ICONS_FOLDER.iterdir():
        new_bitmap = wx.Bitmap(width=24, height=24, depth=32)
        new_bitmap.LoadFile(
            str(file)
        )
        image_list.Add(new_bitmap)
    return image_list