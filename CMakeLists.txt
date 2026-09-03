cmake_minimum_required(VERSION 3.20)
project(wow_catmap_verifiers LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(
  fourth_moment_pair_key_verifier
  computations/cpp/fourth_moment_pair_key_verifier.cpp
)

add_executable(
  cat_map_order
  computations/cpp/cat_map_order.cpp
)

if (MSVC)
  target_compile_options(fourth_moment_pair_key_verifier PRIVATE /W4)
  target_compile_options(cat_map_order PRIVATE /W4)
else()
  target_compile_options(fourth_moment_pair_key_verifier PRIVATE -Wall -Wextra -Wpedantic)
  target_compile_options(cat_map_order PRIVATE -Wall -Wextra -Wpedantic)
endif()
