import matplotlib.pyplot as plt
import numpy as np

# ====================================================================================================

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "InfoToolLib - Plot - Plot Ax Flat"
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -------------------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
#
#                             TOOLBOX FOR AX PLOT:
#
# ----------------------------------------------------------------------------------------------------

def flat_style( ax:         plt.Axes | np.ndarray[plt.Axes], 
                fill_alpha: float   = None, 
                    ) -> None:
    '''
    Apply the flat plot style to the axes.
    
    Parameters:
    -----------
    ax:         (`plt.Axes | np.ndarray[plt.Axes]`) : The axes to apply the flat style.
    fill_alpha: (`float`)                           : The alpha value for the fill.
        - Default: `None`.
    '''
    
    # Check if ax is iterable
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            flat_style(ax_, fill_alpha)
            pass
        return
    
    # Hide the right and top spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set color for the left and bottom spines
    ax.spines['left'].set_color('#333333')
    ax.spines['bottom'].set_color('#333333')

    # Set color for the ticks
    ax.tick_params(axis = 'x', colors = '#333333')
    ax.tick_params(axis = 'y', colors = '#333333')

    # Set color for the axis labels
    ax.yaxis.label.set_color('#333333')
    ax.xaxis.label.set_color('#333333')
    
    # Set color and font size for the title and axis labels
    # Fetch current labels and title
    current_title:  str = ax.get_title()
    current_xlabel: str = ax.get_xlabel()
    current_ylabel: str = ax.get_ylabel()
    
    ax.set_title( current_title,  color = '#333333', fontsize = 12)
    ax.set_xlabel(current_xlabel, color = '#333333', fontsize = 10)
    ax.set_ylabel(current_ylabel, color = '#333333', fontsize = 10)
    
    # Rotate x-axis labels and adjust layout
    ax.tick_params(axis = 'x', rotation = 45)
    
    ax.grid(True, color = '#CCCCCC', linestyle = '-', linewidth = 0.5, alpha = 0.7)
    
    # ------------------------
    #    Fill the area
    # ------------------------
    
    if fill_alpha is not None:
        fill_plt(ax, alpha = fill_alpha)    
    
    pass

# ----------------------------------------------------------------------------------------------------------------------

def combine_legends(ax:               plt.Axes | np.ndarray[plt.Axes] | list[plt.Axes], 
                    legend_font_size: str   = None,
                        ) -> None:
    '''
    Combine legends from multiple axes into a single legend on the primary axis.
    
    Parameters:
    -----------
    ax:               (`plt.Axes | np.ndarray[plt.Axes] | list[plt.Axes]`) : The primary axes or a list of axes.
    legend_font_size: (`str`)                                              : The font size for the legend.
        - Default: `None`.
    '''
    
    # Start with the primary axis's handles and labels
    handles, labels = ax.get_legend_handles_labels()
    
    # Attempt to get the twin axes by checking the figures axes
    for ax2 in ax.figure.axes:
        # Skip if it's the same as the original axes
        if ax2 is ax:
            continue
        
        # Check if the axes share an x-axis or y-axis
        if ax2.get_shared_x_axes().joined(ax, ax2) or ax2.get_shared_y_axes().joined(ax, ax2):
            h, l = ax2.get_legend_handles_labels()
            handles += h
            labels  += l
    
    # Create a combined legend on the original axis
    if legend_font_size is not None:
        ax.legend(handles, labels, fontsize = legend_font_size)
    else:
        ax.legend(handles, labels, fontsize = 'small')
    
    pass

# ----------------------------------------------------------------------------------------------------------------------

def fill_plt(   ax:     plt.Axes | np.ndarray[plt.Axes], 
                alpha:  float   = 0.3, 
                    ) -> None:
    '''
    Fill the area between the lines in the plot.
    
    Parameters:
    -----------
    ax:     (`plt.Axes | np.ndarray[plt.Axes]`) : The axes to fill the area between the lines.
    alpha:  (`float`)                          : The alpha value for the fill.
        - Default: `0.3`.
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            fill_plt(ax_, alpha)
        return
    
    # get line data:
    x_data_list = [line.get_xdata() for line in ax.get_lines()]
    y_data_list = [line.get_ydata() for line in ax.get_lines()]
    
    # fill the area between the lines
    for i in range(len(x_data_list)):
        ax.fill_between(x_data_list[i], y_data_list[i], alpha=alpha)
        pass
    
    pass

# ----------------------------------------------------------------------------------------------------------------------

def add_xtick_suffix(   ax:            plt.Axes | np.ndarray[plt.Axes], 
                        x_tick_suffix: str, 
                            ) -> None:
    '''
    Add a suffix to the x-tick labels.
    
    Parameters:
    -----------
    ax:            (`plt.Axes | np.ndarray[plt.Axes]`) : The axes to add the suffix to the x-tick labels.
    x_tick_suffix: (`str`)                             : The suffix to add to the x-tick labels.
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            add_xtick_suffix(ax_, x_tick_suffix)
        return
    
    xtick_labels: list[str] = ax.get_xticklabels()  # Get current x-tick labels        
    new_labels:   list[str] = [label.get_text() + x_tick_suffix for label in xtick_labels] # Create new labels with the suffix
    
    ax.set_xticklabels(new_labels)  # Set the new labels to the axes    
    pass

# ----------------------------------------------------------------------------------------------------------------------

def add_ytick_suffix(   ax:            plt.Axes | np.ndarray[plt.Axes], 
                        y_tick_suffix: str, 
                            ) -> None:
    '''
    Add a suffix to the y-tick labels.
    
    Parameters:
    -----------
    ax:            (`plt.Axes | np.ndarray[plt.Axes]`) : The axes to add the suffix to the y-tick labels.
    y_tick_suffix: (`str`)                             : The suffix to add to the y-tick labels.    
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            add_ytick_suffix(ax_, y_tick_suffix)
        return
    
    ytick_labels: list[str] = ax.get_yticklabels()     # Get current y-tick labels        
    new_labels:   list[str] = [label.get_text() + y_tick_suffix for label in ytick_labels]   # Create new labels with the suffix
    
    ax.set_yticklabels(new_labels)      # Set the new labels to the axes
    pass

# ----------------------------------------------------------------------------------------------------------------------

def yticks_remove_labels(ax: plt.Axes | np.ndarray[plt.Axes]) -> None:
    '''
    Remove the y-tick labels from the axes.
    
    Parameters:
    -----------
    ax: (`plt.Axes | np.ndarray[plt.Axes]`) : The axes to remove the y-tick labels.
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            yticks_remove_labels(ax_)
        return
    
    ax.set_yticklabels([])
    pass

# ----------------------------------------------------------------------------------------------------------------------

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
    ax:       (`plt.Axes | np.ndarray[plt.Axes]`) : The axes object.
    title:    (`str`)                             : The title to set at the bottom.
    color:    (`str | tuple[float, 4] | tuple[float, 3]`) : The color for the title.
        - Default: `#333333`.
    fontsize: (`int`)                             : The font size for the title.
        - Default: `12`.
    location: (`str`)                             : The location for the title.
        - Default: `bottom`.        
    '''
    
    if isinstance(ax, np.ndarray):
        for ax_ in ax:
            set_title_bottom(ax_, title, color, fontsize, location)
        return    
    
    ax.set_title(title, color = color, fontsize = fontsize, va = location)
    pass

# ----------------------------------------------------------------------------------------------------------------------