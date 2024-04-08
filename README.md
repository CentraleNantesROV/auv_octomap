# AUV Octomap

This repository contains a basic example of how to get an octomap from a AUV with a sonar.


## Requirements

### For the simulation

- [BlueROV2](https://github.com/CentraleNantesROV/bluerov2.git)
- [auv_control](https://github.com/CentraleNantesROV/auv_control) for basic control laws, from source
- [Floatgen](https://github.com/CentraleNantesROV/floatgen.git) for the environnement


### For the octomap

- [octomap_server](https://github.com/OctoMap/octomap_mapping/tree/ros2)
    - or `sudo apt install ros-${ROS_DISTRO}-octomap-mapping`

## Installation 

Clone the package and its dependencies (if from source) in your ROS 2 workspace `src` and compile with `colcon`

## Running 

Run the simulation that will spawn a BlueROV2 below a floating wind turbine:

```bash
ros2 launch auv_octomap sim_launch.py
```

then run the octomap server:

```bash
ros2 launch auv_octomap octomap_launch.py
```

## Saving the current map

The current state of the octomap can be saved to `auv_octomap/maps/floatgen.bt` with:

```bash
ros2 launch auv_octomap save_launch.py
```
