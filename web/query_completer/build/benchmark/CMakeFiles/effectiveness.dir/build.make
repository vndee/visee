# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/hoang/Desktop/autocomplete

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/hoang/Desktop/autocomplete/build

# Include any dependencies generated for this target.
include benchmark/CMakeFiles/effectiveness.dir/depend.make

# Include the progress variables for this target.
include benchmark/CMakeFiles/effectiveness.dir/progress.make

# Include the compile flags for this target's objects.
include benchmark/CMakeFiles/effectiveness.dir/flags.make

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o: benchmark/CMakeFiles/effectiveness.dir/flags.make
benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o: ../benchmark/effectiveness.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/hoang/Desktop/autocomplete/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o"
	cd /home/hoang/Desktop/autocomplete/build/benchmark && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/effectiveness.dir/effectiveness.cpp.o -c /home/hoang/Desktop/autocomplete/benchmark/effectiveness.cpp

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/effectiveness.dir/effectiveness.cpp.i"
	cd /home/hoang/Desktop/autocomplete/build/benchmark && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/hoang/Desktop/autocomplete/benchmark/effectiveness.cpp > CMakeFiles/effectiveness.dir/effectiveness.cpp.i

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/effectiveness.dir/effectiveness.cpp.s"
	cd /home/hoang/Desktop/autocomplete/build/benchmark && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/hoang/Desktop/autocomplete/benchmark/effectiveness.cpp -o CMakeFiles/effectiveness.dir/effectiveness.cpp.s

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.requires:

.PHONY : benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.requires

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.provides: benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.requires
	$(MAKE) -f benchmark/CMakeFiles/effectiveness.dir/build.make benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.provides.build
.PHONY : benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.provides

benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.provides.build: benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o


# Object files for target effectiveness
effectiveness_OBJECTS = \
"CMakeFiles/effectiveness.dir/effectiveness.cpp.o"

# External object files for target effectiveness
effectiveness_EXTERNAL_OBJECTS =

effectiveness: benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o
effectiveness: benchmark/CMakeFiles/effectiveness.dir/build.make
effectiveness: benchmark/CMakeFiles/effectiveness.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/hoang/Desktop/autocomplete/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../effectiveness"
	cd /home/hoang/Desktop/autocomplete/build/benchmark && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/effectiveness.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
benchmark/CMakeFiles/effectiveness.dir/build: effectiveness

.PHONY : benchmark/CMakeFiles/effectiveness.dir/build

benchmark/CMakeFiles/effectiveness.dir/requires: benchmark/CMakeFiles/effectiveness.dir/effectiveness.cpp.o.requires

.PHONY : benchmark/CMakeFiles/effectiveness.dir/requires

benchmark/CMakeFiles/effectiveness.dir/clean:
	cd /home/hoang/Desktop/autocomplete/build/benchmark && $(CMAKE_COMMAND) -P CMakeFiles/effectiveness.dir/cmake_clean.cmake
.PHONY : benchmark/CMakeFiles/effectiveness.dir/clean

benchmark/CMakeFiles/effectiveness.dir/depend:
	cd /home/hoang/Desktop/autocomplete/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/hoang/Desktop/autocomplete /home/hoang/Desktop/autocomplete/benchmark /home/hoang/Desktop/autocomplete/build /home/hoang/Desktop/autocomplete/build/benchmark /home/hoang/Desktop/autocomplete/build/benchmark/CMakeFiles/effectiveness.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : benchmark/CMakeFiles/effectiveness.dir/depend

