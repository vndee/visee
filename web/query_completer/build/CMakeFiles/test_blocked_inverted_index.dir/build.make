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
include CMakeFiles/test_blocked_inverted_index.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test_blocked_inverted_index.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_blocked_inverted_index.dir/flags.make

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o: CMakeFiles/test_blocked_inverted_index.dir/flags.make
CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o: ../test/test_blocked_inverted_index.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/hoang/Desktop/autocomplete/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o -c /home/hoang/Desktop/autocomplete/test/test_blocked_inverted_index.cpp

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/hoang/Desktop/autocomplete/test/test_blocked_inverted_index.cpp > CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.i

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/hoang/Desktop/autocomplete/test/test_blocked_inverted_index.cpp -o CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.s

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.requires:

.PHONY : CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.requires

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.provides: CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.requires
	$(MAKE) -f CMakeFiles/test_blocked_inverted_index.dir/build.make CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.provides.build
.PHONY : CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.provides

CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.provides.build: CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o


# Object files for target test_blocked_inverted_index
test_blocked_inverted_index_OBJECTS = \
"CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o"

# External object files for target test_blocked_inverted_index
test_blocked_inverted_index_EXTERNAL_OBJECTS =

test_blocked_inverted_index: CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o
test_blocked_inverted_index: CMakeFiles/test_blocked_inverted_index.dir/build.make
test_blocked_inverted_index: CMakeFiles/test_blocked_inverted_index.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/hoang/Desktop/autocomplete/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_blocked_inverted_index"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_blocked_inverted_index.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_blocked_inverted_index.dir/build: test_blocked_inverted_index

.PHONY : CMakeFiles/test_blocked_inverted_index.dir/build

CMakeFiles/test_blocked_inverted_index.dir/requires: CMakeFiles/test_blocked_inverted_index.dir/test/test_blocked_inverted_index.cpp.o.requires

.PHONY : CMakeFiles/test_blocked_inverted_index.dir/requires

CMakeFiles/test_blocked_inverted_index.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_blocked_inverted_index.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_blocked_inverted_index.dir/clean

CMakeFiles/test_blocked_inverted_index.dir/depend:
	cd /home/hoang/Desktop/autocomplete/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/hoang/Desktop/autocomplete /home/hoang/Desktop/autocomplete /home/hoang/Desktop/autocomplete/build /home/hoang/Desktop/autocomplete/build /home/hoang/Desktop/autocomplete/build/CMakeFiles/test_blocked_inverted_index.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_blocked_inverted_index.dir/depend

