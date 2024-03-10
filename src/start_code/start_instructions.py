sh_file_path = "src/start_instructions_sh"

def start_gazebo():
        instruction = sh_file_path + "/start_gazebo.sh"
        return instruction


def start_ardupilot():
        instruction = sh_file_path + "/start_ardupilot.sh"
        return instruction
        



def start_receiver():
        instruction = sh_file_path + "/start_ros_alici.sh"
        return instruction




