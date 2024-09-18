# ============================================================================================

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "report favicon"
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: --------------------------------------------------------------

# v0.0.2 @ 2024-08-13 : Initial Release

# ============================================================================================

def _get_base64_favicon() -> str:
    '''
    Returns the base64 favicon string.
    '''    
    favicon: str = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAB3RJTUUH6AgNFTYD/iEBBwAABQ5JREFUWIXFl0toXFUYx3/ncc/Mnds8m04yiZr6qPioiNiFVKkuFFxUQQRdmEU3WSgIIgquVFy0VMSFokvdFEEKFkttUawPUAu2KcYWWtNSm8bm1aQmmXszk/s6LiaPsc1Mp0Xb/+5evv93/vd/vvN958INhrj0hTHmkZ6unnyYhMl/upAQQinF8PDwH8CJ1QTIvr6+j/r7+/tbW9tUHMcAZLMZpJRYC0JAHCeE4cJq2hFCkM1mEEIsx0dRTBSFCCHQWjMwMDC7Y8eO/qGhod0AuoqfeXjz5qe2bNmibFX60fOj+LMzSKWwaUK+u5v29rZVv9IC54bPUfJ9lJTY1NLb20tzc9NyzIY772rZs2fPE6sJQEkVAARBCaU0wdwMb777PrpnA8bRTE9NcZMI2P72m5TDGGvtMtcYw7mzZ9n58Qd0378RKSTn/xphQ66Z1195FX++hGMMvu/jOE55ifcvATZdSSgEROECXkee2x5/Cg1cmByndGgfaZIselQdLwhLJTrX9/LQM09j44T2U0MEh45e5lOapstPmjoQQoC1xKUAhCApl5BCIITAy5nVCNgkYcEPIEmJSmWklPWWqC9gVVFSkiQJP3zzLcW5WZRWhGHE3XffQ8YYxOW1+d8K0FozPj3Nwc928WRXAaEko2Nj7D12jOe2bau49n8KAIiThFsLXTx630awMNrWymQUk1bV0P8qQAhBnKbYhZAEKIURV+39IupXyHXADRdQdwustSAkjuuhAJ11iW3lHCshEMagAc9xsGFImqZIpch4HiQJjpsltPXroqYAIQQmmyWYnuTkDwcwWjM9PUWvjFjjeQxf/JsvB39HasXExATJ7XfgeR7jwyMc/uoACsHIyAi3ZbzVxkZ9AUIIyuUyUhte3taHP/M3UimStJd8oYdcxuXZF19iNgiQUuKlCbcUumlqaqL/+RcoBT5SStLu9fT03sLMbLFmQ6opoDg3h+8XaWtvp71jLdjF6o9jxsbHWNexlvy6jiUGcRwxMTFOvqsTQedyniiKGBsbJZ/P47puYwKstbg5F+1oxCX+OY7BdXOXcYxj4PL8lfhcDq01dlFUQw6EYUhpvoSU13a+q5FaS8ZU7hVRFMHKLKrtgJQS5WjkNTaYaihAac3MxWmmpy4g9Uo91DgFAilkZfJdYZrVxWLdpGnK1IVJFsrlxewrH1VjCyCOIxbK5YYFrNwO7Mrii9zA94njCNd1EWkDNWCtxWSyCCmvcroJrE0RCHKeR5zETE6Oo7Qk57XgOE6liSm1nLRmEc7PBxSLc6gGHUjTlGzWpavQjeM4DB4/xskTJ0htihSC1FqM1uSMYWZ2xrmiA563hkwm07AD1oKSEmMcBgYH2b99J5s6u5GVSxXGcdBK8dFP35/5eejkp1d2IAgo+kWkaswBm1pMxrB2bRuTUxe4t6WdrQ88COUyZLMkccR7B7/+9ZejR/r8KDp1RQfcXK7SiBp2wKJUJZ1WihhgoQxaMzw1yTvf7Pv8k+8OvgRcrObVngWlEr5fu4dfikqzMazraAdACmBNE0eGTvLWgb079x898sZqvGoBQirhAmjHoatQQMpCQ4svYWnyGsdhTS7HwWO/Lbz2xe7Xfztz6sNanGoB4ZGBgaOPnT59c1NzK0u/ZlcLN2uI5kvsGjg8OnD2z/5T58/trxd/6Qa3bNq0aWuhs7MjipJr+jnVWosgKKrvf/zxW+D4teS4rvgHgQT+ow5vHeEAAAAASUVORK5CYII='
    
    return favicon

# ============================================================================================