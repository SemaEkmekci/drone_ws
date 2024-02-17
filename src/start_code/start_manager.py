from playsound import playsound

import subprocess
import threading

class StartManager:

    def __init__(self, start_functions):
        print(start_functions)
        self.start_instruction_arr = start_functions
        self.main()

    def start(self, start_instruction):
        #subprocess.run(start_instruction, shell=True)
        #subprocess.Popen(start_instruction, shell=True)
        #subprocess.Popen(f"gnome-terminal -- {start_instruction}", shell=True)
        #subprocess.Popen(["gnome-terminal", "-e", start_instruction])
        #subprocess.Popen(['gnome-terminal' '-e', 'bash', '-c', terminal_commands['gnome-terminal']])
        terminal_commands = {
            'gnome-terminal': start_instruction,
            # Buraya farklı terminal ve komutları ekleyebilirsiniz
        }
        subprocess.Popen(['gnome-terminal', '-e', 'bash', '-c', terminal_commands['gnome-terminal']])
    def main(self):
        print(self.start_instruction_arr)
    
        for instruction in self.start_instruction_arr:
            playsound('ses.mp3')
            t = threading.Thread(target=self.start, args=(instruction,))
            t.start()
        
