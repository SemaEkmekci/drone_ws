from playsound import playsound

import subprocess
import threading

class StartManager:

    def __init__(self, start_functions):
        print(start_functions)
        self.start_instruction_arr = start_functions
        self.main()

    def start(self, start_instruction):
        subprocess.run(start_instruction, shell=True)
        
       
    def main(self):
        print(self.start_instruction_arr)
    
        for instruction in self.start_instruction_arr:
            playsound('ses.mp3')
            t = threading.Thread(target=self.start, args=(instruction,))
            t.start()
        
