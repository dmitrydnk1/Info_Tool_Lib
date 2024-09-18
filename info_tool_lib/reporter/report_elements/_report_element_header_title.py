import random

from ._report_element import ReportElement, ReportElementTypes

# ============================================================================================

__version__:      str = '0.0.6'
__version_date__: str = '2024-08-21'
_name_:           str = 'Report Element - header title'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.6 @ 2024-08-21 : Updated header background images to random dynamic generated background.

# --- TODO : ---------------------------------------------------------------------------------

# --- CONSTANTS: -----------------------------------------------------------------------------


# ============================================================================================

def get_header_title(   title:                str, 
                        subtitle:             str  = '', 
                        use_background_image: bool = True, 
                            ) -> ReportElement:
    
    if not use_background_image:
        return _get_header_title_simple(title, subtitle)
    
    res: ReportElement = ReportElement()
    
    res.type = ReportElementTypes.HEAD_TITLE_ON_BACKGROUND
    
    # Generate random colors and positions
    color1:       str = _generate_random_color()
    color2:       str = _generate_random_color()
    color3:       str = _generate_random_color()
    color4:       str = _generate_random_color()
    
    shape_a_size: int = _generate_random_size()
    shape_b_size: int = _generate_random_size()
    shape_c_size: int = _generate_random_size()

    shape_a_top:  int = _generate_random_position()
    shape_a_left: int = _generate_random_position()
    shape_b_top:  int = _generate_random_position()
    shape_b_left: int = _generate_random_position()
    shape_c_top:  int = _generate_random_position()
    shape_c_left: int = _generate_random_position()
    
    # Abstract background styles with randomness    
    style_abstract_background: str = f'''
    .parallax {{
        position: relative;
        height: 250px;
        background: linear-gradient(135deg, {color1}, {color2}), 
                    linear-gradient(45deg, {color3}, {color4});
        background-blend-mode: screen;
        background-size: 400% 400%;
        animation: gradientAnimation 60s ease infinite;
        overflow: hidden;
    }}

    @keyframes gradientAnimation {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}

    .shape_A, .shape_B, .shape_C {{
        position: absolute;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        animation: floatShape 20s ease-in-out infinite;
    }}

    .shape_A {{
        width: {shape_a_size}px;
        height: {shape_a_size}px;
        top: {shape_a_top}%;
        left: {shape_a_left}%;
        animation-duration: 30s;
        animation-delay: -5s;
    }}

    .shape_B {{
        width: {shape_b_size}px;
        height: {shape_b_size}px;
        top: {shape_b_top}%;
        left: {shape_b_left}%;
        animation-duration: 40s;
        animation-delay: -10s;
    }}

    .shape_C {{
        width: {shape_c_size}px;
        height: {shape_c_size}px;
        top: {shape_c_top}%;
        left: {shape_c_left}%;
        animation-duration: 35s;
        animation-delay: -15s;
    }}

    @keyframes floatShape {{
        0% {{
            transform: translateY(0) translateX(0) scale(1);
        }}
        25% {{
            transform: translateY(-20px) translateX(20px) scale(1.1);
        }}
        50% {{
            transform: translateY(20px) translateX(-20px) scale(1.05);
        }}
        75% {{
            transform: translateY(-10px) translateX(10px) scale(1);
        }}
        100% {{
            transform: translateY(0) translateX(0) scale(1);
        }}
    }}
    '''
    
    # Header content styles
    style_header_content: str = '''
    .parallax-content {
        z-index: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100%;
        padding: 20px;
        box-sizing: border-box;
    }

    .title {
        font-size: 2.5em;
        color: #222222;        
        font-family: 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
        margin: 0;
    }

    .subtitle {
        font-size: 1.5em;
        color: #222222;        
        font-family: 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
        margin: 0;
    }
    '''
    
    # Combine styles into res.style_content
    res.style_content = style_abstract_background + style_header_content
    
    # --------------- BODY ---------------
    
    res.body_content = f'''
    <div class="parallax">        
            <div id="header">
                <div class="grid_12 parallax-content alpha">
                    <div class="grid_8 alpha">
                        <h1 class="title">{title}</h1>
                        {'<h2 class="subtitle">' + subtitle + '</h2>' if subtitle else ''}
                    </div>
                </div>
            </div>            
        <div class="shape_A"></div>
        <div class="shape_B"></div>
        <div class="shape_C"></div>
    </div>
    '''
    
    res.body_content += '''
        <div class="content">
        '''
    
    return res

# --------------------------------------------------------------------------------------------
#
#                SUPPORTING FUNCTIONS:
#
# --------------------------------------------------------------------------------------------

def _generate_random_color() -> str:
    return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'

# --------------------------------------------------------------------------------------------

def _generate_random_size(  min_size: int = 50, 
                            max_size: int = 200, 
                                ) -> int:
    
    return random.randint(min_size, max_size)

# --------------------------------------------------------------------------------------------

def _generate_random_position() -> int:
    return random.randint(0, 90)

# --------------------------------------------------------------------------------------------

def _get_header_title_simple(   title:    str, 
                                subtitle: str = '', 
                                    ) -> ReportElement:
    
    res: ReportElement = ReportElement()
    res.type           = ReportElementTypes.HEAD_TITLE_ON_BACKGROUND
    
    # --- BODY -----------------------------------------
    
    res.body_content = f'''
        <div id=\"header\">
            <div class=\"grid_12\">
                <div class=\"grid_8 alpha\">
                <h1 class=\"title\">{title}</h1>
                </a>
                {'<h2 class="subtitle">' + subtitle + '</h2>' if subtitle else ''}
                </a>
                </div>
            </div>
        </div>
        '''
    
    # --- CONTENT PREPARATION ----------------------------
    
    res.body_content += f'''
        <div class=\"content\">
        '''
    
    return res

# --------------------------------------------------------------------------------------------