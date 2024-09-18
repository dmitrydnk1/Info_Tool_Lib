from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - param value table'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------
#
#                                  REPORT ELEMENTS:
#
# --------------------------------------------------------------------------------------------

def get_param_value_table_element(  param_value_table: dict[str, str] | list[(str, str)], 
                                    title:             str = '', 
                                    cfg_truncate_len:  int = 60,
                                        ) -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.PARAM_VALUE_TABLE
    
    res.body_content = '<div class=\"grid_12\">'
    
    if title:
        res.body_content += f'<h2>{title}</h2>'
    
    res.body_content += '<div class="param-value-element">'
    
    param_val_list = list(param_value_table.items()) if isinstance(param_value_table, dict) else param_value_table
    param_val_list.reverse()  
    
    for param, val in param_val_list:
        
        val = str(val)
        
        if len(val) > cfg_truncate_len:
            val = _short_str(val, max_length = cfg_truncate_len)
            pass
        
        param_text_class: str = 'param-value-text'
        
        if len(val) > cfg_truncate_len // 2:
            param_text_class += ' param-value-text-long'
        
        res.body_content += f'''
            <div class="param-value-item">
                <div class="param-value-caption">{param}</div>
                <div class="{param_text_class}">{val}</div>
            </div>
        '''
    
    res.body_content += '</div>'
    res.body_content += '</div>'
    
    return res

# --------------------------------------------------------------------------------------------

def get_param_value_table_element_v2(   param_value_table: dict[str, str] | list[(str, str)], 
                                        title:             str = '', 
                                            ) -> ReportElement:
    
    res      = ReportElement()
    res.type = ReportElementTypes.PARAM_VALUE_TABLE_v2
    
    res.body_content = '<div class=\"grid_12\">'
    
    if title != '':
        res.body_content += f'<h2>{title}</h2>'
    
    param_val_list = list(param_value_table.items()) if isinstance(param_value_table, dict) else param_value_table.copy()
    param_val_list.reverse()
    
    # Start the table with the class 'param-val-style-table' applied
    res.body_content += '<table class="param-val-style-table">'
    
    # Add table head
    res.body_content += '''
        <thead>
            <tr>
                <th>Parameter Name</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
    '''
    
    for param, val in param_val_list:
        val = _short_str(val)  # Assuming _short_str is a function to shorten or process the string value
        res.body_content += f'''
            <tr>
                <td>{param}</td>
                <td>{val}</td>
            </tr>
        '''
    
    res.body_content += '</tbody></table></div>'
    
    return res

# --------------------------------------------------------------------------------------------
#
#                                 SUPPORTING FUNCTIONS:
#
# --------------------------------------------------------------------------------------------

def _short_str( val, 
                max_length: int = 60, 
                    ) -> str:
    
    res: str = None
    if type(val) == float:
        res: str = _short_float(val)
        pass
        
    elif type(val) == list:
        res: str = _short_repr(val)
        pass
    
    else:
        res: str = str(val)
        pass
        
    res: str = _truncate_long_string(res, max_length = max_length)
        
    return res

# --------------------------------------------------------------------------------------------

def _short_repr(    arr: list, 
                    n:   int = 2, 
                        ) -> str:
    
    if type(arr) != list:
        return arr
    
    if len(arr) > n + 1:
        return str(arr[:n])[:-1] + ', .., ' + str(arr[-1]) + ']'
    else:
        return str(arr)

# --------------------------------------------------------------------------------------------

def _short_float(   val: float,
                    n:   int = 4, 
                        ) -> str:
    
    if type(val) == float:
        return str(round(val, n))    
    # else:    
    return str(val)

# --------------------------------------------------------------------------------------------

def _truncate_long_string(  string:     str, 
                            max_length: int = 60, 
                                ) -> str:
    '''
    Truncates the given string to the given max_length.
    '''
    if len(string) <= max_length:
        return string
    
    return string[:max_length] + '...'

# --------------------------------------------------------------------------------------------