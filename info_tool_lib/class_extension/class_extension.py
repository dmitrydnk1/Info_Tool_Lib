import numpy as np
import pandas as pd
import numba

from . import cls_repr_html

from . import VERSION as _LIB_VERSION  # For Ease of Use in a standart way.

# ===========================================================================================

__version__:      str = '0.0.3'
__version_date__: str = '2024-08-15'
_name_:           str = 'Class Info Ext'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: ---------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.3 @ 2024-08-15 : Updated Help Info
#                     : Added call function from __init__ to show version info: get_version()

# ===========================================================================================
#
#               Display Info DECORATORS:
#
# ===========================================================================================

def info_Display_HIDE(func):
    '''
    DECORATOR: Adds the property to the list of properties to hide.
    '''
    def wrapper(self):
        self._display_config: Diplay_Info_Config  # type: ignore
        self._display_config._add_property_to_hide_by_decorator(func)        
        return func(self)
    
    return wrapper

# -------------------------------------------------------------------------------------------

def info_Display_SHOW(func):
    '''
    DECORATOR: Adds the property to the list of properties to show.
    '''
    def wrapper(self):
        self._display_config: Diplay_Info_Config  # type: ignore
        self._display_config._add_property_to_show_by_decorator(func)        
        return func(self)
    
    return wrapper

# ===========================================================================================

# ===========================================================================================
#
#       Display Properties:
#
# ===========================================================================================

