from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - show/hide region'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --- TODO : ---------------------------------------------------------------------------------
# - TODO: use_hide not workingh yet.

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_showhide_region_open_element(   title:       str, 
                                        region_name: str, 
                                        use_hide:    bool = True, # TODO: not working yet, to FIX.
                                            ) -> ReportElement:
    '''
    use_hide not workingh yet.
    '''
    res      = ReportElement()
    res.type = ReportElementTypes.SHOWHIDE_REGION_OPEN
    
    res.body_content = f'''
        <button class="toggle-button" onclick="toggleContent('{region_name}', this, '{title}')">▶ Show {title}</button>        
        <div class="content_show_hide" id="{region_name}">
        '''
            
    return res

# --------------------------------------------------------------------------------------------

def get_showhide_region_close_element() -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.SHOWHIDE_REGION_CLOSE
    
    res.body_content = f'''      
        </div>    
        '''
    
    return res

# --------------------------------------------------------------------------------------------