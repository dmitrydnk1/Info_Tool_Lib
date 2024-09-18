from enum import Enum

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Report Element'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# ============================================================================================

# --------------------------------------------------------------------------------------------
#
#                         REPORT ELEMENT TYPES (ENUM):
#
# --------------------------------------------------------------------------------------------

class ReportElementTypes(Enum):
    
    NONE:                       str = 'none'
    TITLE:                      str = 'title'
    TEXT:                       str = 'text'
    CHART:                      str = 'chart'
    STYLE:                      str = 'style'
    SPACE:                      str = 'space'
    DFTABLE:                    str = 'df_table'
    OTHER:                      str = 'other'
    FOOTER:                     str = 'footer'
    CODE:                       str = 'code'
    ALERT_BOX:                  str = 'alert_box'
    TEXT_CONSOLE:               str = 'text_console'
    HEAD_TITLE_ON_BACKGROUND:   str = 'Head_title_on_background'
    HORIZONTAL_LINE:            str = 'horizontal_line'
    PARAM_VALUE_TABLE:          str = 'param_value_table'
    PARAM_VALUE_TABLE_v2:       str = 'param_value_table_v2'
    PARAM_VALUE_GRID:           str = 'param_value_grid'
    SHOWHIDE_REGION_OPEN:       str = 'showhide_region_open'
    SHOWHIDE_REGION_CLOSE:      str = 'showhide_region_close'
    
    IMAGE_JPEG:                 str = 'image/jpeg'
    IMAGE_PNG:                  str = 'image/png'
    
    pass

# --------------------------------------------------------------------------------------------

def get_report_element_type_str(element_type: ReportElementTypes) -> str:
    '''get the string representation of the enum: ReportElementTypes'''
    return element_type.value

# --------------------------------------------------------------------------------------------
#
#                                 REPORT ELEMENT:
#
# --------------------------------------------------------------------------------------------

class ReportElement():
    
    def __init__(self) -> None:
        
        self.type: ReportElementTypes = ReportElementTypes.NONE        
        
        self.body_content:  str = ''
        self.style_content: str = ''

        pass
    
    # --------------------------------------------------------------------------------------------
    
    def __str__(self) -> str:
        res: str = 'ReportElement: \t' + self.type.value
        return res
    
    # --------------------------------------------------------------------------------------------
    
    def __repr__(self) -> str:
        return self.__str__()
    
    # --------------------------------------------------------------------------------------------
    
    def get_style_str(self) -> str:
        '''
        Returns the style string for the element.
        '''
        return self.style_content
    
    # --------------------------------------------------------------------------------------------
    
    def get_body_str(self) -> str:
        '''
        Returns the body string for the element.
        '''
        return self.body_content
    
    # --------------------------------------------------------------------------------------------

# ==================================================================================================