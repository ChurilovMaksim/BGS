cmake_minimum_required(VERSION 3.16)
project(arithmetic_cat_map_research LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(mobius_pair_key_diagnostic
  computations/cpp/mobius_pair_key_diagnostic.cpp)
add_executable(fourth_moment_pair_key_verifier
  computations/cpp/fourth_moment_pair_key_verifier.cpp)
add_executable(cat_map_order
  computations/cpp/cat_map_order.cpp)
add_executable(relation_shape_automaton
  computations/cpp/relation_shape_automaton.cpp)

foreach(target
    mobius_pair_key_diagnostic
    fourth_moment_pair_key_verifier
    cat_map_order
    relation_shape_automaton)
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic)
endforeach()
