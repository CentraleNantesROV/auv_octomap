from simple_launch import SimpleLauncher


def generate_launch_description():
    
    sl = SimpleLauncher(use_sim_time = True)
    
    with sl.group(ns='bluerov2'):

        sl.node('octomap_server', 'octomap_server_node',
                remappings = {'cloud_in': 'cloud'},
                parameters = {'sensor_model.max_range': 50.,
                              'frame_id': 'world',
                              'resolution': 0.1,
                              'octomap_path': sl.find('auv_octomap', 'floatgen.bt', 'maps')})
        
    return sl.launch_description()
