cmake_minimum_required(VERSION 3.20)
project(WoW LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

add_executable(cross_term_energy src/cpp/m1/cross_term_energy.cpp)
add_executable(fourth_moment_factorization src/cpp/verification/fourth_moment_factorization.cpp)
