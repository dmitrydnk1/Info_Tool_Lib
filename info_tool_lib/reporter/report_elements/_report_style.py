# ============================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Report Style CSS'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# ============================================================================================

REPORT_STYLE: str = '''
        .grid_2,
        .grid_5,
        .grid_3,
        .grid_10,
        .grid_6,
        .grid_8,
        .grid_4{
            display: inline;
            float: left;
            position: relative;
            margin-left: 15px;
            margin-right: 15px;
        }
        
        .omega{margin-right: 0;}  
        .alpha{margin-left: 0;}
        
        .grid_12{
            margin: 0 auto;
            width: 1170px;}

        .grid_10{width: 970px;}
        .grid_6{width: 570px;}
        .grid_8{width: 770px;}
        .grid_4{width: 370px;}
        .grid_3{width: 270px;}
        .grid_5{width: 470px;}
        .grid_2{width: 170px;}
        .right{float: right;}
        
        img, 
        a{
            outline: none; border:0;}
        
        table {
            border-collapse: collapse; 
            border-spacing: 0; 
            width: 100%; }
        

        img{vertical-align: top;}
        
        .red{color: #ed1c25;}
        
        p{
            margin: 0;
            padding: 0 0 18px;
        }
        
        .row{
            width: 100%;
            overflow: hidden;
        }
        
        body{
            margin:0;
            font:14px/18px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            color:#333;
            background:#fff;
            width: 100%;
            min-width: 1170px;
        }
        
        #header{
            width: 100%;
            overflow: hidden;
            /* border-bottom: 1px solid #012135; /* Dark blue border */
            padding: 24px 0 24px;
            margin: 0 0 40px;
        }
        
        
        #header .title{
            margin: 18px 0 0 0;
            font: 34px/36px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            color: #111;  /* #DDD; */ 
        }
        
        #header .subtitle{
            font: 24px/26px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            display: block;
            padding: 0 0 10px;
            margin: 27px 0 0 0;
            color: #111 /* #DDD; */ 
        }
        
        #header a{margin: 0 0 0 30px; }
        
        #header .st{margin-top: 11px;}
        
        .content{
            width: 100%;
            overflow: hidden;
        }
        
        .content h1{
            font: bold 44px/48px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            display: block;
            padding: 0 0 10px;
            margin: 27px 20px 0 0;
            color: #111;        
        }
        
        .content h2{
            font: bold 30px/36px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            display: block;
            padding: 0 0 10px;
            margin: 27px 20px 0 0;
            color: #111;        
        }
        
        .content h3{
            font: bold 20px/24px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            display: block;
            padding: 0 0 10px;
            margin: 27px 20px 0 0;
            color: #111;        
        }
        
        

        h2 .info{
            float: right;
            font:14px/19px Arial, Helvetica, sans-serif;
            margin: 11px 0 0 0;
        }
        
        h2 .info img{margin: 0 10px 0 0;}
        
        /* Graph */
        
        
        .graph-item,
        .graph {
            width: 100%;
            overflow: hidden;
            margin: auto; /* Center the container */
            padding: 0;
            background-color: white; /* White background */
            border: none; /* Flat border */
            border-radius: 6px; /* Smoothed radius */
            transition: box-shadow 0.3s; /* Smooth transition for shadow */
        }
        
        .graph:hover {
            box-shadow: 2px 6px 10px rgba(0, 0, 0, 0.1); /* Shadow on hover */
        }

        
        .graph-info{
            padding: 0 0 0 70px;
            overflow: hidden;
        }
        
        .top-margin{margin: 21px 0 0 0;}
        
        .right-graph-info{padding: 0;}
        
        .graph-group h3,
        .graph h3{
            font:bold 20px/22px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            margin: 0;
            padding: 0 0 17px;
        }
        
        .last-graph{padding: 20px 0 17px;}
        
        .last.graph{padding: 0;}
        
        .graph-group span,
        .graph span{
            font:16px/18px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            color: #606a70;
            margin: 0 0 7px 0;
            float: left;
            min-width: 121px;
        }
        
        .graph-group span img,
        .graph span img{
            margin: 0 5px 0 0;
            vertical-align: middle;
        }
        .right-graph-info span{font-size:14px; margin: 0 0 7px;}
        
        /* df table */
        .minimalistic-style-table {
            /* width: calc(100% - 20px); /* Reduces the total width to allow for 10px spacing on each side */
            width: 98%; /* Reduces the total width to allow for 10px spacing on each side */
            margin: auto; /* Centers the table horizontally */
            box-sizing: border-box;
            border-collapse: collapse;
            font-family: Arial, sans-serif;
            color: #333;
            font-size: 0.9em;
            background-color: #fff;
            box-shadow: 0 2px 3px rgba(0,0,0,0.1);
            margin: 25px 0;        
        }
        .minimalistic-style-table th, .minimalistic-style-table td {
            text-align: left;
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
            /* position: sticky;
            top: 0; /* Adjusts the top position to make it stick at the top of the table container */
            /* background-color: #f0f0f0; /* Ensure background is opaque */
            z-index: 2; /* Ensures the header is above other content */
        }
        
        .minimalistic-style-table th {
            background-color: #f0f0f0; /* Light grey background for header */
            color: #333;
        }
        .minimalistic-style-table td.index-column {
            background-color: #f2f2f2; /* Slightly different background for index column for distinction */
        }
        .minimalistic-style-table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .minimalistic-style-table tr:hover {
            background-color: #f1f1f1;        
        }
        
        .table-scroll-wrapper {
            /* max-height: 1000px; /* or whatever value suits your layout */
            /* overflow-y: auto; /* */
        }

        @media print{
            #header{margin: 0 0 20px; padding: 0 0 24px;}
            .row{
                page-break-inside: avoid;
            }
            
            .graph{
                page-break-inside: avoid;
            }
            
            .graph-group{page-break-before: always;}
        }
        
        img{max-width:100%;}

        @media print and (orientation:portrait) { 
            .grid_12{width: 92%; padding: 0; margin: 0;}
            .grid_10{width: 940px;}
            .grid_6{width: 520px;}
            .grid_8{width: 700px;}
            .grid_4{width: 340px;}
            .grid_3{width: 230px;}
            .grid_5{width: 430px;}
            .grid_2{width: 130px;}
                    
        }
        @media print and (orientation:landscape){
            
            table{
                margin: 0 0 10px;
            }
            
            table span{
                font:bold 18px/20px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            }
            
            .content h2{
                font: bold 20px/22px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
                margin: 14px 0 0 0;
            }
        }
        
        /* Code Part */
        pre {
            padding: 1em;
            margin: 0.5em 0;
            overflow: auto;            
            border-radius: 6px; /* Slightly more rounded edges for a softer look */
            border: none; /* Remove border for a flat, minimalistic design */
            background-color: #ffffff; 
        }
        
        pre:hover {
            box-shadow: 2px 6px 10px rgba(0, 0, 0, 0.1); /* Shadow on hover */
        }
        
        /* Show Hide Button */
                
        .section {
            margin-bottom: 20px;            
        }
        .toggle-button {
            background-color: #f2f2f2; /* Light grey background for a clean, minimalistic look */
            color: #333333; /* Dark grey text for a subtle, sophisticated contrast */
            border: none; /* Remove border for a flat, minimalistic design */
            border-radius: 6px; /* Slightly more rounded edges for a softer look */
            padding: 12px 24px; /* Slightly larger padding for a better tactile feel */
            cursor: pointer;
            font-size: 16px; /* Maintain readable font size */
            transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effects */
            margin: 10px auto; /* Uniform margin for vertical spacing and horizontal centering */
            display: block; /* Maintain block level for easy centering */
            width: 80%; /* Button width reduced to 80% */
            max-width: 1170px; /* Maximum width of 1170px */
            font-weight: bold; /* Bold font for a modern look */
            text-align: center; /* Center align text */
            box-shadow: 0 1px 4px rgba(0,0,0,0.1); /* Subtle box shadow for depth */
        }

        .toggle-button:hover {
            background-color: #e6e6e6; /* Slightly darker grey on hover for interactive feedback */
            color: #1a1a1a; /* Darken text color on hover for contrast */
        }

        /* Simplified Content Area Style */
        .content_show_hide {
            display: none;
            padding: 20px;
            border: none; /* Remove border for a cleaner look */
            border-radius: 6px; /* Consistent rounded corners for a cohesive design */
            margin: 10px 0; /* Simplified margin for top and bottom spacing */
            background-color: #fafafa; /* Very light grey for a clean background */
            box-shadow: 0 2px 6px rgba(0,0,0,0.05); /* More pronounced shadow for a floating effect */
        }
        
        /* Alert Box */
        /* Base style for all alert boxes, minimalistic design */
        .alert-box {
            background-color: #f7f7f7; /* Very light grey background */
            border-radius: 5px; /* Smooth rounded corners */
            padding: 15px 20px; /* Generous padding for a spacious layout */
            font-size: 15px; /* Slightly larger font size for readability */
            color: #1d1d1f; /*  typical dark grey text color */
            box-shadow: 0 4px 8px rgba(0,0,0,0.05); /* Soft shadow for depth */
            display: flex; /* Flexbox for layout */
            align-items: center; /* Vertically center elements */
            gap: 12px; /* Space between elements */
            font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif; /* Modern, system-based font */
            margin: 15px 0; /* Margin for spacing between boxes */
            transition: background-color 0.3s, box-shadow 0.3s; /* Transition for hover effect */
        }

        /* Hover effect */
        .alert-box:hover {
            background-color: #ffffff; /* Lighten background color on hover */
            box-shadow: 0 6px 12px rgba(0,0,0,0.1); /* Increase shadow for depth on hover */
        }

        /* Styles for specific alert types with subtle color accents */
        .info-box { border-left: 8px solid #007aff; } /*  blue for information */
        .warning-box { border-left: 8px solid #ff9500; } /*  orange for warning */
        .note-box { border-left: 8px solid #34c759; } /*  green for notes */
        .error-box { border-left: 8px solid #ff3b30; } /*  red for errors */

        /* Style for emojis inside alert boxes */
        .alert-box .emoji {
            font-size: 22px; /* Slightly larger emoji for emphasis */
            vertical-align: middle; /* Ensure vertical alignment with text */
        }

        /* Style for text inside alert boxes */
        .alert-box .text {
            /* Keep minimalistic, no additional styling required */
        }
        
        
        /* Param val Style Table */
        
        .param-val-style-table {
            /*width: 100%;*/
            /*max-width: 600px;*/
            border-collapse: collapse; /* For no borders: border-collapse: separate; */
            border-spacing: 0;
            border-radius: 3px;
            margin: 25px auto;            
            font-size: 1.1em;
            min-width: 400px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            
        }

        .param-val-style-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }

        .param-val-style-table th:first-child,
        .param-val-style-table td:first-child {
            width: 30%; /* Narrower for the parameter column */
        }

        .param-val-style-table th,
        .param-val-style-table td {
            padding: 12px 15px;
            text-align: left;
            font-size: 1.0em;
        }

        .param-val-style-table th {
            background-color: #009879;
            color: #F5F5F5; /* White for contrast */
            font-weight: normal;
        }

        .param-val-style-table tbody tr {
            border-bottom: 1px solid #e0e0e0;
        }

        .param-val-style-table tbody tr:last-child {
            border-bottom: none;
        }

        .param-val-style-table tbody tr:nth-of-type(even) {
            background-color: #f4f4f4;
        }

        .param-val-style-table tbody tr:hover {
            background-color: #d5f4e6; /* Soft green on hover */
        }

        .param-val-style-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }

        .param-val-style-table tbody td {
            font-size: 1.0em;
        }
        
        /*   Param Value Grid: */
        
        /* Style for param-value elements */
        
        .param-value-element {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start; /* Align items to the left */
            /* justify-content: space-around; */ 
            margin-bottom: 20px;
            font: 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
        }

        .param-value-caption {
            /*font-size: 0.9em;*/
            color: #111;
            text-align: left;
            width: 100%; /* Ensure the caption spans the full width */
            font: 17px/24px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif
        }

        .param-value-text {
            /*font-size: 1.8em;*/
            color: #444;
            text-align: left;
            font: 40px / 44px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif;
            /*font-weight: bold; */
        }
        
        .param-value-text-long {
            font: 24px / 28px 'Segoe UI', 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif; /* Smaller font size for longer text */
        }

        .param-value-item {
            margin: 10px;
            flex-basis: calc(25% - 20px);
            text-align: left;
        }
        
        '''.replace("  ", "").replace("\n", "").replace("\t", "").replace("    ", "")


# -----------------------------------------------------------------------------------------------------------
#
#                            Testing:
#
# -----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    print(REPORT_STYLE)
    
    pass

# -----------------------------------------------------------------------------------------------------------