#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
import xacro

def generate_launch_description():
    # gazebo_pkg = get_package_share_directory('black_donut_gazebo')
    # gz_ros_pkg = get_package_share_directory('gazebo_ros')
    use_sim_time = LaunchConfiguration('use_sim_time')

    doc = xacro.process_file('/home/zyme/ros_ws/black_donut_simulation/src/black_donut_simulation/black_donut_description/urdf/black_donut_library.urdf.xacro')
    robot_desc = doc.toprettyxml(indent='  ')
    params = {'robot_description': robot_desc}

    # urdf_pkg = get_package_share_directory('black_donut_description')
    # urdf_path= os.path.join(urdf_pkg, 'urdf', "black_donut_library.urdf.xacro")
    # urdf = open(urdf_path).read()

    robot_state_publisher_node = Node(
        name="robot_state_publisher",
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": params, 'use_sim_time': use_sim_time}],
    )

    # joint_state_node = Node(
    #     name="joint_state_publisher",
    #     package="joint_state_publisher",
    #     executable="joint_state_publisher",
    # )

    # rviz_node = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     arguments=['-d', os.path.join(urdf_pkg, 'rviz2', 'display.rviz')],
    #     condition=IfCondition(LaunchConfiguration('open_rviz'))
    # )

    return LaunchDescription(
        [
            DeclareLaunchArgument('open_rviz', default_value='true', description='Open RViz.'),
            robot_state_publisher_node,
            #joint_state_node,
            #rviz_node
        ]
    )
