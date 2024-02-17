#!/bin/bash

cd ~/Desktop/drone_ws
colcon build
source install/setup.bash
ros2 run kontrol alici
