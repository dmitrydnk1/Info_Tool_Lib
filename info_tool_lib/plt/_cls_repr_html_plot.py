# -------------------------------------------------------------------------------------------------------

__version__:      str = '0.0.5'
__version_date__: str = '2024-08-21'
_name_:           str = 'Plot - Report Elements'
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VESRSION HISTORY: ---------------------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.5 @ 2024-08-21 : Updated visual styles for compatibility with JupiterLab

# =======================================================================================================
#
#                   BLOCKS STYLES COLLECTION:
#
# =======================================================================================================

# -------------------------------------------------------------------------------------------------------
#
#                           CONTAINER STYLE:
#
# -------------------------------------------------------------------------------------------------------

CONTAINER_A_STYLE: str = '''    
style="
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    font-size: 14px;
    color: #C5C5C5;
    width: 100%;
    min-width: 600px;
    background-color: #1c1c1e;
    background-image: linear-gradient(145deg, #1c1c1e, #16181d);
    box-sizing: border-box;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0,0,0,0.5);
    margin-top: 2px;
    align-items: left;
"
'''

# -------------------------------------------------------------------------------------------------------
#
#                           TITLE MAIN STYLE:
#
# -------------------------------------------------------------------------------------------------------

TITLE_MAIN_STYLE: str = '''
style="
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    font-size: 30px;
    color: #C2D2D2;
    display: block;
    padding: 5px 0 0 20px;
"
'''

# ========================================================================================================
#
#                    TITLE MAIN VERSION SPAN STYLE:
#
# ========================================================================================================

TITLE_MAIN_VERSION_SPAN_STYLE_A: str = '''
style="
    font-size: 14px;     
    opacity: 0.4;
    padding-left: 10px;
    "
'''

TITLE_MAIN_VERSION_SPAN_STYLE_B: str = '''
style="
    font-size: 16px; 
    opacity: 0.6; 
    padding-left: 10px;
    "
'''

TITLE_MAIN_VERSION_SPAN_STYLE_C: str = '''
style="
    font-size: 18px; 
    # text-decoration: underline; 
    color: #99AFAF; 
    padding-left: 10px;
    "
'''

TITLE_MAIN_VERSION_SUB_STYLE_D: str = '''
style="
    font-size: 14px;
    opacity: 0.5; 
    color: #A9B8B8; 
    padding-left: 5px;
    "
'''

# -------------------------------------------------------------------------------------------------------
#
#                           DEVIDE LINE STYLE:
#
# -------------------------------------------------------------------------------------------------------

DEVIDE_LINE_STYLE: str = '''
style="
    border: 0;
    height: 1px;
    background: #333333;        
    background-image: linear-gradient(to right, rgba(80,210,180, 0.4), rgba(70,200,200, 0.4));
    margin: 10px 0;
    padding: 0;        
    "
'''        

DEVIDE_LINE_STYLE_B_DARKPART: str = '''
style="
    border: 0;
    height: 1px;
    background: #333333;            
    background-image: linear-gradient(to right, rgba(0,0,0, 0.4), rgba(0,0,0, 0.6), rgba(0,0,0, 0.4));
    margin: 0;
    padding: 0;        
    "
'''        

DEVIDE_LINE_STYLE_B_LIGHTPART: str = '''
style="
    border: 0;
    height: 1px;
    background: #333333;            
    background-image: linear-gradient(to right, rgba(255,255,255, 0.1), rgba(255,255,255, 0.2), rgba(255,255,255, 0.1));
    margin: 0;
    padding: 0;        
    "
'''        

# -------------------------------------------------------------------------------------------------------
#
#                             PARAM VALUE TABLE STYLES:
#
# -------------------------------------------------------------------------------------------------------

PARAM_VAL_TABLE_STYLE: str = '''
style="
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    font-size: 16px;
    color: #D2D2D2;
    padding: 0;
    margin: 0;
    border-collapse: collapse;
    width: 97%;
    border-spacing: 0px 1px;
    overflow: auto;
    border-radius: 8px;
    text-align: left;
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------
    
PARAM_VAL_TABLE_STYLE_TR: str = '''
style="
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------
    
PARAM_VAL_PRE_STYLE_VALUE: str = '''
style="
    padding: 1px 10px;
    margin: 0;
    text-align: left;
    font-size: 16px;
    color: #D2D2D2;
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------

PARAM_VAL_PRE_STYLE_PARAM: str = '''
style="
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    font-weight: 400;
    font-size: 16px;
    color: #37C9B0;
    padding: 0px 10px ;
    margin: 0;
    text-align: left;
    background-color: transparent;
    "
    '''

#  -------------------------------------------------------------------------------------------------------

PARAM_VAL_PRE_STYLE_TYPE: str = '''
style="
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    font-weight: 400;
    font-size: 11px;
    color: #A88F6D;
    padding: 0 10px ;
    margin: 0;
    text-align: left;
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------    

PARAM_VAL_TH_STYLE_PARAM: str = '''
style="        
    font-family: 'Optimistic Display', -apple-system, ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    padding: 5px 10px ;
    margin: 0;
    text-align: left;
    width: 15%;        
    width-max: 25%;
    background-color: transparent;    
    "
    '''

# -------------------------------------------------------------------------------------------------------

PARAM_VAL_TH_STYLE_VALUE: str = '''
style="        
    padding: 1px 10px;
    margin: 0;
    text-align: left;
    width: 80%;
    width-max: 80%;
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------
#
#                      SPACE STYLE:
#
# -------------------------------------------------------------------------------------------------------

SPACE_STYLE: str = '''
style="
    padding: 0;
    margin: 0;
    height: 30px;
    background-color: transparent;
    "
    '''

# -------------------------------------------------------------------------------------------------------