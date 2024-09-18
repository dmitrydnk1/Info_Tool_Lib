import numba
from . import cls_repr_html


# ======================================================================================================================

__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'CLS Info - Numba Repr'
VERSION:          str = f'{_name_:>20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -------------------------------------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# --- TODO : -----------------------------------------------------------------------------------------------------------

# - TODO: Add Help and more documentation.

# ======================================================================================================================
#
#              Functions for Viewing Extension for NUMBA Classes, compatible with Jupyter Notebook.
#
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
#                   Parameters Storage:
# ----------------------------------------------------------------------------------------------------------------------

param_val_list: numba.typed.List = numba.typed.List([('name', 'val', 'type')])
param_val_list_signature         = numba.typeof(numba.typed.List([('name', 'val', 'type')]))


_get_param_val_list_signature = param_val_list_signature()

@numba.njit(_get_param_val_list_signature, 
            cache = True, )
def repr_numba_get_param_val_list() -> numba.typed.List:
    res = numba.typed.List([('name', 'val', 'type')])    
    return res

# ----------------------------------------------------------------------------------------------------------------------
#                     Function for Detail / Compact Parameter:
# ----------------------------------------------------------------------------------------------------------------------

@numba.njit(numba.types.unicode_type(numba.types.unicode_type, numba.types.unicode_type), 
            cache = True, )
def repr_numba_detail_compact_param_str(simple_veiw: str, detail_view: str) -> str:    
    res: str = '<details><summary>' + simple_veiw + '</summary><p>' + detail_view + '</p></details>'
    return res


# ----------------------------------------------------------------------------------------------------------------------
#                     Function for string conversion:
# ----------------------------------------------------------------------------------------------------------------------

@numba.njit(numba.types.unicode_type(numba.float64, numba.int64), 
            cache = True, )
def repr_numba_float64_to_str(  val:    float, 
                                digits: int, 
                                    ) -> str:
        
    part_b: int = int((val - int(val)) * 10**digits)
    if part_b < 0:        
        res = '-' + str(int(val)) + '.' + str(-part_b)
        return res
    
    res = str(int(val)) + '.' + str(part_b)
    return res

# ----------------------------------------------------------------------------------------------------------------------
@numba.njit(numba.types.unicode_type(numba.float32, numba.int32), 
            cache = True, )
def repr_numba_float32_to_str(  val:    float, 
                                digits: int, 
                                    ) -> str:
        
    part_b: int = int((val - int(val)) * 10**digits)
    if part_b < 0:        
        res = '-' + str(int(val)) + '.' + str(-part_b)
        return res
    
    res = str(int(val)) + '.' + str(part_b)
    return res


# ----------------------------------------------------------------------------------------------------------------------
#             Function for Adding Parameters and Values to the List : Array(int64, 1, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.int64, 1, 'C', False, aligned = True)

_add_param_val_array_int64_signature = param_val_list_signature(param_val_list_signature, 
                                                                numba.types.unicode_type, 
                                                                _arr_int_temp_sig)

@numba.njit(_add_param_val_array_int64_signature, 
            cache = True, )
def repr_numba_add_param_val_array_int64(   param_val_lst, 
                                            name: str, 
                                            val, 
                                                ) -> numba.typed.List:    
    
    type_str = "Array(int64, 1, 'C', False, aligned = True)"
    
    size: int = len(val)
    val_str: str = ''
    if size > 3:
        val_str: str = '[ ... , ' + str(val[size-2]) + ', ' + str(val[size-1]) + ' ]'        
        val_str += ' ( Size: ' + str(size) + ' )'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 0:
        val_str = '[]'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 1:
        val_str = '[' + str(val[0]) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 2:
        val_str = '[' + str(val[0]) + ', ' + str(val[1]) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    return param_val_lst        

# ----------------------------------------------------------------------------------------------------------------------
#             Function for Adding Parameters and Values to the List : Array(int32, 1, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.int32, 1, 'C', False, aligned = True)

_add_param_val_array_int32_signature = param_val_list_signature(param_val_list_signature, 
                                                                numba.types.unicode_type, 
                                                                _arr_int_temp_sig)

@numba.njit(_add_param_val_array_int32_signature, 
            cache = True, )
def repr_numba_add_param_val_array_int32(   param_val_lst, 
                                            name: str, 
                                            val, 
                                                ) -> numba.typed.List:    
    
    type_str = "Array(int32, 1, 'C', False, aligned = True)"
    
    size: int = len(val)
    val_str: str = ''
    if size > 3:
        val_str: str = '[ ... , ' + str(val[size-2]) + ', ' + str(val[size-1]) + ' ]'        
        val_str += ' ( Size: ' + str(size) + ' )'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 0:
        val_str = '[]'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 1:
        val_str = '[' + str(val[0]) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 2:
        val_str = '[' + str(val[0]) + ', ' + str(val[1]) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    return param_val_lst        


