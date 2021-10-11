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

def test():
    print(find_files('.c', './test'))                         # return None with a warning: given path not exist

    c_files = sorted(find_files('.c', './testdir'))           # return ['./testdir/subdir5/a.c', 
                                                              #         './testdir/subdir3/subsubdir1/b.c', 
                                                              #         './testdir/subdir1/a.c', 
                                                              #         './testdir/t1.c'] 
                                                              # sorted for printing
    
    print('{} C-Files are found:'.format(len(c_files)))
    print(*c_files, sep='\n')                                 

test()