#!/bin/bash
outdir=$1
width=$2
height=$3
find * -type d -maxdepth 0 | xargs -P 3 -I {} -n 1 ../build/ReplicaSDK/ReplicaRendererDataset {}/mesh.ply {}/textures {}/glass.sur ../glob/{}_6dof.txt y $outdir $width $height

