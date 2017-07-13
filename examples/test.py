import logging
import time
import os
from threading import Thread, Event
from respeaker import Microphone

# use madplay to play mp3 file     
os.system('madplay')               
     


def task(quit_event):                                                         
    mic = Microphone(quit_event=quit_event)                                   

    while not quit_event.is_set():
        if mic.wakeup('respeaker'):        
            print('Wake up')               
                          

def main():                                                              
    logging.basicConfig(level=logging.DEBUG)                                                           
    quit_event = Event()        
    thread = Thread(target=task, args=(quit_event,))
    thread.start()                          
    while True:                             
        try:                                
            time.sleep(1)                           
        except KeyboardInterrupt:                   
            print('Quit')                           
            quit_event.set()
            break        
    thread.join()                

if __name__ == '__main__':       
    main() 