import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import keyring

import os
import re
import webbrowser

from datetime import datetime


try:
    from .report_favicon  import _get_base64_favicon
    from .report_elements import (  ReportElement, 
                                    ReportElementTypes, 
                                    get_space_element, 
                                    get_title_element, 
                                    get_text_element, 
                                    get_code_element, 
                                    get_text_console_element,
                                    get_chart_element, 
                                    get_table_dataframe_element,
                                    get_alert_box_element, 
                                    get_horizontal_line_element,
                                    get_param_value_table_element, 
                                    get_param_value_table_element_v2,
                                    get_showhide_region_open_element, 
                                    get_showhide_region_close_element,
                                    get_header_title, 
                                    get_footer_element, 
                                    get_style_element, )
    pass

except:
    from report_favicon  import _get_base64_favicon
    from report_elements import (   ReportElement, 
                                    ReportElementTypes, 
                                    get_space_element, 
                                    get_title_element, 
                                    get_text_element, 
                                    get_code_element, 
                                    get_text_console_element,
                                    get_chart_element, 
                                    get_table_dataframe_element,
                                    get_alert_box_element, 
                                    get_horizontal_line_element,
                                    get_param_value_table_element, 
                                    get_param_value_table_element_v2,
                                    get_showhide_region_open_element, 
                                    get_showhide_region_close_element,
                                    get_header_title, 
                                    get_footer_element, 
                                    get_style_element, )

    pass

# ============================================================================================

__version__:      str = '0.0.6'
__version_date__: str = '2024-08-21'
_name_:           str = 'Tools - Reporter'
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.4 @ 2024-08-20 : Updated Annotations and Documentation
# v0.0.6 @ 2024-08-21 : Updated Report Style and Report Elements
#                     : Replaced images for header by random generated background images.
#                     : Updated package structure, to get rid of unnecessary backgroud images.

# --- TODO : ---------------------------------------------------------------------------------

# - TODO: Make Suitable to work with the Plot objects, of various size.
# - TODO: Update default Color Scheme for Tables Heatmaps. df_heatmap_colormap_name

# --- CONSTANTS: -----------------------------------------------------------------------------

DEFAULT_REPORT_TITLE: str = 'Report'

# --------------------------------------------------------------------------------------------
#
#                   REPORT SETTINGS:
#
# --------------------------------------------------------------------------------------------

class Reports_Settings():
    
    _folder_path:      str = 'Reports\\'
    _report_file_name: str = 'report'
    _file_format:      str = '.html'
    
    # Constants:
    __SERVICE_NAME:       str = 'info_tool_lib'
    __REPORTS_FOLDER_KEY: str = 'reports_folder_keyring'
    
    custom_folder_path:   str = None
    
    param_value_table_truncate_length: int   = 60
    df_heatmap_nan_color:              str   = '#ff0000' 
    df_heatmap_colormap_name:          str   = 'coolwarm'
    df_heatmap_used_clr_pcnt:          float = 0.6
    df_min_col_amount_for_full_width:  int   = 8
    
    use_open_saved_file:            bool = True
    use_header_title_on_background: bool = True
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def set_deafult_report_path(folder_path: str) -> None:
        '''
        Set the default folder path for the reports.
        '''
        if folder_path[-1] != '\\':
            folder_path += '\\'
            pass
        
        Reports_Settings._folder_path = folder_path        
        keyring.set_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY, folder_path)        
        
        print(f'Updated default reports folder path: {Reports_Settings._folder_path}')
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def get_deafult_report_path() -> str:
        '''
        Get the default folder path for the reports.
        '''        
        folder_path = keyring.get_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY)
        return folder_path
        
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def activate_default_report_path() -> None:
        '''
        Activate the default folder path for the reports.
        '''
        try:
            new_path = Reports_Settings.get_deafult_report_path()
            if new_path is not None:
                Reports_Settings._folder_path = new_path
                pass        
        except:
            pass
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def reset_deafult_report_path() -> None:
        '''
        Reset the default folder path for the reports.
        '''        
        keyring.delete_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY)
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def set_folder_path(folder_path: str) -> None:
        '''
        Set the folder path for the reports.
        '''
        Reports_Settings._folder_path = folder_path
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def set_file_name(file_name: str) -> None:
        '''
        Set the file name for the reports.
        '''
        Reports_Settings._report_file_name = file_name
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def disable_open_saved_file() -> None:
        '''
        Disable open saved file.
        '''
        Reports_Settings.use_open_saved_file = False
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def enable_open_saved_file() -> None:
        '''
        Enable open saved file.
        '''
        Reports_Settings.use_open_saved_file = True
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def disable_header_title_on_background() -> None:
        '''
        Disable header title on background.
        '''
        Reports_Settings.use_header_title_on_background = False
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def enable_header_title_on_background() -> None:
        '''
        Enable header title on background.
        '''
        Reports_Settings.use_header_title_on_background = True
        pass
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def info() -> None:
        '''
        Print the current settings.
        '''
        print('Reports Settings: \n')
        print(f'------------------- \n')
        print(f'+ Folder Path:         {Reports_Settings._folder_path}')
        print(f'+ Custom Folder Path:  {Reports_Settings.custom_folder_path}')
        print(f'+ File Name:           {Reports_Settings._report_file_name}')
        print(f'+ File Format:         {Reports_Settings._file_format}')
        print(f'+ Use Open Saved File: {Reports_Settings.use_open_saved_file}')
        print(f'+ Use Header Title:    {Reports_Settings.use_header_title_on_background}')
        pass
    
    # --------------------------------------------------------------------------------------------
    
    pass

