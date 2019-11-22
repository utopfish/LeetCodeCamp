cmake_minimum_required(VERSION 3.15)
project(deleteNode)

set(CMAKE_CXX_STANDARD 11)

add_executable(deleteNode deleteNode.cpp ../../middle/removeNthFromEnd/removeNthFromEnd.cpp ../reverseList/reverseList.cpp)