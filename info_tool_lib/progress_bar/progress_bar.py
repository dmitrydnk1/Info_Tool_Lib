import time
from collections     import deque
from IPython.display import display, HTML, clear_output

# -------------------------------------------------------------------------------------------
#
#                       PROGRESS BAR
#
# -------------------------------------------------------------------------------------------

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'InfoToolLib - Progress Bar'
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: ----------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# -------------------------------------------------------------------------------------------

# --- TODO : --------------------------------------------------------------------------------

# -

# --- CONSTANTS & CFG: ----------------------------------------------------------------------

UPDATE_STEP_SCALER: int = 1000   

# -------------------------------------------------------------------------------------------
#
#                    Progress Bar Object:
#
# -------------------------------------------------------------------------------------------

class ProgressBar():
    '''
    
    Progress Bar Object.
    
    ---
    
    EXAMPLES:
    ---------
    
    - ### Basic Example:    
    ```python
    from info_tool_lib import ProgressBar
    
    # Create a Progress Bar:
    pb: ProgressBar = ProgressBar(100)
    for i in range(100):
        pb.update(i)
    pb.finish()
    ```
    
    - ### Example for Jupyter Notebook:
    ```python
    import numpy as np
    import time

    steps: int = 100

    pb = ProgressBar(steps)

    for i in range(steps):        
        pb.step(f'current step: {i}')        
        wait_period: float = 0.03 + np.random.rand() * 0.03        
        time.sleep(wait_period)        
        pass

    # pb.end() # (OPTIONAL) This is not required for Jupyter Notebook.
    ```
    
    - ### Example of custom use of progress messages:
    ```python
    import numpy as np
    import time
    from info_tool_lib import ProgressBar

    steps: int = 100

    pb = ProgressBar(100)

    for i in range(100):
        wait_period: float = 0.03 + np.random.rand() * 0.03
        time.sleep(wait_period)
        pb.update(i)
        
        # Get the progress status string to use for other purposes
        #   e.g. for logging or updating by chat bot message.
        progress_status_str: str = pb.get_status_str()
        print(progress_status_str, end='\r')
        pass
    ```
    
    - ### Example with Custom Settings:    
    ```python
    from info_tool_lib import ProgressBar
    
    # Progress Bar with Custom Settings:
    pb: ProgressBar = ProgressBar(  target_score          = 100,
                                    start_score           = 0,
                                    update_frequency_pcnt = 1.0,
                                    bar_length            = 30,
                                    text_message_default  = 'Processing...',
                                    jupyter_mode          = False, )
    
    for i in range(100):
        pb.update(i)
    pb.finish()
    ```
    
    '''
    
    # ---------------------------------------------------------------------------------------------------
    # 
    #          Factory Methods, for Jupyter version.
    #          make_for_jupyter(..) and jupyter(..) are the same.
    #
    # ---------------------------------------------------------------------------------------------------
    
    @classmethod
    def make_for_jupyter(   cls, 
                            target_score:             int, 
                            start_score:              int   = 0, 
                            update_frequency_pcnt:    float = 1.0, 
                            bar_length:               int   = 30,
                            text_message_default:     str   = '',
                                ) -> 'ProgressBar':
        '''
        Factory Method to create a ProgressBar Object for Jupyter Notebook.
        same as jupyter(..)
        
        
        Parameters:
        -----------
        target_score:          (`int`)   : Target Score.
        start_score:           (`int`)   : Start Score.
            - Default: `0`
        update_frequency_pcnt: (`float`) : Update Frequency Percentage.
            - Default: `1.0`
        bar_length:            (`int`)   : Bar Length.
            - Default: `30`
        text_message_default:  (`str`)   : Default Text Message.
            - Default: `''`
        
        Returns:
        --------
        (`ProgressBar`) : ProgressBar Object.
        
        Example:
        --------
        >>> pb: ProgressBar = ProgressBar.make_for_jupyter( target_score          = 100,
                                                            start_score           = 0,
                                                            update_frequency_pcnt = 1.0,
                                                            bar_length            = 30,
                                                            text_message_default  = 'Processing...', )
        >>> for i in range(100):
                pb.update(i)
            pb.finish()
        '''
    
        res: 'ProgressBar' = cls.jupyter(   target_score             = target_score,
                                            start_score              = start_score,
                                            update_frequency_pcnt    = update_frequency_pcnt,
                                            bar_length               = bar_length,
                                            text_message_default     = text_message_default,
                                            jupyter_mode_always_true = True, )        
        return res
    
    # ---------------------------------------------------------------------------------------------------
    
    @classmethod
    def jupyter(cls,
                target_score:             int, 
                start_score:              int   = 0, 
                update_frequency_pcnt:    float = 1.0, 
                bar_length:               int   = 30,
                text_message_default:     str   = '',
                jupyter_mode_always_true: bool  = True,
                    ) -> 'ProgressBar':
        '''
        Factory Method to create a ProgressBar Object for Jupyter Notebook.
        same as make_for_jupyter(..)
        '''
        
        res: 'ProgressBar' = cls(   target_score            = target_score,
                                    start_score             = start_score,
                                    update_frequency_pcnt   = update_frequency_pcnt,
                                    bar_length              = bar_length,
                                    text_message_default    = text_message_default,
                                    jupyter_mode            = True, )        
        return res

    # ---------------------------------------------------------------------------------------------------
    
    def __init__(self, 
                    target_score:          int, 
                    start_score:           int   = 0, 
                    update_frequency_pcnt: float = 1.0, 
                    bar_length:            int   = 30,
                    text_message_default:  str   = '',
                    jupyter_mode:          bool  = False,
                            ) -> None:
        '''
        Progress Bar Object.
        
        Parameters:
        -----------
        target_score:          (`int`)   : Target Score.
        start_score:           (`int`)   : Start Score.
            - Default: `0`
        update_frequency_pcnt: (`float`) : Update Frequency Percentage.
            - Default: `1.0`
        bar_length:            (`int`)   : Bar Length.
            - Default: `30`
        text_message_default:  (`str`)   : Default Text Message.
            - Default: `''`
        jupyter_mode:          (`bool`)  : Jupyter Mode.
            - Default: `False`
        
        Example:
        --------
        >>> pb: ProgressBar = ProgressBar(  target_score          = 100,
                                            start_score           = 0,
                                            update_frequency_pcnt = 1.0,
                                            bar_length            = 30,
                                            text_message_default  = 'Processing...',
                                            jupyter_mode          = False, )
        >>> for i in range(100):
                pb.update(i)
            pb.finish()
        
        '''

        # --- Settings: ---
        self.bar_length:              int   = bar_length
        self.update_frequency_pcnt:   float = update_frequency_pcnt
        self.PROGRESS_CONSOLE_SYMBOL: str   = '█'
        self.jupyter_mode:            bool  = jupyter_mode
        
        # --- Progress: ---
        self._current_score: int | float = start_score
        self._start_score:   int | float = start_score
        self._target_score:  int | float = target_score        
        self._score_size:    int | float = self._target_score - self._start_score
        
        if self._score_size == 0:
            self._score_size = 1
                
        # --- Private: ---
        self._start_time = time.time()
        self._end_time   = time.time()
        
        self._update_step: int = self._get_update_step()
        
        _history_lenght: int = 10
        
        if self._score_size > 200:
            _history_lenght = int(self._score_size / 20)    
        
        self._progress_history = deque(maxlen = _history_lenght)  # Stores tuples of (timestamp, progress)

        self.text_message          = text_message_default
        self._text_message_default = text_message_default
        
        self._print_start()
        
        pass
        
    # -------------------------------------------------------------------------------------------------------------------
    
    def update(self,                 
                new_score:     int | float = None,
                text:          str         = None,
                progress_step: int | float = 1,
                        ) -> None:
        '''
        Update the Progress Bar.
        
        Parameters:
        -----------
        new_score:     (`int` or `float`) : New Score.
            - Default: `None`
        text:          (`str`)            : Text Message.
            - Default: `None`
        progress_step: (`int` or `float`) : Progress Step.
            - Default: `1`
        '''
        
        if type(new_score) == str:
            text      = new_score
            new_score = None
        
        if new_score is not None:
            self._current_score  = new_score
        else:
            self._current_score += progress_step

        # Add current progress and time to history
        current_time: float = time.time()
        self._progress_history.append((current_time, self._current_score))
        
        # ========= JUPYTER MODE: =============
        
        if self.jupyter_mode == True:
            if text is not None:
                self.text_message = text            
            else:
                self.text_message = self._text_message_default
            
            clear_output(wait = True)
            display(self)
            
            return
        
        current_step_int: int = int(self._current_score * 1000)
        
        if current_step_int % self._update_step == 0:
            if text is None:
                text_message: str = self.text_message
            else:
                text_message: str = text

            self._print_progress(text_message = text_message)
        
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def step(   self, 
                new_score:     int | float = None,
                text:          str         = None,
                progress_step: int | float = 1,             
                        ) -> None:
        '''
        Update the Progress Bar.
        
        Parameters:
        -----------
        new_score:     (`int` or `float`) : New Score.
            - Default: `None`
        text:          (`str`)            : Text Message.
            - Default: `None`
        progress_step: (`int` or `float`) : Progress Step.
            - Default: `1`
        '''
        
        self.update(new_score = new_score, progress_step = progress_step, text = text)        
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def next(   self, 
                new_score:     int | float = None,
                text:          str         = None,
                progress_step: int | float = 1,             
                        ) -> None:
        ''' 
        Update the Progress Bar.
        
        Parameters:
        -----------
        new_score:     (`int` or `float`) : New Score.
            - Default: `None`
        text:          (`str`)            : Text Message.
            - Default: `None`
        progress_step: (`int` or `float`) : Progress Step.
            - Default: `1`            
        '''
        
        self.update(new_score = new_score, progress_step = progress_step, text = text)        
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def end(self, 
            text:       str = None, 
            title_done: str = 'DONE', 
                ) -> None:  
        '''
        Complete the Progress Bar.
        
        Parameters:
        -----------
        text:       (`str`) : Text Message.
            - Default: `None`
        title_done: (`str`) : Title for Done.
            - Default: `'DONE'`
        '''
        
        if text is None:
            text_message: str = self.text_message
        else:
            text_message: str = text
        
        # ========= JUPYTER MODE: =============
        if self.jupyter_mode == True:
            self._finish_html_(text_message = text_message, title_done = title_done)
            return

        self._print_progress(text_message = text_message)                
        self._print_final(text = text, title_done = title_done)        
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def finish( self, 
                text:       str = None, 
                title_done: str = 'DONE', 
                    ) -> None:
        '''
        Complete the Progress Bar.
        
        Parameters:
        -----------
        text:       (`str`) : Text Message.
            - Default: `None`
        title_done: (`str`) : Title for Done.
            - Default: `'DONE'`
        '''
        
        self.end(text = text, title_done = title_done)
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def get_ETA_str(self) -> str:
        
        res: str = self._format_time(self._calculate_eta())
        return res
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def get_status_str(self) -> str:
        '''
        Returns the Status String for use by other functions.
        
        Returns:
        --------
        (`str`) : Status String.
        
        Example:
        --------
        >>> status_str: str = pb.get_status_str()
        >>> print(status_str)
            'Elapsed Time: 00:00:00:000 | ETA: 00:00:00:000 | Progress: 0.00%'
        ''' 
        
        elapsed_time:        float = time.time() - self._start_time
        eta:                 float = self._calculate_eta()
        progress_percentage: float = self._get_progress() * 100
        
        res: str = f'Elapsed Time: {self._format_time(elapsed_time)} | ETA: {self._format_time(eta)} | Progress: {progress_percentage:.2f}%'
        
        return res
    
    # -------------------------------------------------------------------------------------------------------------------
    #
    #                   Private Methods
    #
    # -------------------------------------------------------------------------------------------------------------------
    
    def _print_start(self) -> None: 
        
        if self.jupyter_mode == True:            
            return
        
        self._print_progress(text_message = self.text_message )
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def _print_final(   self, 
                        text:       str = '', 
                        title_done: str = 'DONE', 
                            ) -> None:
        
        if text is None:
            text = ''
        
        self._end_time  = time.time()
        end_time: float = self._end_time - self._start_time
        
        print(f'\n{title_done} in {round(end_time, 3)}s. {text}')
        
        pass
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def _get_update_step(self) -> int:
        
        res: float = float(self._score_size) * (self.update_frequency_pcnt / 100.0)        
        res: int   = int(res * UPDATE_STEP_SCALER)
        
        if res == 0:
            res = UPDATE_STEP_SCALER
        
        return res
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def _get_progress(self) -> float:
        
        res: float = float(self._current_score - self._start_score) / float(self._score_size)        
        res        = min(max(res, 0.0), 1.0)        
        return res
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def _calculate_eta(self) -> float:
        
        if len(self._progress_history) < 2:
            return 0  # Not enough data to calculate ETA

        # Calculate rates between each consecutive pair of updates
        rates: list[float] = []
        
        for i in range(1, len(self._progress_history)):
            
            time_diff:     float = self._progress_history[i][0] - self._progress_history[i-1][0]
            progress_diff: float = self._progress_history[i][1] - self._progress_history[i-1][1]
            
            if time_diff > 0:
                rates.append(progress_diff / time_diff)

        if not rates:
            return 0  # Avoid division by zero

        # Calculate moving average of rates & Estimate ETA based on average rate
        average_rate:       float = sum(rates) / len(rates)        
        remaining_progress: float = self._target_score - self._current_score
        eta_seconds:        float = remaining_progress / average_rate if average_rate > 0 else 0

        return eta_seconds
    
    # -----------------------------------------------------------------------------------------------------------------------
    
    def _format_time(self, seconds: float) -> str:
        
        if seconds == float('inf'):
            return "Calculating..."
        
        res: str = ''
        
        # Get Days:
        days: int = seconds // (24 * 3600)
        if days > 0:
            seconds = seconds % (24 * 3600)            
            res += f'{int(days)} Days '
            pass        
        
        res += time.strftime("%H : %M : %S:", time.gmtime(seconds))
        # Make with milliseconds
        res += f'{seconds:.3f}'.split('.')[1]
        
        return res
    
    # -----------------------------------------------------------------------------------------------------------------------
    
    def _print_progress(self, text_message: str) -> None:        
        
        percent: float = self._get_progress() 
        percent        = min(max(percent, 0.0000000001), 1.0)   # To avoid division by zero.
        
        arrow: str = self.PROGRESS_CONSOLE_SYMBOL * int(round(percent * self.bar_length)-1)
        if percent < 1.0:
            arrow += '>'
        else:
            arrow += self.PROGRESS_CONSOLE_SYMBOL
        
        spaces: str    = '-' * (self.bar_length - len(arrow))
        elapsed_time   = time.time() - self._start_time        
        estimated_time = self._calculate_eta()

        current_step_text: str = f'{self._current_score}/{self._target_score}'
        
        if type(self._current_score) == float:
            current_step_text = f'{round(self._current_score, 3)}/{round(self._target_score, 3)}'        
        elif type(self._current_score) == int:
            current_step_text = f'{self._current_score}/{self._target_score}'
        
        if percent < 1.0:            
            print(f'\rProgress: [{arrow + spaces}] {round(percent * 100, 2):.2f}% - {current_step_text}  \tElapsed Time: {round(elapsed_time, 3)}s  \tETA: {round(estimated_time, 3)}s \t  {text_message}    ', end = '\r')            
        else:            
            print(f'\rProgress: [{arrow + spaces}] {round(percent * 100  ):.1f}%  - {current_step_text}  \tElapsed Time: {round(elapsed_time, 3)}s  \tETA: {round(estimated_time, 3)}s \t   {text_message}   ', end = '\r')
        
        pass
    
    # -----------------------------------------------------------------------------------------------------------------------
    
    def _repr_html_(self) -> str:
        
        progress_percentage: float = self._get_progress() * 100
        elapsed_time:        float = time.time() - self._start_time
        eta:                 float = self._calculate_eta()
        
        intformation_str: str = ''
        
        if self.text_message is not None or self.text_message != '':
            intformation_str = f'<p style="line-height: 1.6; margin-bottom: 10px;"><strong></strong> {self.text_message}</p>'
            pass

        progress_bar_html: str = f'''
        <div style="color: white; margin-bottom: 5px; font-family: 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif; font-size: 14px; color:#C5C5C5">
            <p style="line-height: 1.6; margin-bottom: 10px;"><strong>STATUS:</strong> Current: {self._current_score} | Target: {self._target_score} | Elapsed Time: {self._format_time(elapsed_time)} | ETA: {self._format_time(eta)}</p>
            {intformation_str}
            <p style="line-height: 1.6; margin-bottom: 10px;"><strong>PROGRESS:</strong> {progress_percentage:.2f}%</p>
        </div>
        <div style="background-color: #333333; border-radius: 20px; padding: 2px; border: 1px solid #444444; box-shadow: 0 2px 4px rgba(0,0,0,0.5);">
            <div style="width: {progress_percentage}%; height: 20px; background: linear-gradient(90deg, rgba(10,132,255,1) 0%, rgba(59,153,252,1) 100%); border-radius: 18px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.2); transition: width 0.3s ease-in-out;">
            </div>
        </div>
        '''
        
        return progress_bar_html
    
    # -----------------------------------------------------------------------------------------------------------------------
    
    def _finish_html_(  self, 
                        text_message: str = None,   
                        title_done:   str = 'DONE', 
                            ) -> None:
        
        end_time:       float = time.time()
        elapsed_time:   float = end_time - self._start_time
        final_progress: float = self._get_progress() * 100
        
        additional_info: str = ''
        if text_message is not None:
            additional_info = f'<p style="line-height: 1.6; margin-bottom: 10px;"><strong>Info:</strong> {text_message}</p>'
            pass
        
        final_message_html: str = f'''
        <div style="
                font-family: 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
                color: #C5C5C5;
                background-color: #1c1c1e; 
                border-radius: 12px; 
                padding: 20px; 
                box-shadow: 0 4px 8px rgba(0,0,0,0.5); 
                margin-top: 10px;">
            <h2 style="text-align: center; color: #4EC9B0; font-weight: normal;">{title_done}</h2>
            <div style="border-top: 2px solid #313133; padding-top: 15px; margin-top: 15px;">
                <p style="line-height: 1.6; margin-bottom: 10px;"><strong>Start Time:</strong> {time.strftime('%H: %M: %S', time.localtime(self._start_time))}</p>
                <p style="line-height: 1.6; margin-bottom: 10px;"><strong>End Time:</strong> {time.strftime('%H: %M: %S', time.localtime(end_time))}</p>
                <p style="line-height: 1.6; margin-bottom: 10px;"><strong>Elapsed Time:</strong> {self._format_time(elapsed_time)}</p>
                <p style="line-height: 1.6; margin-bottom: 10px;"><strong>Total Progress:</strong> {final_progress:.2f}%</p>
                {additional_info}
            </div>
        </div>
        '''
        
        clear_output(wait=True)
        display(HTML(final_message_html))
        pass    
    
# ====================================================================================================================================

# ------------------------------------------------------------------------------------------------------------------------------------
#
#                TEST:
#
# ------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    print('Testing ProgressBar:')
    
    import numpy as np
    import time
    
    steps: int = 500    
    
    pb = ProgressBar(steps)
    
    for i in range(steps):        
        pb.step(f'current step: {i}')        
        wait_period: float = 0.03 + np.random.rand() * 0.03        
        time.sleep(wait_period)        
        pass
    
    pb.end()
    
    print(f'Done.')
    
    pass

# -----------------------------------------------------------------------------------------------------------------------------------