# ------------------------------------------------------------------------------------------------
#
#                                   REPORT HTML CLASS:
#
# ------------------------------------------------------------------------------------------------

class ReportHTML():
    '''
    HTML Report Constructor.
    
    Example:
    --------
    ```python
    from info_tool_lib import ReportHTML
    
    report: ReportHTML = ReportHTML(title                = 'My Report',
                                    sub_title            = 'My Sub Title',
                                    file_name            = 'my_report',
                                    use_title_background = True,
                                    open_saved_file      = True)
    
    report.add_title('My Title')
    report.add_text('My Text')
    report.save()
    ```
    
    '''
    
    _show_hide_region_id_counter: int = 0
    
    # --------------------------------------------------------------------------------------------
    
    @staticmethod
    def _get_show_hide_region_id() -> str:
        '''
        Returns the show hide region id.
        '''
        ReportHTML._show_hide_region_id_counter += 1
        return f'show_hide_region_{ReportHTML._show_hide_region_id_counter}'
    
    # --------------------------------------------------------------------------------------------
    
    def __init__(   self, 
                    title:                str  = None, 
                    sub_title:            str  = None, 
                    file_name:            str  = None, 
                    use_title_background: bool = True, 
                    open_saved_file:      bool = None
                        ) -> None:
        '''
        ReportHTML Constructor.
        
        Parameters:
        ----------
        title                (str):  title of the report. (Optional)
            - default: `None`
        sub_title            (str):  sub title of the report. (Optional)
            - default: `None`
        file_name            (str):  file name of the report. (Optional)
            - default: `None`
        use_title_background (bool): if True, then use title background. (Optional)
            - default: `True`
        open_saved_file      (bool): if True, then open saved file. (Optional)
            - default: `None`
        
        Example:
        --------
        ```python
        from info_tool_lib import ReportHTML        
        report: ReportHTML = ReportHTML(title                = 'My Report',
                                        sub_title            = 'My Sub Title',
                                        file_name            = 'my_report',
                                        use_title_background = True,
                                        open_saved_file      = True)
        
        report.add_title('My Title')
        report.add_text('My Text')
        report.save()
        ```
        
        
        '''
        
        
        # --- CONSTANTS: -------------------------
        
        self._USE_TRANSPARENT_PLOTS: bool = True
        
        # --- SETTINGS: --------------------------
        
        self.folder_path: str = Reports_Settings._folder_path
        
        if Reports_Settings.custom_folder_path is not None:
            self.folder_path: str = Reports_Settings.custom_folder_path
            pass
        
        self.report_file_name: str = Reports_Settings._report_file_name
        
        if title is not None:
            self.report_file_name = title
        
        if file_name is not None:
            self.report_file_name = file_name
        
        self.file_format: str = Reports_Settings._file_format
        
        self.title: str = DEFAULT_REPORT_TITLE
        if title is not None:
            self.title = title
            
        self.sub_title:            str  = self._get_current_date_time()
        self.use_custom_sub_title: bool = False
        
        if sub_title is not None:
            self.sub_title            = sub_title
            self.use_custom_sub_title = True
            pass
        
        self._file_name: str = self._sanitize_filename(self.report_file_name)
        self._file_path: str = self.folder_path + self._file_name + self.file_format
        
        self.use_open_saved_file: bool = Reports_Settings.use_open_saved_file
        if open_saved_file is not None:
            self.use_open_saved_file = open_saved_file
        
        self.use_title_background: bool = use_title_background
        
        self.elements_list:        list[ReportElement] = []        
        self.bottom_elements_list: list[ReportElement] = []  # Elements to add to the bottom of the report.
        
        self._initialize()
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def __str__(self) -> str:
        
        _lwidth: int = 25
        _line:   str = '-' * 40             
        res:     str = ''
        
        res += 'ReportHTML: \n'
        res += _line + '\n'
        res += f'+ {str("Folder Path").ljust(_lwidth)}: {self.folder_path} \n'
        res += f'+ {str("Report File Name").ljust(_lwidth)}: {self.report_file_name} \n'
        res += f'+ {str("File Name").ljust(_lwidth)}: {self._file_name} \n'
        res += f'+ {str("File Format").ljust(_lwidth)}: {self.file_format} \n'
        res += f'+ {str("Title").ljust(_lwidth)}: {self.title} \n'
        res += f'+ {str("File Path").ljust(_lwidth)}: {self._file_path} \n'
        res += f'+ {str("Use Open Saved File").ljust(_lwidth)}: {self.use_open_saved_file} \n'
        res += f'+ {str("Use Title Background").ljust(_lwidth)}: {self.use_title_background} \n'
        res += f'+ {str("Elements Count").ljust(_lwidth)}: {len(self.elements_list)} \n'
        
        for element in self.elements_list:
            res += f'\t + {element.type} \n'
            pass
                
        res += _line + '\n'
        
        return res
    
    # --------------------------------------------------------------------------------------------
    
    def __repr__(self) -> str:
        return self.__str__()
    
    # --------------------------------------------------------------------------------------------
    
    def _initialize(self) -> None:
        '''
        Initialize the report.
        '''
        self.elements_list = []
        
        self.elements_list.append(get_style_element())
        
        element_header_title = get_header_title(title       = self.title,
                                                subtitle    = self.sub_title,
                                                use_background_image = self.use_title_background)
        
        self.elements_list.append(element_header_title)
        
        pass
    
    # --------------------------------------------------------------------------------------------

    def save_to_file(self)-> None:
        '''
        Save the report to the file.
        '''
        # Check if the folder exists:
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            pass
        
        self._file_name = self.report_file_name
        self._file_name = self._sanitize_filename(self._file_name)
        
        # Construct the full file path
        self._file_path = os.path.join(self.folder_path, self._file_name + self.file_format)        
        
        # if file exists, then update the filename, and save the file.        
        while os.path.exists(self._file_path):
            self._file_name = self._update_filename(self._file_name)
            self._file_path = os.path.join(self.folder_path, self._file_name + self.file_format)
            pass
        
        # UPDATING SUBTITLE FOR DEFAULT SETTINGS WITH FILENAME:        
        if self.use_custom_sub_title == False:
            self.sub_title = self.sub_title + f'<p><p>{self._file_name}'
            self.update_header_title(subtitle = self.sub_title)            
            pass
        
        
        # Save the HTML content to the file
        with open(self._file_path, 'w', encoding="utf-8") as file:
            file.write(self._get_html_str())

        # Optionally open the file after saving
        if self.use_open_saved_file:
            webbrowser.open_new_tab(self._file_path)        
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def save(self) -> None:
        '''
        Save the report to the file.
        '''
        self.save_to_file()
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def enable_open_saved_file(self) -> None:
        '''
        Enable open saved file.
        '''
        self.use_open_saved_file = True
        pass
    
    # --------------------------------------------------------------------------------------------
        
    def disable_open_saved_file(self) -> None:
        '''
        Disable open saved file.
        '''
        self.use_open_saved_file = False
        pass    
    
    # --------------------------------------------------------------------------------------------
    
    def update_header_title(self, 
                            title:                str  = None, 
                            subtitle:             str  = None, 
                            use_title_background: bool = None, 
                                ) -> None:
        '''
        Update the header title.
        if title is None, then the title will be updated from class variable.
        
        Parameters:
        ----------
        title                (str):  title of the report. (Optional)
            - default: `None`
        subtitle             (str):  sub title of the report. (Optional)
            - default: `None`
        use_title_background (bool): if True, then use title background. (Optional)
            - default: `None`
            
        Example:
        --------
        >>> report.update_header_title( title                = 'My New Title', 
                                        subtitle             = 'My New Sub Title', 
                                        use_title_background = True, )
        '''
        
        if title is not None:
            self.title = title
            pass
        
        if subtitle is not None:
            self.sub_title = subtitle
            pass
        
        if use_title_background is not None:
            self.use_title_background = use_title_background
            pass
        
        header_element = get_header_title(  title    = self.title, 
                                            subtitle = self.sub_title, 
                                            use_background_image = self.use_title_background)
        
        self.elements_list[1] = header_element
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_horizontal_line(self) -> None:
        '''
        Add horizontal line to the report.
        '''
        self.elements_list.append(get_horizontal_line_element())
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_space(self) -> None:
        '''
        Add space to the report.
        '''
        self.elements_list.append(get_space_element())
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_title(  self, 
                    title:      str, 
                    h_level:    int  = 1, 
                    use_center: bool = False,
                        ) -> None:
        '''
        Add title to the report.
        
        Parameters:
        ----------
        title      (str): title of the report.
        h_level    (int): heading level. (Optional)
            - can be 1, 2, 3
            - default: 1
        use_center (bool): if True, then use center alignment. (Optional)
            - default: False
        
        Example:
        --------        
        >>> report.add_title(   title      = 'My Title', 
                                h_level    = 1, 
                                use_center = False)
        '''
        self.elements_list.append(get_title_element(title, 
                                                    h_level    = h_level, 
                                                    use_center = use_center))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_text(self, text: str) -> None:
        '''
        Add text to the report.
        
        Parameters:
        ----------
        text (str): text to add to the report.
        
        Example:
        --------
        >>> report.add_text(text = 'My Text')
        >>> long_text: str = \''' My Long Text 
        ...                    My Long Text not over yet.
        ...                    My long tex is still going on. \'''
        >>> report.add_text(text = long_text)
        '''
        self.elements_list.append(get_text_element(text))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_text_console(self, text: str) -> None:
        '''
        Add text to the report, in console style.
        
        Parameters:
        ----------
        text (str): text to add to the report.
        
        Example:
        --------
        >>> report.add_text_console(text = 'My Text')
        >>> long_text: str = \''' My Long Text
        ...                    My Long Text not over yet.
        ...                    My long tex is still going on. \'''
        >>> report.add_text_console(text = long_text)        
        '''
        self.elements_list.append(get_text_console_element(text))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_chart(  self, 
                    chart_plt:     plt, 
                    use_fullwidth: bool = False, 
                    heigth:        int  = None, 
                    width:         int  = None, 
                        ) -> None:
        '''
        Add chart to the report.
        
        Parameters:
        ----------
        chart_plt     ('plt') : matplotlib chart.
        use_fullwidth ('bool'): if True, allow full width. 
            - (default: 'False')
        heigth        ('int') : chart heigth in pixels.
            - (Optional)
        width         ('int') : chart width in pixels.
            - (Optional)
        
        Example:
        --------
        >>> plt.figure(figsize = (4, 8), dpi = 100, tight_layout = True)
        >>> plt.plot([1, 2, 3, 4])
        >>> plt.ylabel('Some numbers')
        >>> report.add_chart(chart_plt        = plt,
                                use_fullwidth = False,
                                heigth        = 400,
                                width         = 800)
        '''
        
        use_transparent_plots: bool = self._USE_TRANSPARENT_PLOTS
        
        self.elements_list.append(get_chart_element(chart_plt, 
                                                    use_fullwidth         = use_fullwidth, 
                                                    heigth                = heigth, 
                                                    width                 = width, 
                                                    use_transparent_plots = use_transparent_plots, ))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_plot(   self, 
                    plot_plt:      plt, 
                    use_fullwidth: bool = False, 
                    heigth:        int  = None, 
                    width:         int  = None, 
                        ) -> None:
        '''
        Add plot to the report.
        
        Parameters:
        ----------
        plot_plt      ('plt') : matplotlib plot.
        use_fullwidth ('bool'): if True, allow full width.
            - (default: 'False')
        heigth        ('int') : chart heigth in pixels.
            - (Optional)
        width         ('int') : chart width in pixels.
            - (Optional)
        
        Example:
        --------
        >>> plt.figure(figsize = (4, 8), dpi = 100, tight_layout = True)
        >>> plt.plot([1, 2, 3, 4])
        >>> report.add_plot(plot_plt      = plt,
                            use_fullwidth = False,
                            heigth        = 400,
                            width         = 800)
        '''
        
        self.add_chart( plot_plt, 
                        use_fullwidth, 
                        heigth, 
                        width, )
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_dataframe_table(self, 
                            df:                 pd.DataFrame, 
                            highlight_columns:  list[str] = [], 
                            round:              int       = -1, 
                            color_map_name:     str       = Reports_Settings.df_heatmap_colormap_name,
                            used_part_of_color: float     = Reports_Settings.df_heatmap_used_clr_pcnt,
                                ) -> None:
        '''
        Add dataframe table to the report, from pandas dataframe.
        
        Parameters:
        ----------
        df                ('pd.DataFrame'): pandas dataframe.
        highlight_columns ('[str]')       : list of columns names to highlight values in a table by heatmap.
            - if empty, then no columns will be highlighted.
        round             ('int')         : round the values in the table to the given number of digits after the decimal point.
            - if -1, then no rounding will be done.
        color_map_name    ('str')         : name of the color map to use for the heatmap.
            - (default: 'coolwarm')
        used_part_of_color ('float')      : part of the color map to use for the heatmap.
            - (default: 0.4)
            Should be between 0.05 and 1.0.
        
        Example:
        --------
        >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
        >>> report.add_dataframe_table( df,
                                        highlight_columns  = ['A'],
                                        round              = 2,
                                        color_map_name     = 'coolwarm',
                                        used_part_of_color = 0.4)        
        '''
                
        self.elements_list.append(get_table_dataframe_element(  df, 
                                                                highlight_columns, 
                                                                round, 
                                                                color_map_name,
                                                                used_part_of_color,
                                                                Reports_Settings.df_heatmap_nan_color,
                                                                Reports_Settings.df_min_col_amount_for_full_width))
        pass
    
    # --------------------------------------------------------------------------------------------    
    
    def add_df_table(   self, 
                        df:                pd.DataFrame, 
                        highlight_columns: list[str] = [], 
                        round:             int       = -1, 
                            ) -> None:
        '''
        Add dataframe table to the report, from pandas dataframe.
        
        Parameters:
        ----------
        df                ('pd.DataFrame'): pandas dataframe.
        highlight_columns ('[str]')       : list of columns names to highlight values in a table by heatmap.
            - if empty, then no columns will be highlighted.
            - (Default: `[]`)
        round             ('int')         : round the values in the table to the given number of digits after the decimal point.
            - if -1, then no rounding will be done.
            - (Default: `-1`)
        
        Example:
        --------
        >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
        >>> report.add_df_table(df,
                                highlight_columns = ['A'],
                                round             = 2)            
        '''
        
        self.add_dataframe_table(   df, 
                                    highlight_columns, 
                                    round)
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_param_value_table(  self, 
                                pv_data:       dict[str, str] | list[(str, str)], 
                                title:         str  = '', 
                                use_big_table: bool = False, 
                                    ) -> None:
        '''
        Add param value table to the report.
        
        Parameters:
        ----------
        pv_data       ('dict[str, str] | list[(str, str)]') : dictionary of param name and value.
        title         ('str')                               : title of the table.
            - (Default: '')
        use_big_table ('bool')                              : if True, then use big table style.
            - (Default: `False`)
        
        Example:
        --------
        >>> pv_data: dict = {'Param1': 'Value1', 'Param2': 'Value2'}
        >>> report.add_param_value_table(   pv_data, 
                                            title         = 'My Param Value Table', 
                                            use_big_table = False, )        
        '''
        
        if use_big_table == True:
            self.elements_list.append(get_param_value_table_element_v2(pv_data, title))
        else:
            self.elements_list.append(get_param_value_table_element(pv_data, 
                                                                    title, 
                                                                    Reports_Settings.param_value_table_truncate_length))
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_param_value_table_big(  self, 
                                    pv_data:       dict[str, str] | list[(str, str)], 
                                    title:         str  = '', 
                                    use_big_table: bool = True, 
                                            ) -> None:
        '''
        Add param value table with big style to the report.
        
        Parameters:
        ----------
        pv_data       ('dict[str, str] | list[(str, str)]') : dictionary of param name and value.
        title         ('str')                               : title of the table.
            - (Default: '')
        use_big_table ('bool')                              : if True, then use big table style.
            - (Default: `True`)
        
        Example:
        --------
        >>> pv_data: dict = {'Param1': 'Value1', 'Param2': 'Value2'}
        >>> report.add_param_value_table_big(   pv_data,
                                                title         = 'My Param Value Table', 
                                                use_big_table = True, )
        '''
        
        self.add_param_value_table( pv_data, 
                                    title, 
                                    use_big_table)
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_code(   self, 
                    func, 
                    title: str = None, 
                        ) -> None:
        '''
        Add code to the report.
        
        Parameters:
        ----------
        func  ('function'): function to add code to the report.
        title ('str')     : title of the block.
            - Default: `None`
        
        Example:
        --------
        >>> def my_func():
        ...     print('Hello World!')
        >>> report.add_code(my_func, title = 'My Code Block')        
        '''
        
        import inspect        
        
        f_name = func.__name__
        f_code = inspect.getsource(func)
        
        if title is not None:
            self.add_title(title)            
            pass
        
        self.elements_list.append(get_code_element(f_code))
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_alert_box(  self, 
                        text:       str, 
                        alert_type: str = 'i', 
                        emoji:      str = '', 
                            ) -> None:
        '''
        Add Alert Box to the report.
        
        Parameters:
        ----------
        text       ('str'): text to display in the alert box.
        alert_type ('str'): type of the alert box. (Optional)
            - 'i' - info
            - 'w' - warning
            - 'n' - note
            - 'e' - error
            - (Default: 'i')
        emoji      ('str'): emoji to display in the alert box. (Optional)
            - if None, then no emoji will be displayed according alert type.
            - (Default: '' - no emoji))
        
        Example:
        --------
        >>> report.add_alert_box(   text       = 'My Alert Box Text',
                                    alert_type = 'i',
                                    emoji      = '', )
        '''
        
        self.elements_list.append(get_alert_box_element(text, 
                                                        alert_type, 
                                                        emoji))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_showhide_region_open(   self, 
                                    title:        str, 
                                    title_suffix: str = '', 
                                    region_name:  str = None, 
                                        ) -> None:
        '''
        Add show hide region open to the report.
        
        ⚠️ WARNING: At the end of the region, you must add show hide region close.
        
        Parameters:
        ----------
        title        ('str'): title of the region.
        title_suffix ('str'): title sufix for the region. (Optional)
            - Final title will be: title_suffix + title
            - (Default: '')
        region_name  ('str'): name of the region. (Optional)
            - if None, then region name will be generated automatically.
            - (Default: None)
        
        Example:
        --------
        >>> report.add_showhide_region_open(    title        = 'My Show Hide Region',
                                                title_suffix = '',
                                                region_name  = None)
        >>> report.add_text('My Text')
        >>> report.add_showhide_region_close()
        '''
        
        if region_name is None:
            region_name = self._get_show_hide_region_id()
        
        title_upd: str = title_suffix + title
        
        self.elements_list.append(get_showhide_region_open_element(title_upd, region_name))
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def add_showhide_region_close(self) -> None:
        '''
        Add show hide region close to the report.
        '''
        self.elements_list.append(get_showhide_region_close_element())
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def move_element_to_bottom(self) -> None:
        '''
        Moving last added element to the bottom of the report.
        
        Example:
        --------
        >>> report.add_text('My Text')
        >>> report.move_element_to_bottom()
        '''
        if len(self.elements_list) > 0:
            self.bottom_elements_list.append(self.elements_list.pop())
            pass
        
        pass    
    
    # --------------------------------------------------------------------------------------------
    #                                         PRIVATE METHODS:
    # --------------------------------------------------------------------------------------------
    
    def _adding_bottom_elements_to_report(self) -> None:
        '''
        Adding bottom elements to the report.
        '''
        while len(self.bottom_elements_list) > 0:
            self.elements_list.append(self.bottom_elements_list.pop(0))
            pass

        pass
    
    # --------------------------------------------------------------------------------------------
    
    def _add_element(self, element: ReportElement) -> None:
        '''
        Add the given element to the report.
        
        Parameters:
        ----------
        element ('ReportElement'): element to add to the report.
        '''
        
        self.elements_list.append(element)
        
        pass
    
    # --------------------------------------------------------------------------------------------
    
    def _update_filename(self, filename_old: str) -> str:
        '''
        Returns the new filename, with added number at the end.
        or if the filename already contains a number at the end, then increment it by 1.
        
        Parameters:
        ----------
        filename_old (str): old filename.
        
        Returns:
        -------
        filename_new (str): new filename.
        
        Example:
        --------
        >>> filename_old: str = 'my_report'
        >>> filename_new: str = self._update_filename(filename_old)
        '''
        # Check if filename_old contain '(NNNN)' at the end:
        #   and if contains, then get the number value inside the brackets:
        #   and increment it by 1.
        #   and then add the new number to the filename_old.
        #   and then return the new filename.
        
        # Regular expression to match the pattern (NNNN) at the end of the filename
        pattern = r"\(\d{4}\)$"

        # Search for the pattern in the old filename
        match = re.search(pattern, filename_old)

        if match:
            # Extract the number, increment it, and format it to 4 digits
            number:       int = int(match.group()[1:-1]) + 1
            new_number:   str = f"({number:04d})"            
            # Replace the old number with the new incremented number
            filename_new: str = re.sub(pattern, new_number, filename_old)
        else:
            # Append (0001) if the pattern is not found
            filename_new: str = f"{filename_old}_(0001)"

        return filename_new
    
    # --------------------------------------------------------------------------------------------
    
    def _check_folder_path(self) -> None:
        # if folder einished without  '\\', then add it.
        
        if self.folder_path[-1] != '\\':
            self.folder_path += '\\'        
        pass
    
    # --------------------------------------------------------------------------------------------    
    
    def _get_html_str(self) -> str:
        '''
        Returns the html string for the report.
        '''
        
        # adding bottom elements to the report:
        self._adding_bottom_elements_to_report()
        
        # Adding final element:
        self.elements_list.append(get_footer_element())        
        
        favicon_base64: str = _get_base64_favicon()
        
        res: str = '<!DOCTYPE html> \n'
        res     += '<html lang="en"> \n'
        res     += '<head> \n'
        res     += '<meta charset="UTF-8"> \n'
        res     += f'<link rel="icon" type="image/png" href="{favicon_base64}"/>'
        res     += f'''<title>
                    {self.title}                
                    </title> \n'''
                
        # Code Highlighting:
        res     += '''<link rel="stylesheet"
                    href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/vs.min.css">
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js"></script>
                    <script>hljs.highlightAll();</script>'''
                
        res     += '<style> \n'
        
        for element in self.elements_list:
            res += element.get_style_str()
            pass
        
        res     += '</style> \n'        
        res     += '</head> \n'
        res     += '<body> \n'
        
        for element in self.elements_list:
            res += element.get_body_str()
            pass        

        res     += '''<script>
                    function toggleContent(regionId, btn, regionName) {
                        var content = document.getElementById(regionId);
                        if (content.style.display === "none" || content.style.display === "") {
                            content.style.display = "block";
                            btn.innerHTML = '▼ Hide ' + regionName;
                        } else {
                            content.style.display = "none";
                            btn.innerHTML = '▶ Show ' + regionName;
                        }
                    }         
                </script>'''
        
        res     += '</body> \n'
        res     += '</html> \n'
        
        return res
    
    # --------------------------------------------------------------------------------------------    
    
    def _sanitize_filename(self, filename: str) -> str:
        '''
        Sanitize the given filename.
        
        Parameters:
        ----------
        filename (str): filename to sanitize.
        
        Returns:
        -------
        sanitized (str): sanitized filename.
        
        Example:
        --------
        >>> filename:  str = 'my_report.htm'
        >>> sanitized: str = self._sanitize_filename(filename)
        '''
        
        # Define the acceptable character pattern (letters, digits, underscore, hyphen, and space)
        pattern  = r'[^\w\s-]'
        
        sanitized = re.sub(pattern, '_', filename)      # Replace unacceptable characters with an underscore        
        sanitized = sanitized.strip()                   # Remove leading and trailing spaces        
        sanitized = re.sub(r'[\s_-]+', '_', sanitized)  # Replace multiple consecutive spaces or underscores with a single one

        if not sanitized:                               # If the filename is empty, use a default filename
            sanitized = "default_filename"

        return sanitized
    
    # --------------------------------------------------------------------------------------------
    
    def _get_current_date_time(self) -> str:
        '''
        Returns the current date and time and milliseconds as `str`.
        '''
        res_date_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]        
        return res_date_time

