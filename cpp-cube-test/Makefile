cc = g++
cflags = -lmingw32 -lSDL2main -lSDL2 -lSDL2_image
src_files = src/*.cpp
include_dirs = -I include
lib_dirs = -L lib
output_file = bin/main

default:
	$(cc) -o $(output_file) $(src_files) $(include_dirs) $(lib_dirs) $(cflags)
	$(output_file)