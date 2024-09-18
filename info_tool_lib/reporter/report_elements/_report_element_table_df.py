import pandas as pd

from ._report_element import ReportElement, ReportElementTypes
from ._value_to_color import value_to_color

# ============================================================================================

__version__:      str = '0.0.7'
__version_date__: str = '2024-09-18'
_name_:           str = 'report element - table dataframe'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.7 @ 2024-09-18 : Updated heatmap spectrum color use, 
#                           for better visibility with heatmap_used_clr_pcnt = 0.6

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_table_dataframe_element(    df: pd.DataFrame, 
                                    highlight_columns             = [], 
                                    round:                  int   = -1, 
                                    heatmap_colormap_name:  str   = 'coolwarm',
                                    heatmap_used_clr_pcnt:  float = 0.6,
                                    heatmap_nan_color:      str   = '#ff0000',
                                    df_min_col_amount_for_full_width: int = 8,
                                        ) -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.DFTABLE
    
    # Adding Scroller:    
    # get columns amount:
    columns_amount = len(df.iloc[0].values)
    
    if columns_amount < df_min_col_amount_for_full_width:
        res.body_content += '<div class=\"grid_12\">'
        pass
    
    res.body_content += '<div class=\"table-scroll-wrapper\">'
    
    # Calculate min and max values for highlighted columns
    min_max_values = {col: (df[col].min(), df[col].max()) for col in highlight_columns if col in df.columns}

    if round >= 0:
        df = df.copy()
        df = df.round(round)
        pass
    
    # Apply the styling using pandas Styler
    styler = df.style.apply(_style_dataframe, 
                            highlight_columns     = highlight_columns, 
                            min_max_values        = min_max_values, 
                            axis                  = None, 
                            heatmap_colormap_name = heatmap_colormap_name,
                            heatmap_nan_color     = heatmap_nan_color,
                            heatmap_used_clr_pcnt = heatmap_used_clr_pcnt, )
    
    # Float Rounding Formating:
    if round >= 0:
        # Set the float format for HTML display
        format_temp = '{:.' + str(round) + 'f}'        
        
        styler = styler.format( format_temp, 
                                na_rep = "-", 
                                subset = pd.IndexSlice[:, df.select_dtypes(include=['float64', 'float32']).columns])
        pass
    
    # Set the class for the table
    styler.set_table_attributes('class="minimalistic-style-table"')
    
    # Convert to HTML
    html_table = styler.to_html(escape = False, border = 0)

    
    res.body_content += html_table
    
    if columns_amount < df_min_col_amount_for_full_width:
        res.body_content += '</div>'
        pass
    
    res.body_content += '</div>'
    
    return res

# --------------------------------------------------------------------------------------------
#
#                              STYLING FUNCTION:
#
# --------------------------------------------------------------------------------------------

def _style_dataframe(   df: pd.DataFrame, 
                        highlight_columns: list[str], 
                        min_max_values, 
                        heatmap_colormap_name: str   = 'coolwarm',
                        heatmap_nan_color:     str   = '#ff0000',
                        heatmap_used_clr_pcnt: float = 0.6,
                            ) -> pd.DataFrame:
    
    styles = pd.DataFrame(  '', 
                            index   = df.index, 
                            columns = df.columns)
    
    for col in highlight_columns:
        
        if col in df.columns:
            # Check if min >= max then skip:
            if min_max_values[col][0] >= min_max_values[col][1]:
                continue
            
            color: str = df[col].apply(value_to_color, args = ( min_max_values[col][0], 
                                                                min_max_values[col][1], 
                                                                heatmap_colormap_name,
                                                                heatmap_nan_color, 
                                                                heatmap_used_clr_pcnt,))
            
            styles[col] = 'background-color: ' + color
            pass
        pass
    
    return styles

# --------------------------------------------------------------------------------------------