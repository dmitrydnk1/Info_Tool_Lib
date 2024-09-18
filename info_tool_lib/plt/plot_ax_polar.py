import matplotlib.pyplot as plt
import numpy as np

# ====================================================================================================

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "InfoToolLib - Plot - Plot Ax Polar"
VESRSION:         str = f"{_name_:<20} VERSION: {__version__} @ {__version_date__}"

# --- VESRSION HISTORY: ------------------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# ====================================================================================================


# ====================================================================================================
#
#                             TOOLBOX FOR AX PLOT POLAR:
#
# ====================================================================================================

def apply_xticks_sparse(ax: plt.Axes | np.ndarray[plt.Axes]) -> None:
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            apply_xticks_sparse(ax_)
        return
        
    # Define angles for major and minor x-axis ticks
    angles_in_degrees = [0, 90, 180, 270]
    angles_in_radians = np.deg2rad(angles_in_degrees)
    
    ax.set_xticks(angles_in_radians)
    ax.set_xticklabels([f'{angle}°' for angle in angles_in_degrees])
    ax.set_xticks(np.deg2rad(range(0, 360, 15)), minor = True)  # Ensure gridlines are shown at 45-degree intervals    
    ax.grid(which = 'minor', linestyle = ':', linewidth = 1.0)  # Set grid for minor ticks
    
    pass

# ---------------------------------------------------------------------------------------------------

def apply_polar_style(ax: plt.Axes | np.ndarray[plt.Axes]) -> None:
    '''
    Apply the polar plot style to the axes.
    
    Parameters:
    -----------
    ax: (`plt.Axes | np.ndarray[plt.Axes]`) : The polar plot axes.
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            apply_polar_style(ax_)
        return
    
    
    # Check that ax not polar:
    flag_polar_plot: bool = ax.spines.keys().__contains__('polar')
    
    if flag_polar_plot == False:
        print('Polar plot NOT detected. Cannot apply polar style.')
        return ax
    
    ax: plt.Axes = ax
        
    ax.set_theta_zero_location('NW')     # Set 0 degrees to the top    
    ax.set_theta_direction(-1)           # Set the direction of theta to be clockwise
    
    # Set color for the ticks
    ax.tick_params(axis = 'x', colors = '#333333')
    ax.tick_params(axis = 'y', colors = '#333333')

    # Set color for the axis labels
    ax.yaxis.label.set_color('#333333')
    ax.xaxis.label.set_color('#333333')

    # Set color and font size for the title and axis labels
    # Fetch current labels and title
    current_title  = ax.get_title()
    current_xlabel = ax.get_xlabel()
    current_ylabel = ax.get_ylabel()
    
    ax.set_title( current_title,  color = '#333333', fontsize = 12)
    ax.set_xlabel(current_xlabel, color = '#333333', fontsize = 10)
    ax.set_ylabel(current_ylabel, color = '#333333', fontsize = 10)
        
    # Set the grid
    ax.grid(color = '#cccccc', linestyle = '-', linewidth = 0.5, alpha = 0.7)
    
    apply_xticks_sparse(ax)
    
    yticks_remove_labels(ax)
    
    pass

# ------------------------------------------------------------------------------------------------

def apply_polar_xticks( ax:         plt.Axes | np.ndarray[plt.Axes], 
                        angle_step: float       = 45, 
                            ) -> None:
    '''
    Transform the x-ticks to polar plot format.
    
    Parameters:
    -----------
    ax:         (`plt.Axes | np.ndarray[plt.Axes]`) : The polar plot axes.
    angle_step: (`float`)                           : The angle step for the x-ticks.
        - Default: `45` degrees.    
    '''
        
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            apply_polar_xticks(ax_, angle_step)
        return    
    
    EPS_VAL: float = 1e-6
    
    x_ticks_arr = np.arange(0, 360 + EPS_VAL, angle_step, dtype = int)
    ax.set_xticks(x_ticks_arr, labels = [f'{i:3d}°' for i in x_ticks_arr])
    
    pass

# ------------------------------------------------------------------------------------------------

def yticks_remove_labels(ax: plt.Axes| np.ndarray[plt.Axes]) -> None:
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            yticks_remove_labels(ax_)
        return
    
    ax.set_yticklabels([])
    pass

# ------------------------------------------------------------------------------------------------

def set_title_bottom(   ax:       plt.Axes | np.ndarray[plt.Axes], 
                        title:    str, 
                        color:    str | tuple[float, 4] | tuple[float, 3] = '#333333', 
                        fontsize: int       = 12, 
                        location: str       = 'bottom', 
                            ) -> None:
    '''
    Set the title at the bottom of the plot.
    
    Parameters:
    -----------
    ax:       (`plt.Axes | np.ndarray[plt.Axes]`)         : The axes object.
    title:    (`str`)                                     : The title string.
    color:    (`str | tuple[float, 4] | tuple[float, 3]`) : The color of the title.
        - Default: `'#333333'`.
    fontsize: (`int`)                                     : The font size of the title.
        - Default: `12`.
    location: (`str`)                                     : The location of the title.
        - Default: `'bottom'`.
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            set_title_bottom(ax_, title, color, fontsize, location)
        return
    
    ax.set_title(title, color = color, fontsize = fontsize, va = location)
    pass

# ------------------------------------------------------------------------------------------------