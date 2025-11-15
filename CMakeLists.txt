cmake_minimum_required(VERSION 4.0)
project(wit_in4sdsu)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(wit_in4sdsu
        survey.cpp
        survey.h)
