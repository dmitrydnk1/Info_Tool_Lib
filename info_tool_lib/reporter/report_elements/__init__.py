'''

'''

# ============================================================================================
#
#                           REPORT ELEMENTS
#
# ============================================================================================

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Reporter - Report Elements'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --------------------------------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --- TODO -----------------------------------------------------------------------------------

# -

# ============================================================================================
#
#                             Report Element Objects:
#
# ============================================================================================

from ._report_element import ReportElement, ReportElementTypes

# --------------------------------------------------------------------------------------------
#
#                                REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

from ._report_element_alert_box         import get_alert_box_element
from ._report_element_chart             import get_chart_element
from ._report_element_code              import get_code_element
from ._report_element_footer            import get_footer_element
from ._report_element_header_title      import get_header_title
from ._report_element_horizontal_line   import get_horizontal_line_element
from ._report_element_param_val_table   import get_param_value_table_element, get_param_value_table_element_v2
from ._report_element_showhide          import get_showhide_region_open_element, get_showhide_region_close_element
from ._report_element_space             import get_space_element
from ._report_element_style             import get_style_element
from ._report_element_table_df          import get_table_dataframe_element
from ._report_element_text              import get_text_element
from ._report_element_text_console      import get_text_console_element
from ._report_element_title             import get_title_element

# --------------------------------------------------------------------------------------------