class Diplay_Info_Config():
    
    def __init__(self) -> None:
        
        self._VERSION:                 str      = None 
        self.DISPLAY_KEY_TO_IGNORE:    set[str] = set()        
        self.DISPLAY_STANDART_PARAMS:  bool     = True  # Display standart parameters.
                                                        # If False, will display only the parameters 
                                                        # in the _param_val_dict_extra.

        self.DISPLAY_KEY_TO_SHOW:      set[str] = set()        
        self.OBJECT_NAME_SYMBOLE:      str      = '▸'
        self.PARAM_KEY_SYMBOLE:        str      = '•'
        self.DISPLAY_FLOAT_ROUND:      int      = 4        
        self.DISPLAY_PRIVATE_VARS:     bool     = False
        self.DISPLAY_LINE:             bool     = True
        
        self.PARAM_VAL_CUSTOM_TO_SHOW: dict[str, str] = {}        
        self.CUSTOM_OBJECT_NAME:       str            = None
        
        # Properties, and Methods to Ignore, to avoid recursion:
        self._property_names_to_ignore: set[str] = set()        
        self._property_names_to_ignore.update(['_display_config',
                                                'object_name', 
                                                'param_val_dict',
                                                '_pretty_param_val_dict',                                           
                                                '_param_val_dict_extra',    
                                                '_get_display_param_names',    
                                                'get_param_val_dict_pretty',
                                                '_VERSION',
                                                'copy',
                                                'VERSION',
                                                    ])
        
        pass
    
    # --------------------------------------------------------------------------------
    #                 Public Methods:
    # --------------------------------------------------------------------------------
    
    def _add_property_to_hide_by_decorator(self, func):
        self.DISPLAY_KEY_TO_IGNORE.add(func.__name__)
        pass    
    
    # --------------------------------------------------------------------------------
    
    def _add_property_to_show_by_decorator(self, func):
        self.DISPLAY_KEY_TO_SHOW.add(func.__name__)
        pass
    
    # --------------------------------------------------------------------------------
    
    def set_custom_object_name(self, name: str):
        self.CUSTOM_OBJECT_NAME = name
        pass
    
    # --------------------------------------------------------------------------------
    
    def add_to_ignore(self, key: str | list[str]):
        
        if isinstance(key, str):
            self.DISPLAY_KEY_TO_IGNORE.add(key)
            return
        
        for key_item in key:
            self.DISPLAY_KEY_TO_IGNORE.add(key_item)
            pass
        
        pass
    
    # --------------------------------------------------------------------------------
    
    def add_to_show(self, key: str | list[str]):        
        
        if isinstance(key, str):
            self.DISPLAY_KEY_TO_SHOW.add(key)
            return
        
        for key_item in key:
            self.DISPLAY_KEY_TO_SHOW.add(key_item)
            pass        
        pass
    
    # --------------------------------------------------------------------------------
    
    def add_custom_param_val_to_show(self, key: str, val: str):
        self.PARAM_VAL_CUSTOM_TO_SHOW[key] = val
        pass
    
    # --------------------------------------------------------------------------------
    #                IPYTHON DISPLAY Methods:
    # --------------------------------------------------------------------------------
    
    def add_ipython_display_view_A(self, obj):
        '''
        Adds the ipython display view A to the object.
        '''
        
        PARAM_TYPE_MAX_LEN: int = 50
        
        
        def repr_html_func(self):
            
            obj_name: str                         = self.object_name
            param_val_dict_pretty: dict[str, str] = self.get_param_val_dict_pretty()
            param_val_dict:        dict[str, str] = self.param_val_dict
            
            res: str = ''
            
            # --- Main Container: ---
            res += f'<div class="container_PARAM_VAL" {cls_repr_html.CONTAINER_A_STYLE}>'
            
            # --- Title: ---
            res += f'<div class="title_main" {cls_repr_html.TITLE_MAIN_STYLE}>{obj_name}'
            try:
                if self._VERSION is not None:
                    res += f'<span {cls_repr_html.TITLE_MAIN_VERSION_SPAN_STYLE_A}>{self._VERSION}</span></div>'
                else:
                    res += '</div>'
                    pass            
            except:
                res += '</div>'
            
            # --- Devide Line: ---
            # - Single Line:
            res += f'<div {cls_repr_html.DEVIDE_LINE_STYLE}></div>'
            
            # --- Param Val Table: ---
            # Check if param_val_dict is empty:
            if len(param_val_dict_pretty) > 0:
                            
                res += f'<table {cls_repr_html.PARAM_VAL_TABLE_STYLE}>'                
                res += f'''<tr  {cls_repr_html.PARAM_VAL_TABLE_STYLE_TR}>
                            <th {cls_repr_html.PARAM_VAL_TH_STYLE_PARAM}></th>
                            <th {cls_repr_html.PARAM_VAL_TH_STYLE_VALUE}></th></tr>'''
                
                for param_name, param_val in param_val_dict.items():
                    
                    if param_name.startswith('_'):
                        continue
                    
                    # Check if suitable type:
                    if isinstance(param_val, property):
                        param_val = param_val.fget(self)
                        pass
                    
                    if callable(param_val):
                        continue
                    
                    param_val_pretty: str = self._convert_to_pretty_str(param_val)                    
                    param_val_text:   str = cls_repr_html.get_param_val_combined(param_val_pretty, param_val)
                    param_name_text:  str = param_name.replace("_", " ").title()
                    
                    # Param Type:
                    param_type: str = 'UNKNOWN'
                    try:
                        param_type: str = str(numba.typeof(param_val)).replace("Literal", "str").replace("bool_", "bool").replace("unicode_type", "string")
                    except:
                        param_type: str = type(param_val).__name__
                        pass
                    param_type = param_type.replace("#", "").replace("<","[").replace(">","]")
                    
                    # Check for max and trim:
                    if len(param_type) > PARAM_TYPE_MAX_LEN:
                        param_type = param_type[:PARAM_TYPE_MAX_LEN] + ' ..'
                        pass
                    
                    
                    if param_name_text.startswith(' '):
                        param_name_text = param_name_text[1:]
                    
                    res += f'''<tr {cls_repr_html.PARAM_VAL_TABLE_STYLE_TR}>
                                <td>
                                <pre {cls_repr_html.PARAM_VAL_PRE_STYLE_TYPE}>{param_type}</pre>
                                <pre {cls_repr_html.PARAM_VAL_PRE_STYLE_PARAM}>{param_name.title()}</pre></td>
                                <td><pre {cls_repr_html.PARAM_VAL_PRE_STYLE_VALUE}>{param_val_text}</pre></td></tr>'''                    
                    pass
                
                res += f'</table>'                        
                pass
            
            res += f'''<div style="height: 1px;"></p>'''
            res += f'</div>'
            
            return res
        
        obj._repr_html_ = repr_html_func.__get__(obj, obj.__class__)
        
        pass
    
    # --------------------------------------------------------------------------------
    
    def __str__(self) -> str:
        
        res: str = ''
        res += f'DISPLAY INFO CONFIGURATION:\n'
        res += f'============================\n'
        
        if self.CUSTOM_OBJECT_NAME is not None:
            res += f'CUSTOM_OBJECT_NAME = {self.CUSTOM_OBJECT_NAME}\n' 
        
        res += f'OBJECT_NAME_SYMBOLE = {self.OBJECT_NAME_SYMBOLE}\n'
        res += f'PARAM_KEY_SYMBOLE = {self.PARAM_KEY_SYMBOLE}\n'        
        res += f'DISPLAY_FLOAT_ROUND = {self.DISPLAY_FLOAT_ROUND}\n'
        res += f'DISPLAY_PRIVATE_VARS = {self.DISPLAY_PRIVATE_VARS}\n'
        res += f'DISPLAY_LINE = {self.DISPLAY_LINE}\n'
        res += f'DISPLAY_STANDART_PARAMS = {self.DISPLAY_STANDART_PARAMS}\n'
        res += f'DISPLAY_KEY_TO_SHOW (size: {len(self.DISPLAY_KEY_TO_SHOW)}):\n'
        
        for key in self.DISPLAY_KEY_TO_SHOW:
            res += f'\t{key}\n'
        
        res += f'DISPLAY_KEY_TO_IGNORE (size: {len(self.DISPLAY_KEY_TO_IGNORE)}):\n'
        
        for key in self.DISPLAY_KEY_TO_IGNORE:
            res += f'\t{key}\n'
        
        res += f'PARAM_VAL_CUSTOM_TO_SHOW (size: {len(self.PARAM_VAL_CUSTOM_TO_SHOW)}):\n'
        
        for key, val in self.PARAM_VAL_CUSTOM_TO_SHOW.items():
            res += f'\t{key}: {val}\n'
        
        return res
    
    # --------------------------------------------------------------------------------
    
    def __repr__(self) -> str:
        return self.__str__()
    
    pass

