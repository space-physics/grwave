cmake_minimum_required(VERSION 3.1)
project(GRwave Fortran)

add_executable(grwave.bin grwave.for)
target_compile_options(grwave.bin PRIVATE -w)
