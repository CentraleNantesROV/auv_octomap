from simple_launch import SimpleLauncher


def generate_launch_description():
    
    sl = SimpleLauncher(use_sim_time = True)
    
    with sl.group(ns='bluerov2'):

        sl.node('octomap_server', 'octomap_saver_node',
                parameters = {'full': True,
                              'octomap_path': sl.find('auv_octomap', 'floatgen.bt', 'maps')})
        
    return sl.launch_description()
