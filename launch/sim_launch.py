from simple_launch import SimpleLauncher, GazeboBridge

sl = SimpleLauncher(use_sim_time = True)

sl.declare_gazebo_axes(x=1., y=0., z=1., roll=0.,pitch=0., yaw=0.)
sl.declare_arg('moving', False)
sl.declare_arg('sliders', default_value=True)


def launch_setup():

    gz_world = 'floatgen'
    GazeboBridge.set_world_name(gz_world)

    # run world
    sl.include('floatgen', 'farm_launch.py')

    # spawn BlueROV2
    sl.include('bluerov2_description', 'upload_bluerov2_launch.py',
               launch_arguments={'gazebo_world_name': gz_world, 'sliders': False})

    # BlueROV2 control
    with sl.group(ns='bluerov2'):

        # load body controller anyway
        sl.node('auv_control', 'cascaded_pid',
                parameters=[sl.find('bluerov2_control', 'cascaded_pid.yaml')])

        if sl.arg('sliders'):
            sl.node('slider_publisher', 'slider_publisher', name='pose_control',
                    arguments=[sl.find('auv_octomap', 'pose_setpoint.yaml')])

    sl.rviz(sl.find('auv_octomap', 'octomap.rviz'))
    
    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)
