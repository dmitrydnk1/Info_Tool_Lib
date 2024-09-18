'''
## Info Tool Library

A Collections of handy tools to view and process daily-routines information, while working with Python, Jupyter to make life easier. 


---

Example Usage:
--------------
    >>> import info_tool_lib
    print(f'{info_tool_lib.VERSION}')

- ### Progress Bar:
    >>> from info_tool_lib import ProgressBar
    # Create a Progress Bar:
    pb: ProgressBar = ProgressBar(100)
    
    for i in range(100):
        pb.update(i)
    pb.finish()

- ### Progress Bar in Jupyter Notebook:    
    ```python
    import numpy as np
    import time
    from info_tool_lib import ProgressBar

    steps: int = 100

    pb = ProgressBar(steps)

    for i in range(steps):        
        pb.step(f'current step: {i}')        
        wait_period: float = 0.03 + np.random.rand() * 0.03        
        time.sleep(wait_period)        
        pass

    # pb.end() # (OPTIONAL) This is not required for Jupyter Notebook.
    ```

- ### Report:    
    >>> from info_tool_lib import ReportHTML
    # Create a Report:
    report: ReportHTML = ReportHTML('My Report')
    report.add_title('My Report')
    report.add_text('This is a sample report.')
    report.save()

- ### Class Extension:
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

- ### ChatBot Message:
    >>> from info_tool_lib import Chat_Bot
    # Create a ChatBot Message:
    chatbot: Chat_Bot = Chat_Bot()
    chatbot.send_message('Hello World!')

- ### Plotting:
    >>> import numpy as np
    import matplotlib.pyplot as plt
    import info_tool_lib
    x: np.ndarray[float] = np.linspace(0, 2 * np.pi, 100)
    y: np.ndarray[float] = np.sin(x)

    fig = plt.subplots(figsize = (7, 5), dpi = 100, tight_layout = True)
    ax: plt.Axes = fig.add_subplot(111)
    ax.plot(x, y)
    info_tool_lib.plt_ax.flat_style(ax)
    plt.show()

- ### Example Polar Plotting:
    >>> import numpy as np
    import matplotlib.pyplot as plt
    import info_tool_lib

    r:     np.ndarray[float] = np.linspace(0, 10, 100)
    theta: np.ndarray[float] = 2 * np.pi * r

    fig = plt.subplots(figsize = (7, 5), dpi = 100, tight_layout = True)
    ax: plt.Axes = fig.add_subplot(111, polar = True)
    ax.plot(theta, r)
    info_tool_lib.plt_ax_polar.flat_style(ax)
    plt.show()

- ### Example Color Map:
    >>> import info_tool_lib
    # View selected Colormaps:
    info_tool_lib.COLOR_MAP.show_colormaps(['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'twilight'])
    # View All Colormaps:
    info_tool_lib.COLOR_MAP.show_all_colormaps


'''

# ---------------------------------------------------------------------------------

_name_:           str = 'Info Tools Lib'
__version__:      str = '0.0.7'
__version_date__: str = '2024-09-18'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VESRSION HISTORY: -----------------------------------------------------------

# v0.0.1 @ 2024-07-13   : Initial Release
# v0.0.2 @ 2024-08-13   : Added Class Extension Module
#                       : Added Plotting Module
#                       : Added Reporter Module
#                       : Added ChatBot Message Module
# v0.0.3 @ 2024-08-15   : Replaced Class Extension Module to a separate package
#                           dew to performance oprimization, as used by most other packages.
#                       : Updated sub-modules dependencies, to reflect transfer of Class Extension Module.
# v0.0.4 @ 2024-08-20   : Updated Annotation and Documentation
# v0.0.5 @ 2024-08-21   : Updated visual styles for compatibility with JupiterLab
# v0.0.6 @ 2024-08-21   : Updated Report Style and Report Elements
#                           Replaced images for header by random generated background images.
#                           Updated package structure, to get rid of unnecessary backgroud images.
# v0.0.7 @ 2024-09-18   : Updated df heat-map range of colors for better visibility.
#                       : Updated the documentation with more examples and use-cases.

# ---------------------------------------------------------------------------------
#
#           Initialize the Report Settings:
#
# ---------------------------------------------------------------------------------

from .reporter import Reports_Settings
Reports_Settings.activate_default_report_path()

# ---------------------------------------------------------------------------------
#
#                  Class Extension:
#
# ---------------------------------------------------------------------------------

from .class_extension import (  CLS_INFO,
                                info_Display_HIDE,
                                info_Display_SHOW, )

# ---------------------------------------------------------------------------------
#
#                   Reporter Module:
#
# ---------------------------------------------------------------------------------

from .reporter import ReportHTML

# ---------------------------------------------------------------------------------
#
#               Plotting Functions Modules:
#
#3 ---------------------------------------------------------------------------------

from .plt import (  plt_ax,                 
                    plt_ax_polar,
                    plt_color,
                    COLOR_MAP,  )

# ---------------------------------------------------------------------------------
#
#                   Progress Bar:
#
# ---------------------------------------------------------------------------------

from .progress_bar import ProgressBar

# ---------------------------------------------------------------------------------
#
#                  ChatBot Messages:
#
# ---------------------------------------------------------------------------------

from .chatbot_status import Chat_Bot

# ---------------------------------------------------------------------------------