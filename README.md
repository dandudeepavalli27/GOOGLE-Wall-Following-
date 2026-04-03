# GOOGLE-Wall-Following
Aim
To implement a wall-following control rule based on distance error.
General Objective
To understand wall-following behavior as a reactive navigation strategy and how distance error helps maintain safe distance from walls.
Specific Objective
To apply the rule:
Desired Distance = 0.5 m
Actual Distance = 0.2 m
If actual < desired → Move Away from Wall
Dataset
Robot Wall Following Dataset
Source: PythonRobotics
Procedure
Input desired distance
Input actual distance
Compare both values
If actual < desired → Move Away
Display result
Algorithm
Start
Input desired and actual distance
If actual < desired → Move Away
Else → Maintain Distance
Display result
Stop
Code Logic
if actual < desired:
    action = "Move Away from Wall"
Result
Since the robot is too close to the wall:
Move Away from Wall action is executed
Industry Application
Wall-following is used in:
Mobile robots
Cleaning robots
Autonomous navigation
Indoor mapping
Companies like Google use such strategies in:
Robotics research
Navigation systems
Autonomous platforms
Conclusion
Wall-following ensures safe navigation by maintaining optimal distance from obstacles using simple reactive control.
