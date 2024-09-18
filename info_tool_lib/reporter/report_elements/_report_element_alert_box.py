from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - alert_box'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --- CONSTANTS: EMOGI -----------------------------------------------------------------------

INFO_EMOGI:    str = 'ℹ️'
WARNING_EMOGI: str = '⚠️'
NOTE_EMOGI:    str = ''
ERROR_EMOGI:   str = '❌'

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_alert_box_element(  text:       str, 
                            alert_type: str = 'info', 
                            emogi:      str = None,
                                ) -> ReportElement:
    
    res      = ReportElement()    
    res.type = ReportElementTypes.ALERT_BOX
        
    alert_type_res = _get_alert_type(alert_type)
    
    if emogi is None:
        emogi = _get_alert_box_emoji(alert_type_res)
        pass
        
    res.body_content = f'''
        <div class=\"grid_12\">
        <div class=\"alert-box {alert_type_res}-box\">
        <span class=\"emoji\">{emogi}</span>
        <span class=\"text\">{text}</span>
        </div>
        </div>
        '''
    
    return res

# --------------------------------------------------------------------------------------------
#
#                                 SUPPORTING FUNCTIONS:
#
# --------------------------------------------------------------------------------------------

def _get_alert_type(alert_type: str) -> str:
    
    if alert_type == 'i' or alert_type == 'info':
        return 'info'
    
    if alert_type == 'w' or alert_type == 'warning':
        return 'warning'
        
    if alert_type == 'n' or alert_type == 'note':
        return 'note'
    
    if alert_type == 'e' or alert_type == 'error':
        return 'error'
    
    return 'info'

# --------------------------------------------------------------------------------------------

def _get_alert_box_emoji(alert_type: str) -> str:
        
    if alert_type == 'info':
        return INFO_EMOGI
    
    if alert_type == 'warning':
        return WARNING_EMOGI
    
    if alert_type == 'note':
        return NOTE_EMOGI
    
    if alert_type == 'error':
        return ERROR_EMOGI

    return INFO_EMOGI

# --------------------------------------------------------------------------------------------