### black_donut_autonomy

clone to your ROS2 workspace
```
$ git clone git@github.com:BehaviorTree/BehaviorTree.CPP.git
$ colcon build 

$ros2 pkg create test --build--type ament_cmake --dependencies behaviortree_cpp rclcpp 
$ colcon build
```

### 4 Patrol System 
Partol လှည့်ရန်။
```
ros2 launch black_donut_gazebo black_donut_sim_ros2_control.launch.py
ros2 launch black_donut_gazebo controller_spawner.launch.py
ros2 launch black_donut_nav2 sim_localization_init_pose_launch.py
ros2 launch black_donut_nav2 sim_navigation_launch.py map_subscribe_transient_local:=true
ros2 launch black_donut_autonomy autonomy.launch.py
```




<a href="https://github.com/ROM-robotics/black_donut">မူလစာမျက်နှာ </a>
