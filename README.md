# Info Tool Lib

A Collections of handy tools to view and process daily-routines information, while working with Python, Jupyter to make life easier.

## Contains sub-modules for:

1. Jupyter Notebooks Class extension, for view class variables. (CLS_INFO)
    Made for simple view, of class informations updates, while working in Jupyter enviroment.
2. Reporter, for generating and saving custom HTML-Reports, to log, and view complex informations.
3. Progress bar
4. Some functions for Plotting, including view of variaius Color-Maps.
5. Chat-Bot, for sending custom updated by chatbot.

# (👉ﾟヮﾟ)👉 For BEST Experience, use with VS_CODE

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dmitrydnk1/Info_Tool_Lib.git
    ```
2. Navigate to the project directory:
    ```bash
    cd repository
    ```
3. Install with required dependencies:
    ```bash
    pip install .
    ```

## Usage Example

Kindly refer to Examples sub-folder, with Jupyter Notebooks, for demonstration of base functionality.

## Class Eextension Example:
    
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
![Class extension view, from Eaxmples](Examples\_example_CLS_INFO_01.png)

## Reporter Initialization Example:
    
```python
from info_tool_lib import Reports_Settings

# Use one of options, with absolute, or relative path.
REPORTS_ABS_PATH: str = 'C:\\#CODE\\My_Reports\\'
REPORTS_PATH:     str = 'my_reports\\'

# !!! Initialize default path once, in any of the python code, 
#       and it willl be used in all other modules, where it is imported.
Reports_Settings.set_deafult_report_path(REPORTS_ABS_PATH)
```

## Reporter Example:

- ### Reporter Example - Section A:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing Report Class.
from info_tool_lib import ReportHTML

# Creating Report Object. ( It will be filled with data in later steps. )
report: ReportHTML = ReportHTML()

# --------------------------------------------------------------------------------
#
#                   SECTION A: Adding Basic Elemetns:
#
# --------------------------------------------------------------------------------

report.add_title('Title Section A - Basic Elements')

# --- ADD LONG TEXT: ------------------------------------------------------------

my_long_text: str = '''
This is a long text that will be displayed in the report.
With multiple lines and paragraphs.
    Some indentation.
    Some absolute not needed indentation.

Final paragraph with joke, I jsut googled to paste here:
    Why did the scarecrow win an award?
    Because he was outstanding in his field.
'''

report.add_text(my_long_text)

# --- ADD ALERT BOX: ------------------------------------------------------------

report.add_alert_box('Add various elemnts to the reports', alert_type = 'i', emoji = '👍')

# --- ADD PARAMETERS TABLE, as a dictionary: ------------------------------------

contained_elements: dict = {'Param F': 15,
                            'Param Z': 25,
                            'Param Y': 35.6,
                            'Param X': 'Undefined',}


report.add_param_value_table(contained_elements)

# --- ADDING SUB-TITLE: ---------------------------------------------------------

report.add_title('Title Subsection - Parameters with more values:', h_level = 2, use_center = True)

# --- ADD PARAMETERS TABLE with many records, as a dictionary: -------------------

contained_elements_large: dict = {  'Param F': 15,
                                    'Param Z': 25,
                                    'Param Y': 35.6,
                                    'Param X': 'Undefined',
                                    'Param A': 15,
                                    'Param B': 25,
                                    'Param C': 35.6,
                                    'Param D': 'Undefined',
                                    'Param E': 15,
                                    'Param G': 25,
                                    'Param H': 35.6, }

report.add_param_value_table_big(contained_elements_large)
```
![Resulted Section A](Examples\_example_report_section_A.png)


- ### Reporter Example - Section B:
```python
# --------------------------------------------------------------------------------
#
#    SECTION B: Adding DataFrames, Function Source-Code, Hide/Show Region: 
#
# --------------------------------------------------------------------------------

report.add_title('Title Section B - Functions Code & DataFrames')

# --- PREPARE CUSTOM FUNCTION: ----
# it can be any function, in that or previous cells.

def prepare_df() -> pd.DataFrame:
    
    data = {
        'name':     ['John', 'Anna', 'Peter', 'Linda'],
        'location': ['New York', 'Paris', 'Berlin', 'London'],
        'age':      [24, 13, 53, 33]
    }

    df = pd.DataFrame(data, columns = ['name', 'location', 'age'])
    
    return df

# --- ADD SHOW/HIDE REGION: -----------------------------------------------------

report.add_showhide_region_open('Function Code for DataFrame Preparation')

# --- ADD FUNCTION SOURCE CODE, just by passing function name: -------------------

report.add_code(prepare_df)

# --- CLOSE SHOW/HIDE REGION: ---------------------------------------------------

report.add_showhide_region_close()

# Prepare DataFrame, with function, from above.

df: pd.DataFrame = prepare_df()

# --- ADD DATAFRAME TABLE: ------------------------------------------------------

report.add_dataframe_table(df, highlight_columns = ['age']) 
```
![Resulted Section B](Examples\_example_report_section_B.png)

