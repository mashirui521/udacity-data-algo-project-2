import os

def find_files_under_path(suffix, path, files):
    dir_list = os.listdir(path)
    for dir in dir_list:
        full_path = os.path.join(path, dir)
        if os.path.isdir(full_path):
            find_files_under_path(suffix, full_path, files)
        elif os.path.isfile(full_path):
            if full_path.endswith(suffix):
                files.append(full_path)

def find_files(suffix, path):
    if not os.path.isdir(path):
        print('Warning: the given path {} is not a directory or doesn''t exist.'.format(path))
        return None
    else:
        files = list()
        find_files_under_path(suffix, path, files)
        return files

###################################  TEST  ###############################################
def test_no_c_file():
    print('\n--------------------   TEST_NO_C_FILE   ------------------')

    print('{} C-Files are found'.format(len(find_files('.c', './testdata/testdir_no_c'))))       # output: 0 C-Files are found

    print('--------------------   END: TEST_NO_C_FILE   ------------------\n')

def test_invalid_path():
    print('\n--------------------   TEST_INVALID_PATH   ------------------')

    print(find_files('.c', './test'))                         # return None with a warning: given path not exist

    print('--------------------   END: TEST_INVALID_PATH   ------------------\n')

def test():
    print('\n--------------------   TEST   ------------------')

    c_files = sorted(find_files('.c', './testdata/testdir'))  # sorted for printing

    print('{} C-Files are found:'.format(len(c_files)))       # output: 4 C-Files are found
    print(*c_files, sep='\n')                                 #        './testdir/subdir5/a.c', 
                                                              #        './testdir/subdir3/subsubdir1/b.c', 
                                                              #        './testdir/subdir1/a.c', 
                                                              #        './testdir/t1.c'

    print('--------------------   END: TEST   ------------------\n')

def TEST_SUITE():
    test()
    test_invalid_path()
    test_no_c_file()

TEST_SUITE()