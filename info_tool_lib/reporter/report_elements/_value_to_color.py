import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap, rgb2hex


# ================================================================================================

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "Value to color Func."
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: --------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# --- CONSTANT: ----------------------------------------------------------------------------------

COLOR_MAP_NAME_DEFAULT_LIST: list[str] = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
VIRDIS_COLOR_MAP:            Colormap  = plt.get_cmap('viridis')

# ================================================================================================
#
#               Functions for Get heatmap color from value
#
# ================================================================================================

# --- FUNCTIONS: ---------------------------------------------------------------------------------

def generate_hex_colors_list(   colormap: Colormap = VIRDIS_COLOR_MAP, 
                                amount:   int      = 20, 
                                    ) -> list[str]:
    '''
    Generate a list of HEX colors from a colormap.
    '''    
    # Generate n evenly spaced colors from the colormap
    colors     = colormap(np.linspace(0, 1, amount))
    hex_colors = [rgb2hex(color) for color in colors]   # Convert the colors to HEX format
    
    return hex_colors

# ------------------------------------------------------------------------------------------------

def value_to_color( value:             float, 
                    min_value:         float, 
                    max_value:         float, 
                    colormap_name:     str   = 'viridis',                    
                    nan_color:         str   = '#ff0000',
                    used_palette_part: float = 0.4  ,
                        ) -> str:
    '''
    Return the HEX color value for a given value based on the colormap.
    
    Parameters:
    -----------
    value:             (`float`) : Value to be converted to color.
    min_value:         (`float`) : Minimum value of the range.
    max_value:         (`float`) : Maximum value of the range.
    colormap_name:     (`str`)   : Name of the colormap to be used.
        - Default: 'viridis'
    nan_color:         (`str`)   : HEX color to be used for NaN values.
        - Default: '#ff0000'
    used_palette_part: (`float`) : The part of the palette to be used.
        - Default: 0.4 (40% of the palette). Should be between 0.05 and 1.0.
    
    Returns:
    --------
    (`str`) : HEX color value.
    
    Example:
    --------
    >>> res_color: str = value_to_color(value             = 0.5,
                                        min_value         = 0, 
                                        max_value         = 1,
                                        colormap_name     = 'viridis',
                                        nan_color         = '#ff0000', 
                                        used_palette_part = 0.4, )
    >>> print(res_color)
    '#7fff7f'
    '''    
    
    # check if value is NaN
    if np.isnan(value):
        return nan_color
    
    # Check if colormap_name is valid
    if colormap_name not in plt.colormaps():
        emergency_colormap: str = COLOR_MAP_NAME_DEFAULT_LIST[0]
        print(f'!!! ERROR !!! Invalid colormap name: {colormap_name}')
        print(f'WILL USE DEFAULT COLORMAP NAMED:     {emergency_colormap}')
        print(f'A few valid colormap names:')
        
        for cmap_name in COLOR_MAP_NAME_DEFAULT_LIST:
            print(f'    {cmap_name}')
        
        colormap_name = emergency_colormap # Update to default colormap
        pass
    
    colormap: Colormap = plt.get_cmap(colormap_name)
    
    # Normalize the value to the range [0, 1] based on the min and max values
    normalized_value: float = (value - min_value) / (max_value - min_value)
    normalized_value        = np.clip(normalized_value, 0, 1)    
    used_palette_part       = max(0.05, min(1.0, used_palette_part))  # Limit the value between 0.05 and 1.0
    normalized_value        = 0.5 * (1.0 - used_palette_part) + normalized_value * used_palette_part  # Adding the offset
    
    # Get the color from the colormap
    color = colormap(normalized_value)
    
    # Convert the color to HEX format    
    hex_color: str = rgb2hex(color)
    
    return hex_color

# ------------------------------------------------------------------------------------------------