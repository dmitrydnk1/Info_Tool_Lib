'''
Plot Colormaps Example:
-----------------------

```python
# View All Colormaps:
plt_color.COLOR_MAP.show_all_colormaps

# Get Colormap Name List:
plt_color.get_colormap_name_list()

# Get Color Hex:
clr_map = plt_color.COLOR_MAP('viridis')
clr_map = plt_color.COLOR_MAP(3)
clr_map = plt_color.COLOR_MAP(colormaps['viridis'])

color_hex: str = clr_map(10)

color_tuple: tuple[float, 4] = clr_map.get_color(10)
color_hex: str = clr_map.to_hex(color_tuple)
```
'''

from matplotlib        import colormaps
from matplotlib.colors import Colormap

from . import _cls_repr_html_plot as _cls_repr_html

# ======================================================================================================================

_colormaps_name_list = list(colormaps)

# --------------------------------------------------------------------------------------------

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "InfoToolLib - Plot - Plot Colormaps"
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# --- CONSTANTS & CFG: -----------------------------------------------------------------------

COLORS_AMOUNT_TO_SHOW:  int = 18
COLOR_MAP_DEFAULT_NAME: str = 'viridis'

# --------------------------------------------------------------------------------------------
#
#                            PLOT COLORMAPS FUNCTIONS:
#
# --------------------------------------------------------------------------------------------

class _CLR_MAPS_DISPLAY(object):
    
    def __init__(self, display_content: str):
        self.display_content = display_content
        pass
    
    def _repr_html_(self) -> str:
        return self.display_content
    
    pass

# --------------------------------------------------------------------------------------------
#
#                            COLOR MAP CLASS:
#
# --------------------------------------------------------------------------------------------


