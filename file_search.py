# Related blog post - https://algoritmim.co.il/interview-practice/recursive-search-in-a-file-system/

import os
import shutil


def find_files_recur(root, file_name):
    def __get_files(folder):
        folder_files = os.listdir(folder)
        for f in folder_files:
            yield os.path.join(folder, f)

    def __find_file(f, name):
        if not os.path.isdir(f):
            if os.path.basename(f) == name:
                return f
        else:
            return __find_file_in_folder(f, name)

    def __find_file_in_folder(folder, name):
        for f in __get_files(folder):
            result = __find_file(f, name)
            if result:
                return result
        return None

    return __find_file(root, file_name)


def run_tests(path):
    def __before(path):
        os.mkdir(path)
        file_path = os.path.join(path, "file1.txt")
        f = open(file_path, "w+")
        f.write("hello!")

        subdir = os.path.join(path, "hello")
        os.mkdir(subdir)
        sub_file_path = os.path.join(subdir, "file2.txt")
        f = open(sub_file_path, "w+")
        f.write("goodbye")

        return file_path, sub_file_path

    def __after(path):
        shutil.rmtree(path)

    file_path, sub_file_path = __before(path)
    try:
        assert find_files_recur(path, "file1.txt") == file_path
        assert find_files_recur(path, "file2.txt") == sub_file_path
        assert find_files_recur(path, "hello") is None
    except:
        print("TESTS FAILED")
    finally:
        __after(path)


if __name__ == '__main__':
    tests_path = "/tmp/file_search_tests"
    run_tests(tests_path)
