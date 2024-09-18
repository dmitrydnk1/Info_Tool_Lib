'''
This module provides a set of functions for plotting data using matplotlib.
The functions are organized into sub-modules that provide specific plotting capabilities.

The sub-modules are:
    - plot_ax:        Functions for plotting data on a standard Cartesian plot.
    - plot_ax_polar:  Functions for plotting data on a polar plot.
    - plot_colormaps: Functions for working with colormaps.

The sub-modules can be imported individually or as a group using the following syntax:    
    >>> from tools_module_lib.plt import plt_ax, plt_ax_polar, plt_colormaps

Example Usage `plt_ax`:
-----------------------
```python
import matplotlib.pyplot as plt
import numpy as np
import tools_module_lib as tools

x: np.ndarray[float] = np.linspace(0, 2 * np.pi, 100)
y: np.ndarray[float] = np.sin(x)

fig = plt.figure(figsize = (8, 6), dpi = 100, tight_layout = True)
ax: plt.Axes = fig.add_subplot(1, 1, 1)

ax.plot(x, y, label = 'sin(x)', color = '#605', linestyle = '-', linewidth = 2)
ax.set_title('Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()
tools.plt_ax.apply_xticks_sparse(ax)
tools.plt_ax.flat_style(ax)
plt.show()
```

Example Usage `plt_ax_polar`:
-----------------------------
```python
import matplotlib.pyplot as plt
import numpy as np
import tools_module_lib as tools

r:     np.ndarray[float] = np.linspace(0, 10, 100)
theta: np.ndarray[float] = 2 * np.pi * r

fig = plt.figure(figsize = (8, 6), dpi = 100, tight_layout = True)
ax: plt.Axes = fig.add_subplot(1, 1, 1, polar = True)

ax.plot(theta, r, label = 'r = 2 * pi * r', color = '#605', linestyle = '-', linewidth = 2)
ax.set_title('Spiral Plot')
ax.legend()
ax.grid()
tools.plt_ax_polar.apply_xticks_sparse(ax)
tools.plt_ax_polar.apply_polar_style(ax)
plt.show()
```

Example Usage `plt_colormaps`:
------------------------------
```python
import matplotlib.pyplot as plt
import numpy as np
import tools_module_lib as tools

# View All Colormaps:
tools.plt_colormaps.COLOR_MAP.show_all_colormaps

# Get Colormap Name List:
tools.plt_colormaps.get_colormap_name_list()

# Get Color Hex:
clr_map = tools.plt_colormaps.COLOR_MAP('viridis')
clr_map = tools.plt_colormaps.COLOR_MAP(3)
clr_map = tools.plt_colormaps.COLOR_MAP(colormaps['viridis'])

color_hex: str = clr_map(10)

color_tuple: tuple[float, 4] = clr_map.get_color(10)
color_hex:   str             = clr_map.to_hex(color_tuple)

# Get Colormap By Index:
clr_map = tools.plt_colormaps.get_colormap_by_indx(3)

# Get Color From Colormap:
color_hex:   str             = tools.plt_colormaps.get_color_from_colormap('viridis', 10)
color_tuple: tuple[float, 4] = tools.plt_colormaps.get_color_from_colormap('viridis', 10, as_tuple = True)
color_hex:   str             = tools.plt_colormaps.to_hex(color_tuple)
```

'''


# ======================================================================================================================

__version__:      str = '0.0.5'
__version_date__: str = '2024-08-21'
_name_:           str = 'Info Tool Lib - Plot'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# ----------------------------------------------------------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.4 @ 2024-08-20 : Updated Annotations and Documentation
# v0.0.5 @ 2024-08-21 : Updated visual styles for compatibility with JupiterLab

# ======================================================================================================================
#
#                     FUNCTIONS FOR PLOTTING:
#
# ======================================================================================================================

from . import plot_ax        as plt_ax
from . import plot_ax_polar  as plt_ax_polar
from . import plot_colormaps as plt_color

from .plot_colormaps import (   COLOR_MAP, 
                                get_color_from_colormap, 
                                get_colormap_by_indx, 
                                get_colormap_name_list, 
                                to_hex, )

# ----------------------------------------------------------------------------------------------------------------------