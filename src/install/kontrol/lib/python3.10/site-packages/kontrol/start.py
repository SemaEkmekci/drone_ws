
sh_file_path = "/home/sema/Desktop/drone_ws/src/start_instructions_sh"

def start_gazebo():
        instruction = sh_file_path + "./start_gazebo.sh"
        return instruction


def start_ardupilot():
        instruction = sh_file_path + "./start_ardupilot.sh"
        return instruction