# --------------------------------------------------------------------------------------------
#                                  TESTING: 
# --------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    print('Testing: report.py')    
    
    report = ReportHTML()
    print(report)
    
    report.title = 'Test Report'
    report.folder_path = 'reports_4_test\\'
    report.report_file_name = 'tst report'

    element_header_title = get_header_title('Test Report', 'Sub Title')
    element_style = get_style_element()
    
    console_text = '''
    report.add_element(element_style)
    report.add_element(element_header_title)

    report.save_to_file()

    print('File saved to: ', report._file_path)
    print('filename: ', report._file_name)
    '''
    
    param_value_dict            = {}
    param_value_dict['name']    = 'name_value_with a long name to test truncation of the string.'
    param_value_dict['age']     = 21
    param_value_dict['number']  = 12.85
    param_value_dict['bool']    = True
    param_value_dict['list']    = [1, 2, 3]
    param_value_dict['tuple']   = (1, 2, 3)
    param_value_dict['dict']    = {'a': 1, 'b': 2}
    
    elememnt_console_text   = get_text_console_element(console_text)
    element_horizontal_line = get_horizontal_line_element()
    element_title           = get_title_element('Test Title')
    element_text            = get_text_element(console_text)
    element_space           = get_space_element()
    
    element_param_value_table = get_param_value_table_element(param_value_dict, 'Test Param Value Table')
    
    # Create a simple plot
    # Set Plot Size:
    plt.figure(figsize = (11.7, 6), dpi = 100)    
    plt.plot([1, 2, 3, 4])
    plt.ylabel('Some numbers')
    
    element_chart = get_chart_element(plt)
    
    arr  = np.linspace(0, 10, 100)
    varr = np.sin(arr)
    
    # Set Plot Size:
    plt.figure(figsize = (11.7, 6), dpi = 100)
    
    plt.plot(arr, varr)
    plt.title('sin(x)')
    plt.ylabel('sin(x)')
    plt.xlabel('x')
    
    element_chart_2 = get_chart_element(plt)
    
    # ---------------------
    
    df = pd.DataFrame(np.random.randn(90, 4), columns = list('ABCD'))
    highlight_columns = ['C', 'E']
    element_table = get_table_dataframe_element(df, highlight_columns)
    
    
    df2 = pd.DataFrame(np.random.randn(90, 10), columns = list('ABCDEFGHIJ'))
    
    df3 = pd.DataFrame(np.random.randn(10, 20), columns = list('ABCDEFGHIJKLMNOPQRST'))
    report.add_title('MY Report Title')
    
    report.add_showhide_region_open('Test Show Hide Region')
    report.add_code(get_text_console_element)
    report.add_chart(plt, use_fullwidth = True)
    report.add_showhide_region_close()
    
    report.add_title('My Alert Boxes:', use_center = False)
    report.add_alert_box('Test Alert Box', 'i')
    report.add_alert_box('Test Alert Box next', 'i', None)
    
    report.add_alert_box('Test Alert Box', 'e', '')
    
    report.add_param_value_table(param_value_dict)
    report.add_param_value_table_big(param_value_dict)
    report.add_showhide_region_open('Data Frames:')
    report.add_dataframe_table(df3, highlight_columns = highlight_columns)
    report.add_dataframe_table(df, highlight_columns = highlight_columns)
    report.add_showhide_region_close()
    
    report.add_chart(plt)
    report.add_dataframe_table(df2, highlight_columns = highlight_columns, round = 2)
    
    report.save_to_file()
    
    print('File saved to: ', report._file_path)
    print('filename: ', report._file_name)
    
    pass