# ----------------------------------------------------------------------------------------------------------------------
#         Function for Adding Parameters and Values to the List : Array(float64, 1, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.float64, 1, 'C', False, aligned = True)

_add_param_val_array_float64_signature = param_val_list_signature(  param_val_list_signature, 
                                                                    numba.types.unicode_type, 
                                                                    _arr_int_temp_sig)

@numba.njit(_add_param_val_array_float64_signature, 
            cache = True, )
def repr_numba_add_param_val_array_float64( param_val_lst, 
                                            name: str, 
                                            val, 
                                                ) -> numba.typed.List:    
    
    type_str = "Array(float64, 1, 'C', False, aligned = True)"
    
    size: int = len(val)
    val_str: str = ''
    if size > 3:
        val_str: str = '[ ... , ' + repr_numba_float64_to_str(val[size-2], 4) + ', ' + repr_numba_float64_to_str(val[size-1], 4) + ' ]'        
        val_str += ' ( Size: ' + str(size) + ' )'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 0:
        val_str = '[]'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 1:
        val_str = '[' + repr_numba_float64_to_str(val[0], 4) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 2:
        val_str = '[' + repr_numba_float64_to_str(val[0], 4) + ', ' + repr_numba_float64_to_str(val[1], 4) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    return param_val_lst        

# ----------------------------------------------------------------------------------------------------------------------
#         Function for Adding Parameters and Values to the List : Array(float32, 1, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.float32, 1, 'C', False, aligned = True)

_add_param_val_array_float32_signature = param_val_list_signature(  param_val_list_signature, 
                                                                    numba.types.unicode_type, 
                                                                    _arr_int_temp_sig)

@numba.njit(_add_param_val_array_float32_signature, 
            cache = True, )
def repr_numba_add_param_val_array_float32( param_val_lst, 
                                            name: str, 
                                            val, 
                                                ) -> numba.typed.List:    
    
    type_str = "Array(float32, 1, 'C', False, aligned = True)"
    
    size: int = len(val)
    val_str: str = ''
    if size > 3:
        val_str: str = '[ ... , ' + repr_numba_float64_to_str(val[size-2], 4) + ', ' + repr_numba_float64_to_str(val[size-1], 4) + ' ]'        
        val_str += ' ( Size: ' + str(size) + ' )'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 0:
        val_str = '[]'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 1:
        val_str = '[' + repr_numba_float64_to_str(val[0], 4) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    if size == 2:
        val_str = '[' + repr_numba_float64_to_str(val[0], 4) + ', ' + repr_numba_float64_to_str(val[1], 4) + ']'
        param_val_lst.append((name, val_str, type_str))
        return param_val_lst
    
    return param_val_lst        

# ----------------------------------------------------------------------------------------------------------------------
#         Function for Adding Parameters and Values to the List : Array(float64, 2, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.float64, 2, 'C', False, aligned = True)

_add_param_val_array_float64_2d_signature = param_val_list_signature(   param_val_list_signature, 
                                                                        numba.types.unicode_type, 
                                                                        _arr_int_temp_sig)

@numba.njit(_add_param_val_array_float64_2d_signature, 
            cache = True, )
def repr_numba_add_param_val_array_float64_2d(  param_val_lst, 
                                                name: str, 
                                                val, 
                                                    ) -> numba.typed.List:    
    
    type_str = "Array(float64, 2, 'C', False, aligned = True)"
    
    size_B: int = 0
    
    size_A: int = len(val)
    if size_A > 0:
        size_B: int = len(val[0])
    
    
    if size_A > 2 and size_B > 5:
        val_str: str = '[ ... ,'
        val_str += ' [ ... ,' + repr_numba_float64_to_str(val[-2][-1], 4) + ' ] ,'
        val_str += ' [ ... ,' + repr_numba_float64_to_str(val[-1][-1], 4) + ' ] '
        val_str += '] '
        pass
        
    val_str += '( Size: ' + str(size_A) + ' x ' + str(size_B) + ' )'
        
    param_val_lst.append((name, val_str, type_str))
    return param_val_lst
        
# ----------------------------------------------------------------------------------------------------------------------
#         Function for Adding Parameters and Values to the List : Array(float32, 2, 'C', False, aligned = True)
# ----------------------------------------------------------------------------------------------------------------------

