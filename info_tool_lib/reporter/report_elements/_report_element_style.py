from ._report_element import ReportElement, ReportElementTypes
from ._report_style import REPORT_STYLE

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - style'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_style_element() -> ReportElement:
    '''
    Returns the style element.
    '''
    res      = ReportElement()
    res.type = ReportElementTypes.STYLE
    
    res.style_content = REPORT_STYLE
    
    return res

# --------------------------------------------------------------------------------------------