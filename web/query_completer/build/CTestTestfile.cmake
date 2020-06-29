# CMake generated Testfile for 
# Source directory: /home/hoang/Desktop/autocomplete
# Build directory: /home/hoang/Desktop/autocomplete/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_autocomplete "test_autocomplete")
add_test(test_blocked_inverted_index "test_blocked_inverted_index")
add_test(test_compact_forward_index "test_compact_forward_index")
add_test(test_completion_trie "test_completion_trie")
add_test(test_fc_dictionary "test_fc_dictionary")
add_test(test_integer_fc_dictionary "test_integer_fc_dictionary")
add_test(test_inverted_index "test_inverted_index")
add_test(test_locate_prefix "test_locate_prefix")
add_test(test_unsorted_list "test_unsorted_list")
subdirs("external")
subdirs("src")
subdirs("benchmark")
