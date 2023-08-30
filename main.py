import os
from pathlib import Path
import sys

import wx
from pdf_report_builder.utils.app_settings import AppSettings

_parent = Path(os.path.abspath(__file__)).parent
AppSettings.set(
    'DATA_PATH',
    Path(_parent / 'pdf_report_builder' / 'data')
)

from pdf_report_builder.ui.main import PDFReportBuilderFrame


if len(sys.argv) > 1:
    try:
        path = Path(sys.argv[1])
    except Exception:
        path = None
else:
    path = None

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = PDFReportBuilderFrame(None, default_path=path)

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()