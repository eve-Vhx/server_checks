# server_checks
This package is intended to check the status of the AWS OpenVPN server and monitor ROS processes. The script achieves the following tasks:

1. Checks to see if RosCore is running and if not initializes a new instance
2. Relaunches the behavior logic node and websocket after initializing the RosCore
