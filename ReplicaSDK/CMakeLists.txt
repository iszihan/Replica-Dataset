# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
cmake_minimum_required(VERSION 2.6.0)

project(ReplicaSDK)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_LIST_DIR}/../cmake")

set(PTEX_SHADER_DIR "${CMAKE_CURRENT_LIST_DIR}/shaders" CACHE PATH "Where the shaders live")

file(GLOB srcs_ptex ptex/*.cpp)
file(GLOB hdrs include/*.h)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -msse2 -msse3 -Wall -std=c++11 -fopenmp -DSHADER_DIR=${PTEX_SHADER_DIR}")

add_library(ptex SHARED
            ${srcs_ptex}
            ${hdrs}
)

target_link_libraries(ptex
                      ${Eigen_LIBRARIES}
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      stdc++fs
)
target_include_directories(ptex PUBLIC
            ${Pangolin_INCLUDE_DIRS}
            ${Eigen_INCLUDE_DIRS}
            ${dl_INCLUDE_DIRS}
            ${CMAKE_CURRENT_LIST_DIR}
)

include_directories(${Pangolin_INCLUDE_DIRS})
include_directories(${EIGEN3_INCLUDE_DIR})
include_directories(${dl_INCLUDE_DIRS})
include_directories("./include")

add_executable(ReplicaViewer src/viewer.cpp src/MirrorSurface.cpp)

target_link_libraries(ReplicaViewer
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(ReplicaRendererDataset src/render_dataset.cpp src/MirrorSurface.cpp)

target_link_libraries(ReplicaRendererDataset
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(ReplicaVideoRenderer src/render_video.cpp src/MirrorSurface.cpp)

target_link_libraries(ReplicaVideoRenderer
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)


add_executable(ReplicaRenderer src/render.cpp src/MirrorSurface.cpp)

target_link_libraries(ReplicaRenderer
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)


add_executable(DepthMeshViewer src/depth_mesh_viewer.cpp)

target_link_libraries(DepthMeshViewer
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(DepthMeshViewerLayered src/depth_mesh_viewer_layered.cpp)

target_link_libraries(DepthMeshViewerLayered
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(DepthMeshRenderer src/depth_mesh_render.cpp)

target_link_libraries(DepthMeshRenderer
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(DepthMeshRendererBatch src/depth_mesh_render_batch.cpp)

target_link_libraries(DepthMeshRendererBatch
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(DepthMeshRendererLayered src/depth_mesh_render_layered.cpp)

target_link_libraries(DepthMeshRendererLayered
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)

add_executable(DepthMeshRendererLayeredBatch src/depth_mesh_render_layered_batch.cpp)

target_link_libraries(DepthMeshRendererLayeredBatch
                      ${Pangolin_LIBRARIES}
                      ${dl_LIBRARIES}
                      GL
                      GLEW
                      ptex
                      stdc++fs
)
