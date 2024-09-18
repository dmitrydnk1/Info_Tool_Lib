from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - code'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_code_element(code: str) -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.CODE
    
    res.body_content = f'''
        <div class=\"grid_12\">
        <pre><code class="python">{code}</code></pre>
        </div>
    '''
    
    return res

# --------------------------------------------------------------------------------------------