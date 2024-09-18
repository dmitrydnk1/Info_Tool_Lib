from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - title'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_title_element(  title:      str, 
                        h_level:    int  = 1, 
                        use_center: bool = False, 
                            ) -> ReportElement:
        
    res      = ReportElement()
    res.type = ReportElementTypes.TITLE
    
    h_level:     int = max(1, min(3, h_level))
    h_tag_title: str = f'<h{h_level}>{title}</h{h_level}>'
    
    if use_center == True:
        res.body_content = f'''
            <div class=\"grid_12\">
            <div id=\"center\">
            <div align=center>
            {h_tag_title}
            </div>
            </div>        
            </div>
        '''
        pass
    else:
        res.body_content = f'''
            <div class=\"grid_12\">
            {h_tag_title}
            </div>
        '''
        pass
        
    return res

# --------------------------------------------------------------------------------------------