class COLOR_MAP(object):
    '''
    
    COLOR MAP object
    
    
    Example:
    --------
    
    - ### View All Colormaps in Jupyter Notebook:
    ```python
    # To vew all colormaps:
    COLOR_MAP.show_colormaps()    
    # to vew colormaps by index:
    COLOR_MAP.show_colormaps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])    
    # to view colormaps by names:
    COLOR_MAP.show_colormaps(['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'twilight'])
    ```
    
    - ### Make Color Map Object (`clr_map`):
    ```python    
    color_map: str | Colormap | int = 'viridis'
    # Set value with one of options:
    color_map = 'viridis'
    color_map = 3
    color_map = colormaps['viridis']        
    
    # Default Pallete Size:
    size_pallete: int = 100
    
    # Create Object:
    clr_map = COLOR_MAP(color_map, size_pallete)
    ```
    
    - ### Access Color:
    ```python    
    color_hex: str = clr_map.get_color_hex(10)
    color_hex: str = clr_map(10)
    
    color_A = clr_map[0]
    color_B = clr_map[50]
    color_C = clr_map[0.5]
    color_D = clr_map.get_color(0.3)
    color_E = clr_map.get_color(10)
    
    max_colors: int = 120
    color_val: int = 10
    color_F = clr_map.get_color(color_val, max_colors)    
    
    # TO HEX:
    color_hex: str = clr_map.to_hex(color_A)
    ```
    
    - ### UPDATE COLOR MAP:
    ```python
    # update with one of the options:    
    clr_map.set_colormap('plasma')
    clr_map.set_colormap(3)
    clr_map.set_colormap(colormaps['plasma'])
    
    # Update Pallete Size:
    clr_map.set_size(200)
    ```
    
    '''
    
    def __init__(   self, 
                    color_map:    str | Colormap | int | None = None, 
                    size_pallete: int       = 100, 
                        ) -> None:        
        
        self._VERSION: str = f'VERSION: {__version__}'
        
        self.color_map = colormaps[COLOR_MAP_DEFAULT_NAME]
        
        if color_map is not None:
            self.set_colormap(color_map)
        
        self.size_pallete : int = size_pallete
        
        pass
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def __call__(   self, 
                    color_indx:     int | float, 
                    color_map:      str | Colormap | int | None = None, 
                    color_indx_max: int                         = None, 
                        ) -> str:
        '''
        Get Color Hex:
        
        Parameters:
        -----------
        color_indx:     (`int | float`) : The Color Index to get the color.
        color_map:      (`str | Colormap | int | None`) : If used, change the color map.
            - Default: `None`.
        color_indx_max: (`int`) : If used, the max color index for int color_indx.
            - Default: `None`.
        
        Returns:
        --------
        res_hex_color: (`str`) : Result Hex Color of the Color Index.
        
        Example:
        --------
        >>> color_hex: str = clr_map(10)
        >>> color_hex: str = clr_map(10, 'plasma')
        >>> color_hex: str = clr_map(10, 3)
        >>> color_hex: str = clr_map(10, colormaps['plasma'])
        >>> color_hex: str = clr_map(10, 'plasma', 120)
        >>> color_hex: str = clr_map(10, 3, 120)
        >>> color_hex: str = clr_map(10, colormaps['plasma'], 120)        
        '''

        if color_map is not None:
            self.set_colormap(color_map)
        
        res_hex_color: str = self.to_hex(self.get_color(color_indx, color_indx_max))
        return res_hex_color
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def get_color(  self,   
                    color_indx:     int | float, 
                    color_indx_max: int         = None, 
                        ) -> tuple[float, 4]:
        '''
        Get Color Tuple:
        
        Parameters:
        -----------
        color_indx:     (`int | float`) : The Color Index to get the color.
        color_indx_max: (`int`) : If used, the max color index for int color_indx.
            - Default: `None`.
        
        Returns:
        --------
        res_color: (`tuple[float, 4]`) : Result Color Tuple of the Color Index.
        
        Example:
        --------
        >>> color_A = clr_map[0]
        >>> color_B = clr_map[50]
        >>> color_C = clr_map[0.5]
        >>> color_D = clr_map.get_color(0.3)
        >>> color_E = clr_map.get_color(10)        
        '''
        
        if color_indx_max is None:
            color_indx_max = self.size_pallete
        
        # Check if color_indx is int:
        if type(color_indx) is int:
            res_color = self.color_map(float(color_indx) / float(self.size_pallete))
            return res_color
        
        if type(color_indx) is float:
            res_color = self.color_map(color_indx)
            return res_color
        
        res_color = self.color_map(float(color_indx) / float(color_indx_max))
        
        return res_color
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def get_color_hex(  self, 
                        color_indx:     int | float, 
                        color_indx_max: int         = None, 
                            ) -> str:
        '''
        Get Color Hex:
        
        Parameters:
        -----------
        color_indx:     (`int | float`) : The Color Index to get the color.
        color_indx_max: (`int`) : If used, the max color index for int color_indx.
            - Default: `None`.
        
        Returns:
        --------
        res_color_hex: (`str`) : Result Hex Color of the Color Index.
        
        Example:
        --------
        >>> color_hex: str = clr_map.get_color_hex(10)
        >>> color_hex: str = clr_map.get_color_hex(10, 120)
        '''
        
        res_color     = self.get_color(color_indx, color_indx_max)
        res_color_hex = self.to_hex(res_color)
        
        return res_color_hex
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def get_colormap(self) -> Colormap:
        '''
        Get the current colormap.
        
        Returns:
        --------
        res_colormap: (`Colormap`) : The current colormap.
        
        Example:
        --------
        >>> colormap = clr_map.get_colormap()
        '''
        return self.color_map
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def to_hex( self, 
                color_val:  tuple[float, 4] | tuple[float, 3], 
                keep_alpha: bool        = False, 
                    ) -> str:
        '''
        Transform Color Tuple to Hex Color.
        
        Parameters:
        -----------
        color_val:  (`tuple[float, 4] | tuple[float, 3]`) : The Color Tuple to transform to Hex.
        keep_alpha: (`bool`) : If True, keep the alpha channel in the hex color.
            - Default: `False`.
        
        Returns:
        --------
        res_hex: (`str`) : The Hex Color of the Color Tuple.
        
        Example:
        --------
        >>> color_hex = clr_map.to_hex(color_A)
        >>> color_hex = clr_map.to_hex(color_A, keep_alpha = True)        
        '''
        
        if not keep_alpha:
            color_val = color_val[:3]
        
        res_hex: str = "#" + "".join(format(round(val * 255), "02x") for val in color_val)    
        
        return res_hex
    
    # ------------------------------------------------------------------------------------------------------------------
        
    def _repr_html_(self) -> str:

        res: str = ''
        
        res += f'<div {_cls_repr_html.CONTAINER_A_STYLE}>'        
        res += f'<h2  {_cls_repr_html.TITLE_MAIN_STYLE}>COLOR MAP: {self.color_map.name} <span{_cls_repr_html.TITLE_MAIN_VERSION_SPAN_STYLE_B}>{self._VERSION}</span></h2>'
        res += f'<div {_cls_repr_html.PARAM_VAL_PRE_STYLE_TYPE}>Color Pallete Size: <span {_cls_repr_html.PARAM_VAL_PRE_STYLE_VALUE}> {self.size_pallete}</span></div>'        
        res += f'<div {_cls_repr_html.DEVIDE_LINE_STYLE}"></div>'
        
        
        res += f'<div style="display: flex; flex-wrap: wrap; justify-content: space-around; align-items: left;">'
        for i in range(self.size_pallete):
            result_color     = self.color_map(float(i) / self.size_pallete)
            result_color_hex = self.to_hex(result_color)            
            res             += f'<div style="background-color: {result_color_hex}; width: 35px; height: 50px; margin: 5px; font-size: 12px; padding: 5; border-radius: 2px; text-align: center; color: #222;, box-shadow: 0px 3px 3px 0px rgba(0,0,0,0.5);"> {i:03d}</div>'
            pass
        
        res += '</div>'
        res += '</div>'
        
        return res
    
    # ------------------------------------------------------------------------------------------------------------------
        
    def set_size(self, size_int: int) -> None:        
        self.size_pallete = size_int
        pass
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def set_colormap(self, color_map: str | Colormap | int) -> None:
        
        if type(color_map) is str:
            self.color_map = colormaps[color_map]
            pass
        
        elif type(color_map) is int:
            self.color_map = colormaps[_colormaps_name_list[color_map % len(_colormaps_name_list)]]
            pass
        
        elif type(color_map) is Colormap:
            self.color_map = color_map
            pass
        
        pass
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def _show_colormap( 
                        name:          str, 
                        idx:           int, 
                        colors_amount: int,
                            ) -> str:
        
        res: str = ""
        
        res += f'<div style="margin: 5, 5, 5, 5; padding: 5, 5, 5, 5;">'
        res += f'<div {_cls_repr_html.CONTAINER_A_STYLE}>'
        res += f'<h2  {_cls_repr_html.TITLE_MAIN_STYLE}>{name} <span{_cls_repr_html.TITLE_MAIN_VERSION_SPAN_STYLE_B}>ID: {idx}</span></h2>'
        res += f'<div {_cls_repr_html.DEVIDE_LINE_STYLE_B_DARKPART}></div>'
        
        # make the content grouped in left:
        res += f'<div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: left;">'        
        
        colormap_temp = colormaps[name]        
        
        for i in range(colors_amount):
            result_color     = colormap_temp(float(i) / colors_amount)
            result_color_hex = COLOR_MAP.to_hex(result_color)            
            res             += f'<div style="background-color: {result_color_hex}; width: 20px; height: 40px; margin: 2px; font-size: 12px; padding: 5; border-radius: 2px; text-align: center; color: #222;, box-shadow: 0px 3px 3px 0px rgba(0,0,0,0.5);"> </div>'
            pass
        
        res += '</div>'
        res += f'<div {_cls_repr_html.SPACE_STYLE}></div>'
        res += '</div>'
        res += f'<div {_cls_repr_html.SPACE_STYLE}></div>'
        res += '</div>'
        
        return res    
    
    # ------------------------------------------------------------------------------------------------------------------    
    
    def __getitem__(self, i: int | float) -> tuple[float, 4]:        
        return self.get_color(i)
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @property
    def show_all_colormaps(self) -> _CLR_MAPS_DISPLAY:
        return self.show_colormaps(_colormaps_name_list)       
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def show_all_colormaps() -> _CLR_MAPS_DISPLAY:
        return COLOR_MAP.show_colormaps(_colormaps_name_list)
    
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_colormap_name_list() -> list[str]:
        return _colormaps_name_list
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def get_colormap_amount() -> int:
        return len(_colormaps_name_list)    
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def to_hex( color_val:  tuple[float, 4] | tuple[float, 3], 
                keep_alpha: bool        = False,
                    ) -> str:
        
        if not keep_alpha:
            color_val = color_val[:3]
        
        res_hex: str = "#" + "".join(format(round(val * 255), "02x") for val in color_val)
        
        return res_hex
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def get_colormap_by_indx(colormap_indx: int, ) -> Colormap:
        
        colormap_name:   str      = _colormaps_name_list[colormap_indx % len(_colormaps_name_list)]
        result_colormap: Colormap = colormaps[colormap_name]
        return result_colormap
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def get_color_from_colormap(    colormap:       Colormap, 
                                    color_indx:     int, 
                                    color_indx_max: int, 
                                        ) -> tuple[float, 4]:
        
        result_color = colormap(float(color_indx) / float(color_indx_max))
        return result_color
    
    # ------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def show_colormaps( color_map_names: list[str] | list[int] = None) -> _CLR_MAPS_DISPLAY:
        
        if color_map_names is None:
            color_map_names = _colormaps_name_list
        
        res: str = ""        
        res     += '<h1 style="text-align: center;">COLOR MAPS:</h1>'       # TITILE
        res     += '<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">'
        
        if isinstance(color_map_names[0], int):
            color_map_names = [ _colormaps_name_list[indx % len(_colormaps_name_list)] for indx in color_map_names ]
        
        for color_map_name in color_map_names:            
            res += COLOR_MAP._show_colormap(color_map_name, _colormaps_name_list.index(color_map_name), COLORS_AMOUNT_TO_SHOW)            
            pass
        
        res += '</div>'
        
        clr_map_display = _CLR_MAPS_DISPLAY(res)
        
        return clr_map_display
    
    # ------------------------------------------------------------------------------------------------------------------
    
