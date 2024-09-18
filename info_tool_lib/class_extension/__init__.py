'''
## Class extension to display class variables.

***( (!) Dont forget to initialise the class in the __init__ method: )***

---

Example:
--------

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
-------------

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
----------

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
    ```

'''

# --------------------------------------------------------------------------

_name_:           str = 'Class Info Extension'
__version__:      str = '0.0.4'
__version_date__: str = '2024-08-21'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: ------------------------------------------------------

# v0.0.3 @ 2024-08-15 : Initial Release of sub-module.
# v0.0.4 @ 2024-08-21 : Updated the documentation.
#                     : Updated styles for better compatibility with the Jupyter Notebook.#

# --------------------------------------------------------------------------
#
#                 Class Extension:
#
# --------------------------------------------------------------------------

from .class_extension import (  Display_Info_Extension as CLS_INFO,
                                Diplay_Info_Config, 
                                info_Display_HIDE,
                                info_Display_SHOW, )

# --------------------------------------------------------------------------
#
#        Functions for preparing repr elements in NUMBA:
#
# --------------------------------------------------------------------------

from .cls_repr_numba import (   param_val_list_signature, 
                                repr_numba_add_param_val_array_int64, 
                                repr_numba_add_param_val_array_float64, 
                                repr_numba_add_param_val_array_float64_2d,
                                repr_numba_get_repr_str,                
                                repr_numba_float64_to_str,              
                                repr_numba_detail_compact_param_str,
                                repr_numba_float32_to_str,              
                                repr_numba_add_param_val_array_float32, 
                                repr_numba_add_param_val_array_float32_2d,  
                                repr_numba_add_param_val_array_int32,   )

# --------------------------------------------------------------------------