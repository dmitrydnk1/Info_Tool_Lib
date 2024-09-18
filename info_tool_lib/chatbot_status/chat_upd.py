import keyring
import requests
import aiohttp
import asyncio
import threading


# --------------------------------------------------------------------------------------------------------

_name_:           str = 'InfoToolLib - chatbot_status'
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
VESRSION:         str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# --------------------------------------------------------------------------------------------------------

# version: 0.0.2 @ 2024-08-13 : Initial Release

# --------------------------------------------------------------------------------------------------------
#                             CONSTANTS:
# --------------------------------------------------------------------------------------------------------

_CHANNEL_A_NAME_ID:  str = 'chat_bot_channel_a'
_SERVICE_NAME:       str = 'chat_bot_TOOL'
_CHANNEL_A_USERNAME: str = 'InfoToolLib'

# --------------------------------------------------------------------------------------------------------
    
class Chat_Bot():
    '''
    Send Status Updates and Information to a Chat Bot.
    
    HOW TO (Example):
    -----------------
    
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
    
    # --------------------------------------------------------------------------------------------------
    
    @staticmethod
    def cfg_set_channel_link_default(link: str) -> None:
        '''
        Set the channel A link.
        '''
        keyring.set_password(_SERVICE_NAME, _CHANNEL_A_NAME_ID, link)        
        pass
    
    
    @staticmethod
    def cfg_clear_channel_link_default() -> None:
        '''
        Clear the channel A link.
        '''
        keyring.delete_password(_SERVICE_NAME, _CHANNEL_A_NAME_ID)
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def __init__(self):
                
        self._USE_SILENT_MODE: bool = True   # if True, no warnings or errors will be printed.
        self._channel_link:    str  = None                
        
        self._load_default_channel_a_link()
        
        # Start the asyncio event loop in a background thread
        self.loop   = asyncio.new_event_loop()
        self.thread = threading.Thread(target = self._start_loop, args = (self.loop,))
        self.thread.start()
    
        pass    
    
    # --------------------------------------------------------------------------------------------------
    
    def send(self, message: str) -> None:
        self.send_message(message)
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def message(self, message: str) -> None:
        self.send_message(message)
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def send_message(self, message: str, user: str = None)  -> None:        
        if not self.loop.is_running():  # Check if the loop is running
            if not self._USE_SILENT_MODE:
                print("Error: Event loop is not running.")
            return

        asyncio.run_coroutine_threadsafe(self._async_send(message, user), self.loop)
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def send_message_non_async(self, message: str, user: str = None) -> None:
        
        if self._channel_link is None:
            print('Error: No Channel Link Set!')
            return

        if user is None:
            user = _CHANNEL_A_USERNAME
        
        data = {'content':  message, 
                'username': user, }

        response = requests.post(self._channel_link, json = data)
        
        if not self._USE_SILENT_MODE:
            print(f'Message sent with response status: {response.status_code}')
        
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def close(self) -> None:
        # Properly close the event loop and the background thread
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()
        pass
        
    # --------------------------------------------------------------------------------------------------
    #                   PROPERTIES
    # --------------------------------------------------------------------------------------------------
    
    @property
    def silent_mode_OFF(self) -> None:
        self._cfg_silent_mode_off()
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    @property
    def silent_mode_ON(self) -> None:
        self._cfg_silent_mode_on()
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    @property
    def channel_link_enabled(self) -> bool:
        if self._channel_link == None:
            return False
        return True
    
    # --------------------------------------------------------------------------------------------------    
    
    @property
    def info_status(self) -> str:
        if self._USE_SILENT_MODE == False:
            return 'SILENT MODE: OFF'
        return 'SILENT MODE: ON'
        
    # --------------------------------------------------------------------------------------------------    
    #                    PRIVATE METHODS
    # --------------------------------------------------------------------------------------------------
    
    def _load_default_channel_a_link(self) -> None:
        '''
        Load the default channel A link.
        '''
        link: str = keyring.get_password(_SERVICE_NAME, _CHANNEL_A_NAME_ID)
        self._channel_link = link
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def _start_loop(self, loop) -> None:
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    # --------------------------------------------------------------------------------------------------

    async def _async_send(  self, 
                            message:  str, 
                            username: str = None, 
                                ) -> None:
        
        if self._channel_link is None:
            print('Error: No Channel Link Set!')
            return
        
        if username is None:
            username = _CHANNEL_A_USERNAME

        data = {'content':  message, 
                'username': username,}

        connector = aiohttp.TCPConnector(ssl = False)  # This disables SSL verification
        
        async with aiohttp.ClientSession(connector = connector) as session:
            try:
                async with session.post(self._channel_link, json = data) as response:
                    if response.status == 204:
                        if not self._USE_SILENT_MODE:
                            print("Message sent successfully!")
                    else:
                        # Reading the response body for more details on the error
                        response_text = await response.text()
                        if not self._USE_SILENT_MODE:
                            print(f'Failed to send message, status: {response.status}, response: {response_text}')
        
            except aiohttp.ClientError as e:
                if not self._USE_SILENT_MODE:
                    print(f"An error occurred: {e}")

        return
    
    # --------------------------------------------------------------------------------------------------
    
    def _cfg_silent_mode_on(self) -> None:        
        self._USE_SILENT_MODE = True
        pass
    
    # --------------------------------------------------------------------------------------------------
    
    def _cfg_silent_mode_off(self) -> None:        
        self._USE_SILENT_MODE = False
        pass
    
    # --------------------------------------------------------------------------------------------------