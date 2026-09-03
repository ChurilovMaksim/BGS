cmake_minimum_required(VERSION 3.16)
project(arithmetic_cat_map_research LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(cross_term_energy
  computations/cpp/m1/cross_term_energy.cpp)
add_executable(fourth_moment_factorization
  computations/cpp/verification/fourth_moment_factorization.cpp)
add_executable(catmap_order
  computations/cpp/number_theory/catmap_order.cpp)
add_executable(relation_automaton
  computations/cpp/shape/relation_automaton.cpp)

foreach(target cross_term_energy fourth_moment_factorization catmap_order relation_automaton)
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic)
endforeach()