# ===========================================================================================



# ===========================================================================================
#
#       Class Extension to Display Information about the Class
#
# ===========================================================================================

class Display_Info_Extension():
    '''
    
    Class to handle displaying information about the class.
    
    ***( (!) Dont forget to initialise the class in the __init__ method: )***
    
    ---
    
    Example:
    -------
    
    ```python
    from info_tool_lib import CLS_INFO               
    
    # Make python doc variables, for future use:
    __version_date__: str = '2024-08-01'
    __version__:      str = '0.0.1'
    
    print(CLS_INFO.VERSION) 
    # -> 'Class Info Lib       VERSION: 0.0.3 @ 2024-08-15'
    
    # Create your new Class, with the CLS_INFO as a parent:    
    class My_Class(CLS_INFO):
        
        def __init__(self):
        # cls_info_initiation:
        super().__init__()
        # Optional Fileds:
        self._VERSION: str = f"VERSION: {__version__}  ( {__version_date__} )"
        self._CLS_hide(['copy',]) # Varibles, and properties to hide.

        # Add your code here:
        ...
        pass
    
    
    # View of the New Class in Jupyter Notebook:    
    my_class = My_Class()
    my_class
    ```
    
    Display Class in the Jupyter Notebook, or details of class parameters in the console.
    
    ---
    
    Key Settings:
    ------------
    
    - Display Configuration:
        >>> self._display_config: Diplay_Info_Config
    
    - Show private variables:
        >>> self._display_config._DISPLAY_PRIVATE_VARS: bool = False
    
    - Display standart parameters:    
        >>> self._display_config.DISPLAY_STANDART_PARAMS: bool = True
    
        If `False`, will display only the parameters in the `_param_val_dict_extra`.
    
    - Set custom object name:    
        >>> @property   
        def object_name(self) -> str:
            return 'My Custom Object Name'
    
    - Set Additional Parameter Values to Show:
        >>> @property
        def _param_val_dict_extra(self) -> dict:
            res = {}
            return res
    
    Additional Settings:
    --------------------
    
    - Float rounding:    
        >>> self._display_config._DISPLAY_FLOAT_ROUND: int = 4
    
    - Use line:    
        >>> self._display_config._DISPLAY_LINE: bool = True
    
    - Decorate object name:    
        >>> self._display_config._OBJECT_NAME_SIMBOLE: str = '▶'
        self._display_config._PARAM_KEY_SIMBOLE:   str = '•'
    
    Properies:
    ---------
    
    - Param Val Dictionary:    
        >>> @property
        def param_val_dict(self) -> dict:
            ...
    
    - Display Object Name:    
        >>> @property
        def object_name(self) -> str:
            ...
    
    ---
    
    Methods:
    --------
    
    - Convert value to pretty string:    
        >>> def _convert_to_pretty_str(self, val) -> str
    
    - Returns pretty dict of the parameter values:    
        >>> def get_param_val_dict_pretty(self) -> dict[str, str]
    
    - Methods to Hide/Show Properties:    
        >>> self._CLS_hide('_param_a')
        self._CLS_show('_param_b')
    
    Decorators SHOW / HIDE:
    ----------------------
    
    ```python    
    # Import the Decorators:
    from info_tool_lib import CLS_INFO, info_Display_HIDE, info_Display_SHOW
    
    # Custom Class with Decorators Example:    
    class My_Class(CLS_INFO):    
        def __init__(self):
            super().__init__()
            self._VERSION: str = f"VERSION: {__version__}  ( {__version_date__} )"
            self._CLS_hide(['copy',]) # Varibles, and properties to hide.            
            pass    
    
        @property
        @info_Display_HIDE
        def param_a(self) -> int:
            return 1
    
        @property
        @info_Display_SHOW
        def _param_b(self) -> int:
            return 2
        
        pass
    '''    
    # ---- CLASS VARIABLES: ----------------------------------------------------------
    
    VERSION: str = _LIB_VERSION
    
    # --------------------------------------------------------------------------------
    
    def __init__(self):
        
        self._display_config: Diplay_Info_Config = Diplay_Info_Config()        
        self._VERSION:        str                = None
        
        pass
    
    # --------------------------------------------------------------------------------
    #               Display Paremeter Methods:
    # --------------------------------------------------------------------------------
    
    def _CLS_hide(self, key: str | list[str]) -> None:
        '''Hides the parameter from the display.'''
        self._display_config.add_to_ignore(key)
        pass
    
    # --------------------------------------------------------------------------------
    
    def _CLS_show(self, key: str | list[str]) -> None:
        '''Forced Show the parameter from the display.'''
        self._display_config.add_to_show(key)
        pass
    
    # --------------------------------------------------------------------------------
    
    def _get_display_param_names(self) -> list[str]:
        '''Returns list of the parameter names to display.'''
        
        name_list:      list[str] = []
        names_to_check: list[str] = dir(self)
        
        # Check all Attributes:        
        for name in names_to_check:
            
            if name.startswith('__'):
                continue            
            
            if name in self._display_config._property_names_to_ignore:
                continue
            
            if name in self._display_config.DISPLAY_KEY_TO_IGNORE:
                continue   
            
            if name in self._display_config.DISPLAY_KEY_TO_SHOW:
                name_list.append(name)
                continue
            
            if name.startswith('_') and self._display_config.DISPLAY_PRIVATE_VARS == False:                
                continue
            
            name_list.append(name)
            pass
        
        return name_list
    
    # --------------------------------------------------------------------------------
    
    @property
    def param_val_dict(self) -> dict[str, str]:
        
        res = {}
        res.update(self._param_val_dict_extra)
        
        if self._display_config.DISPLAY_STANDART_PARAMS == False:
            return res
        
        name_list: list[str] = self._get_display_param_names()
        
        # Generate dict of name and value:
        for name in name_list:
            
            if name in self._display_config._property_names_to_ignore:
                continue
            
            attr_value = getattr(self, name)            
            
            # Check if it's property:
            if isinstance(attr_value, property):
                res[name] = attr_value.fget(self)
            
            # Chack that not callable and not magic method/property:
            if not callable(attr_value) and not name.startswith('__'):
                res[name] = attr_value
            
            pass
        
        return res
    
    # --------------------------------------------------------------------------------
    
    @property
    def object_name(self) -> str:
        
        res: str = self._display_config.CUSTOM_OBJECT_NAME
        if res is None:
            res= f'{self.__class__.__name__}'
        
        res = res.replace("_", " ")
        return res
    
    # --------------------------------------------------------------------------------
    
    @property
    def _param_val_dict_extra(self) -> dict[str, str]:
        res = {}
        return res
    
    # --------------------------------------------------------------------------------
    
    def get_param_val_dict_pretty(self) -> dict[str, str]:
        '''Returns pretty dict of the parameter values.'''
        res = self._pretty_param_val_dict(self.param_val_dict)
        return res
    
    # --------------------------------------------------------------------------------
    
    def _pretty_param_val_dict(self, param_val_dict: dict) -> dict[str, str]:
        '''Converts dict values to pretty string representation.'''
        
        pretty_dict: dict[str, str] = {}
        
        for key, val in param_val_dict.items():
            
            # --- key_str:
            key_str: str = str(key)
            
            if key_str.startswith('_'):
                key_str = key_str[1:]  # Remove first char
            
            key_str = key_str.replace("_", " ")            
            key_str = key_str.title() # Make Capital Each Word
            
            # --- val_str: 
            val_str: str = self._convert_to_pretty_str(val)
            
            pretty_dict[key_str] = val_str
            
        return pretty_dict
    
    # --------------------------------------------------------------------------------
    #               Pretty String Representation Methods:
    # --------------------------------------------------------------------------------
    
    def _get_child_obj_info_flatten(self, obj_str: str) -> str:
        
        MAX_LEN: int = 300
        
        # Check for Max Length:
        if len(obj_str) > MAX_LEN:
            return self._get_shorter_str(obj_str, MAX_LEN)
        
        # Check if have \n:
        if obj_str.count("\n") > 0:
            
            SPACE:   str = ' | '            
            res_val: str = f' '            
            res_val     += obj_str.replace("\n", f"{SPACE}").replace("\t", f"").replace("  ", f"").replace("+", f"")
            
            return res_val
        
        return obj_str
    
    # --------------------------------------------------------------------------------
    
    def _get_shorter_str(self, obj_str: str, max_len: int = 30) -> str:
    
        if len(obj_str) <= max_len:
            return obj_str
        
        res_val: str = obj_str[:max_len - 3] + ' .. '
        return res_val
    
    # --------------------------------------------------------------------------------
    
    def _get_child_obj_info(self, obj_str: str) -> str:
        
        SPACE_OBJ_CHILD_INFO: str = '|'
        
        # Check if have \n:
        if obj_str.count("\n") > 0:
            
            space_str: str = f'  {SPACE_OBJ_CHILD_INFO}  '
            res_val:   str = f'\n{space_str}'            
            res_val       += obj_str.replace("\n", f"\n{space_str}")
            res_val       += '\n '
            return res_val
        
        return obj_str
    
    # --------------------------------------------------------------------------------
    
    def _convert_to_pretty_str(self, val) -> str:
        '''Converts value to pretty string representation.'''
        
        if isinstance(val, float):
            val_str: str = f'{val:.{self._display_config.DISPLAY_FLOAT_ROUND}f}^' 
            val_str: str = val_str.replace("000000^", "").replace("00000^", "").replace("0000^", "").replace("000^", "").replace("00^", "").replace("0^", "").replace("^", "")            
            return val_str
        
        if isinstance(val, np.ndarray):
            res: str = self._convert_to_pretty_str(val.tolist())
            return res
        
        if isinstance(val, pd.DataFrame):
            res: str = f'pd.DataFrame (Shape: {val.shape})'
            return res
        
        if isinstance(val, list):
            if len(val) == 0:
                return '[]'
            
            # Check if it's array of other than float or int or bool: type, e.g. list of objects.
            if not isinstance(val[0], (int, float, bool, str, np.ndarray)):
                return f'[ {type(val[0]).__name__}, .. ] ({len(val)} elements)'
            
            elif len(val) < 4:
                res: str = '['
                
                for i in range(len(val) - 1):
                    res += self._get_list_element_flatten_short_str(val[i])
                    res += ', '
                
                
                res += self._get_list_element_flatten_short_str(val[-1])
                res += ']'
                return res
            
            res: str = f'[{self._get_list_element_flatten_short_str(val[0])}, {self._get_list_element_flatten_short_str(val[1])}, .. , {self._get_list_element_flatten_short_str(val[-1])}] ({len(val)} elements)'            
            return res
        
        if isinstance(val, int):
            return str(val)            
        
        if isinstance(val, str):
            
            if val.count("\n") > 0:
                res_val: str = f''
                res_val     += f'\n \t + '
                res_val     += val.replace("\n", "\n \t + ")
                res_val      = res_val.replace('▸', '\n▸')
                return res_val
            
            res_val: str = str(val)
            res_val      = res_val.replace('▸', '\n▸')
            return res_val
                
        res_val: str = str(val)
        res_val = res_val.replace('▸', '\n▸')
        
        return res_val
        
    
    # --------------------------------------------------------------------------------
    
    def _get_list_element_flatten_short_str(self, element) -> str:
        
        SHORTER_STR_MAX_LEN: int = 30
        
        res: str = self._convert_to_pretty_str(element)
        res      = self._get_child_obj_info_flatten(res)
        res      = self._get_shorter_str(res, SHORTER_STR_MAX_LEN)
        
        return res
    
    # --------------------------------------------------------------------------------
    
    def _calc_repr_str_parameters(  self, 
                                    param_val_dict: dict[str, str], 
                                    object_name:    str, 
                                        ) -> list[int, int]:
        '''Calculates the width of the repr string and the width of the line.'''
        
        KEY_MARGIN:          int = 1
        LINE_MARGIN:         int = 2
        LINE_KEY_VAL_MARGIN: int = 3        
        LINE_SIZE_MAX:       int = 180
        
        obj_name_len: int = len(object_name)
        
        max_key_len:  int = 0
        max_val_len:  int = 0
        
        for key, val in param_val_dict.items():
            max_key_len = max(max_key_len, self._get_length_of_str(key))
            max_val_len = max(max_val_len, self._get_length_of_str(val))
            pass
        
        res_lwidth:     int = max_key_len + KEY_MARGIN
        res_line_width: int = max_key_len + max_val_len + KEY_MARGIN + LINE_KEY_VAL_MARGIN
        res_line_width      = max(res_line_width, obj_name_len)
        res_line_width     += LINE_MARGIN        
        res_line_width      = min(res_line_width, LINE_SIZE_MAX)
        
        return [res_lwidth, res_line_width]
    
    # --------------------------------------------------------------------------------
    
    def _get_length_of_str(self, val: str) -> int:
        '''Returns the length of the string.'''
        
        if not isinstance(val, str):
            return len(val)
        
        res: int = len(val)
        
        if val.count("\n") > 0:
            val_list: list[str] = val.split("\n")
            res = 0
            for val_item in val_list:
                res = max(res, self._get_length_of_str(val_item))
                pass
            pass
        
        return res
    
    # --------------------------------------------------------------------------------
    
    def __str__(self) -> str:
        
        # OBJECT_NAME_SIMBOLE: str = '•◆▶'
        
        param_val_dict_pretty: dict[str, str] = self._pretty_param_val_dict(self.param_val_dict)
        
        object_name: str       = f'{self._display_config.OBJECT_NAME_SYMBOLE} {self.object_name}'        
        repr_val:    list[int] = self._calc_repr_str_parameters(param_val_dict_pretty, object_name)
        _lwidth:     int       = repr_val[0]
        _linewidth:  int       = repr_val[1]
        _line:       str       = '—' * _linewidth

        res: str = ''
        res     += object_name
        
        if len(param_val_dict_pretty) > 0:
            res += f':\n'
            if self._display_config.DISPLAY_LINE:
                res += _line + '\n'

            for key, val in param_val_dict_pretty.items():                
                
                val  = self._check_for_other_object(val, object_symbol = self._display_config.OBJECT_NAME_SYMBOLE)
                res += f'{self._display_config.PARAM_KEY_SYMBOLE} {str(key).ljust(_lwidth)}: {val} \n'
                pass
            
            if self._display_config.DISPLAY_LINE:
                res += _line
                pass
        
        return res
    
    # --------------------------------------------------------------------------------
    
    def __repr__(self) -> str:
        return self.__str__()
    
    # --------------------------------------------------------------------------------
    
    def _check_for_other_object(self, 
                                val:           str, 
                                object_symbol: str, 
                                    ) -> str:
        
        temp_str: str = str(val)
        
        if temp_str[0] == object_symbol:
            res: str = self._get_child_obj_info(temp_str)
            return res
        
        return val
    
    # --------------------------------------------------------------------------------
    #                REPR HTML:
    # --------------------------------------------------------------------------------
    
    def _repr_html_(self) -> str:
        
        PARAM_TYPE_MAX_LEN: int = 50
        
        obj_name:              str            = self.object_name
        param_val_dict_pretty: dict[str, str] = self.get_param_val_dict_pretty()
        param_val_dict:        dict[str, str] = self.param_val_dict
        
        res: str = ''        
        
        res += f'<div class="container_PARAM_VAL" {cls_repr_html.CONTAINER_A_STYLE}>'  # Main Container
        res += f'<div class="title_main" {cls_repr_html.TITLE_MAIN_STYLE}>{obj_name}'  # Title
        
        try:
            if self._VERSION is not None:
                res += f'<span {cls_repr_html.TITLE_MAIN_VERSION_SPAN_STYLE_A}>{self._VERSION}</span></div>'
            else:
                res += '</div>'
        except:
            res += '</div>'
        
        # --- Devide Line: ---
        # - Single Line:
        res += f'<div {cls_repr_html.DEVIDE_LINE_STYLE}></div>'
        
        # --- Param Val Table: ---
        # Check if param_val_dict is empty:
        if len(param_val_dict_pretty) > 0:
                        
            res += f'<table {cls_repr_html.PARAM_VAL_TABLE_STYLE}>'
            res += f'''<tr  {cls_repr_html.PARAM_VAL_TABLE_STYLE_TR}>
                        <th {cls_repr_html.PARAM_VAL_TH_STYLE_PARAM}></th>
                        <th {cls_repr_html.PARAM_VAL_TH_STYLE_VALUE}></th></tr>'''
            
            for param_name, param_val in param_val_dict.items():
                
                if param_name.startswith('_'):
                    continue
                
                # Check if suitable type:
                if isinstance(param_val, property):
                    param_val = param_val.fget(self)
                
                if callable(param_val):
                    continue
                                    
                param_val_pretty: str = self._convert_to_pretty_str(param_val)                
                param_val_text:   str = cls_repr_html.get_param_val_combined(param_val_pretty, param_val)
                param_name_text:  str = param_name.replace("_", " ").title()
                
                # Param Type:
                param_type: str = 'UNKNOWN'
                
                try:
                    param_type: str = str(numba.typeof(param_val)).replace("Literal", "str").replace("bool_", "bool").replace("unicode_type", "string")
                except:
                    param_type: str = type(param_val).__name__
                    pass
                
                param_type = param_type.replace("#", "").replace("<","[").replace(">","]")
                
                # Check for max and trim:
                if len(param_type) > PARAM_TYPE_MAX_LEN:
                    param_type = param_type[:PARAM_TYPE_MAX_LEN] + ' ..'
                
                if param_name_text.startswith(' '):
                    param_name_text = param_name_text[1:]
                
                res += f'''<tr {cls_repr_html.PARAM_VAL_TABLE_STYLE_TR}>
                            <td>
                            <pre {cls_repr_html.PARAM_VAL_PRE_STYLE_TYPE}>{param_type}</pre>
                            <pre {cls_repr_html.PARAM_VAL_PRE_STYLE_PARAM}>{param_name.title()}</pre></td>
                            <td><pre {cls_repr_html.PARAM_VAL_PRE_STYLE_VALUE}>{param_val_text}</pre></td></tr>'''                    
                pass
            
            res += f'</table>'
            pass
        
        res += f'''<div style="height: 1px;"></p>'''
        res += f'</div>'
        
        return res
    
    # ======================================================================================