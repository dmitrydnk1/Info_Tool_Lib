'''

Chatbot for Discord, to send status messages to a channel.

Send Status Updates and Information to a Chat Bot.

For Now Support Only one Channel.

---

HOW TO USE:
-----------

- ### Basic Usage:    
```python
# Create a Chat Bot Object, and send a message:
chat_bot: Chat_Bot = Chat_Bot()
chat_bot.send('Hello World!')
```

- ### Initialisation:    
```python
# Can be initiated once, in any of the python code, 
#   and default values will be used in all futher calls and projects.    
# Set the Default Channel Link:
Chat_Bot.cfg_set_channel_link_default('https://mylink/1234567890')
```

- ### Silent Mode ON/OFF:    
```python        
chat_Bot.cfg_silent_mode_OFF   # Turn off Silent Mode
chat_Bot.cfg_silent_mode_ON    # Turn on Silent Mode
```

- ### Finally:    
```python        
chat_bot.close()  # Closing Channel After Use
```

'''

# --------------------------------------------------------------------------------------------

_name_:           str = 'Info Tool Lib - Chatbot'
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --- VERSION HISTORY: -----------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------

from .chat_upd import Chat_Bot

# --------------------------------------------------------------------------------------------