- ### Reporter Example - Section C:
```python
# --------------------------------------------------------------------------------
#
#                   SECTION C: Adding Charts
#
# --------------------------------------------------------------------------------

report.add_title('Title Section C - Charts')

# Making custom Chart with Matplotlib.

fig: plt.Figure = plt.figure(figsize = (13, 6), dpi = 100, tight_layout = True)

ax: plt.Axes = fig.add_subplot(111)

chart_line_x:  np.ndarray[float] = np.linspace(0, 10, 1000, dtype = float)
chart_line_y1: np.ndarray[float] = np.sin(chart_line_x)
chart_line_y2: np.ndarray[float] = np.cos(chart_line_x * 4)
chart_line_y3: np.ndarray[float] = chart_line_y1 + chart_line_y2

ax.plot(        chart_line_x, chart_line_y1, color = '#570', linestyle = '-', linewidth = 0.5, alpha = 0.8)
ax.fill_between(chart_line_x, chart_line_y1, color = '#570', alpha = 0.1, label = 'sin(x)')

ax.plot(        chart_line_x, chart_line_y2, color = '#057', linestyle = '--', linewidth = 0.5, alpha = 0.8)
ax.fill_between(chart_line_x, chart_line_y2, color = '#057', alpha = 0.1, label = 'cos(4*x)')

ax.plot(        chart_line_x, chart_line_y3, color = '#333', linestyle = ':', linewidth = 0.5, alpha = 0.8)
ax.fill_between(chart_line_x, chart_line_y3, color = '#333', alpha = 0.1, label = 'sin(x) + cos(4*x)')

ax.set_title('Sinus and Cosinus Functions')
ax.set_xlabel('x - axis')
ax.set_ylabel('y - axis')

ax.legend()

# Using another function from info_tool_lib, for updating plot style. (Optional)
from info_tool_lib import plt_ax
plt_ax.flat_style(ax)

# --- ADD PLOT TO REPORT: -------------------------------------------------------
# Just pass the figure object, and it will be added to the report.
report.add_plot(fig)

# (Optional) Clear the figure, to free memory.
fig.clear()
```
![Resulted Section C](Examples\_example_report_section_C.png)

- ### Reporter Example - Section D:
```python
# --------------------------------------------------------------------------------
#
#                   SECTION D: Adding Large DataFrames
#
# --------------------------------------------------------------------------------

report.add_title('Title Section D - Large DataFrame')

# - Prepare Larger DataFrame:
rows_amount: int = 30

large_df: pd.DataFrame = pd.DataFrame(np.random.randn(rows_amount, 4), columns = list('ABCD'))
large_df['E'] = pd.date_range('20210101', periods = rows_amount)

# adding more Columns to the DataFrame
for i in range(10):
    large_df[f'X{i}'] = np.random.randn(rows_amount)

# --- ADD DATAFRAME TABLE, with heatmap highlights for custom column: ---
report.add_dataframe_table(large_df, highlight_columns = ['A', 'B', 'D'], color_map_name = 'coolwarm', round = 2)

# --------------------------------------------------------------------------------
#
#                   SAVING REPORT.
#
# --------------------------------------------------------------------------------

report.save()
```
![Resulted Section D](Examples\_example_report_section_D.png)

---

### GENERATED EXAMPLE REPORT, located at `Examples\example_html_by_reporter.html`

## Reporter result html file, from a code above:
Examples\example_html_by_reporter.html
[View the webpage](Examples\example_html_by_reporter.html)


---

## Progress Bar Example:

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

pb.end()
```

## Progress Bar for Jupyter Notebook:

```python
import numpy as np
import time

steps: int = 100

pb = ProgressBar.make_for_jupyter(steps)

for i in range(steps):        
    pb.step(f'current step: {i}')        
    wait_period: float = 0.03 + np.random.rand() * 0.03        
    time.sleep(wait_period)
    pass
```
![Progress-Bar in VS-Code](Examples\_example_ProgressBar_01.png)
