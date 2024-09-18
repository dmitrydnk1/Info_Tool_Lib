'''

## Tools Module Library - Reporter

This module provides a simple and easy to use HTML Report Generator, with a set of predefined styles.

---

Example Usage:
--------------
```python
from info_tool_lib import ReportHTML

# Create a Report:
report: ReportHTML = ReportHTML('My Report')
report.add_title('My Report')
report.add_text('This is a sample report.')
report.save()
```

'''


# ===========================================================================================

__version__:      str = '0.0.7'
__version_date__: str = '2024-09-18'
_name_:           str = 'Info Tool Lib - Reporter'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.4 @ 2024-08-20 : Updated Annotation and Documentation
# v0.0.6 @ 2024-08-21 : Updated Report Style and Report Elements
#                     : Replaced images for header by random generated background images.
#                     : Updated package structure, to get rid of unnecessary backgroud images.
# v0.0.7 @ 2024-09-18 : Updated df heat-map range of colors for better visibility.

# -------------------------------------------------------------------------------------------
#
#             Report Style:
#
# -------------------------------------------------------------------------------------------

from .report_elements._report_style import REPORT_STYLE as _REPORT_STYLE

# -------------------------------------------------------------------------------------------
#
#                     General Configuration Settings:
#
# -------------------------------------------------------------------------------------------

from .report import Reports_Settings

# -------------------------------------------------------------------------------------------
#
#                   Report Generator:
#
# -------------------------------------------------------------------------------------------

from .report import ReportHTML

# -------------------------------------------------------------------------------------------