# ======================================================================================================================
#
#                            PLOT COLORMAPS FUNCTIONS:
#
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------

def get_colormap_name_list() -> list[str]:
    return _colormaps_name_list

# ----------------------------------------------------------------------------------------------------------------------

def to_hex( color_val:  tuple[float, 4] | tuple[float, 3], 
            keep_alpha: bool        = False, 
                ) -> str:
    
    if not keep_alpha:
        color_val = color_val[:3]
    
    res_hex: str = "#" + "".join(format(round(val * 255), "02x") for val in color_val)
    return res_hex

# ----------------------------------------------------------------------------------------------------------------------

def get_colormap_by_indx(colormap_indx: int) -> Colormap:
    
    colormap_name: str      = _colormaps_name_list[colormap_indx % len(_colormaps_name_list)]
    res_colormap:  Colormap = colormaps[colormap_name]
        
    return res_colormap
    
# ----------------------------------------------------------------------------------------------------------------------
    
def get_color_from_colormap(    colormap:       Colormap, 
                                color_indx:     int, 
                                color_indx_max: int, 
                                    ) -> tuple[float, 4]:
    
    res_color = colormap(float(color_indx) / float(color_indx_max))
    
    return res_color

# ----------------------------------------------------------------------------------------------------------------------

def show_all_colormaps( color_map_names: list[str] | list[int] = None, 
                                ) -> _CLR_MAPS_DISPLAY:
        
    if color_map_names is None:
        color_map_names = _colormaps_name_list
    
    return COLOR_MAP.show_colormaps(color_map_names)

# ----------------------------------------------------------------------------------------------------------------------