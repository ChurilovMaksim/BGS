cmake_minimum_required(VERSION 3.20)
project(wow_catmap_verifiers LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(Boost REQUIRED)

add_executable(
  fourth_moment_pair_key_verifier
  computations/cpp/fourth_moment_pair_key_verifier.cpp
)

add_executable(
  cat_map_order
  computations/cpp/cat_map_order.cpp
)

add_executable(
  cayley_energy_verifier
  computations/cpp/cayley_energy_verifier.cpp
)

add_executable(
  cayley_fibonacci_verifier
  computations/cpp/cayley_fibonacci_verifier.cpp
)
target_include_directories(cayley_fibonacci_verifier PRIVATE ${Boost_INCLUDE_DIRS})

add_executable(
  cayley_direct_energy_verifier
  computations/cpp/cayley_direct_energy_verifier.cpp
)

add_executable(
  cayley_trace_intercept_rigidity
  computations/cpp/cayley_trace_intercept_rigidity.cpp
)

if (MSVC)
  foreach(target
      fourth_moment_pair_key_verifier
      cat_map_order
      cayley_energy_verifier
      cayley_fibonacci_verifier
      cayley_direct_energy_verifier
      cayley_trace_intercept_rigidity)
    target_compile_options(${target} PRIVATE /W4)
  endforeach()
else()
  foreach(target
      fourth_moment_pair_key_verifier
      cat_map_order
      cayley_energy_verifier
      cayley_fibonacci_verifier
      cayley_direct_energy_verifier
      cayley_trace_intercept_rigidity)
    target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic)
  endforeach()
endif()