_arr_int_temp_sig = numba.types.Array(numba.float32, 2, 'C', False, aligned = True)

_add_param_val_array_float32_2d_signature = param_val_list_signature(   param_val_list_signature, 
                                                                        numba.types.unicode_type, 
                                                                        _arr_int_temp_sig)

@numba.njit(_add_param_val_array_float32_2d_signature, 
            cache = True, )
def repr_numba_add_param_val_array_float32_2d(  param_val_lst, 
                                                name: str, 
                                                val, 
                                                    ) -> numba.typed.List:    
    
    type_str = "Array(float32, 2, 'C', False, aligned = True)"
    
    size_B: int = 0
    
    size_A: int = len(val)
    if size_A > 0:
        size_B: int = len(val[0])
    
    
    if size_A > 2 and size_B > 5:
        val_str: str = '[ ... ,'
        val_str += ' [ ... ,' + repr_numba_float64_to_str(val[-2][-1], 4) + ' ] ,'
        val_str += ' [ ... ,' + repr_numba_float64_to_str(val[-1][-1], 4) + ' ] '
        val_str += '] '
        pass
        
    val_str += '( Size: ' + str(size_A) + ' x ' + str(size_B) + ' )'
        
    param_val_lst.append((name, val_str, type_str))
    return param_val_lst

# ----------------------------------------------------------------------------------------------------------------------
#                     Main Function for Viewing Extension for NUMBA Classes
# ----------------------------------------------------------------------------------------------------------------------


_get_repr_numba_signature = numba.types.unicode_type(   numba.types.unicode_type, 
                                                        param_val_list_signature, 
                                                        numba.int32, 
                                                        numba.types.unicode_type, )

@numba.njit(_get_repr_numba_signature, 
            cache = True, )
def repr_numba_get_repr_str(obj_name:      str, 
                            param_val_lst: numba.typed.List, 
                            styleID:       int, 
                            version:       str,
                                ) -> str:
    
    res: str = ''
    
    # --- Main Container: ---
    res += '<div class="container_PARAM_VAL"' + cls_repr_html.CONTAINER_A_STYLE + '>'
    
    # --- Title: ---
    res += '<div class="title_main"' + cls_repr_html.TITLE_MAIN_STYLE + '>' + obj_name 
    
    if version == '':
        # No Version:
        res += '</div>'
    else:
        res += '<span ' + cls_repr_html.TITLE_MAIN_VERSION_SPAN_STYLE_A + '>' + version + '</span></div>'
    
    
    # --- Devide Line: ---
    if styleID < 100:
        # - Single Line:
        res += '<div ' + cls_repr_html.DEVIDE_LINE_STYLE + '></div>'
        pass
    else:     
        # - Devider Line v2:    
        res += '<div ' + cls_repr_html.DEVIDE_LINE_STYLE_B_LIGHTPART + '></div>'
        res += '<div ' + cls_repr_html.DEVIDE_LINE_STYLE_B_DARKPART  + '></div>'
        
    
    # --- Param Val Table: ---
    if len(param_val_lst) <= 1:
        # Check if the Table should be shown:
        # --- Close Main Container: ---
        res += '<div style="height: 1px;"></p>'
        res += '</div>'
        return res
    
    res += '<table ' + cls_repr_html.PARAM_VAL_TABLE_STYLE + '>'
    res += '<tr '    + cls_repr_html.PARAM_VAL_TABLE_STYLE_TR + '>'
    res += '<th '    + cls_repr_html.PARAM_VAL_TH_STYLE_PARAM + '></th>'
    res += '<th '    + cls_repr_html.PARAM_VAL_TH_STYLE_VALUE + '></th></tr>'
    
    for i in range(1, len(param_val_lst)):
        res += '<tr '  + cls_repr_html.PARAM_VAL_TABLE_STYLE_TR + '>'
        res += '<td>'
        res += '<pre ' + cls_repr_html.PARAM_VAL_PRE_STYLE_TYPE + '>'  + param_val_lst[i][2] + '</pre>'
        res += '<pre ' + cls_repr_html.PARAM_VAL_PRE_STYLE_PARAM + '>' + param_val_lst[i][0] + '</pre>'
        res += '</td>'
        res += '<td>'
        res += '<pre ' + cls_repr_html.PARAM_VAL_PRE_STYLE_VALUE + '>: ' + param_val_lst[i][1] + '</pre>'
        res += '</td></tr>'
        pass
        
    res += '</table>'
    
    # --- Close Main Container: ---
    res += '<div style="height: 1px;"></p>'
    res += '</div>'
    
    return res
    
# ----------------------------------------------------------------------------------------------------------------------