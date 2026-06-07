cmake_minimum_required(VERSION 3.5)
project(mobile_teleop)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch web
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
