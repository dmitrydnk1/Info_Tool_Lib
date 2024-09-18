from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - footer'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_footer_element() -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.FOOTER
    
    res.body_content = f'''
        </div>
        </div>        
        '''
    
    return res

# --------------------------------------------------------------------------------------------