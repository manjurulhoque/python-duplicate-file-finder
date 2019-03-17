import os, sys
import hashlib

class DuplicateFinder:
    def __init__(self, folders):
        self.folders = folders

    def get_duplicates(self):
        duplicates = {}
        for folder in self.folders:
            if os.path.exists(folder):
                self.join_dict(duplicates, self.find_duplicate(folder))
            else:
                print('%s is not a valid path, please verify' % folder)
                sys.exit()
        return duplicates

    def find_duplicate(self, folder):
        # Duplicates in format {hash:[names]}
        duplicates = {}
        for dirName, subdirs, fileList in os.walk(folder):
            print('Currently Scanning %s...' % dirName)
            for filename in fileList:
                # Get the path to the file
                path = os.path.join(dirName, filename)
                # Calculate hash
                file_hash = hashfile(path)
                # print(file_hash)
                # Add or append the file path
                if file_hash in duplicates:
                    duplicates[file_hash].append(path)
                else:
                    duplicates[file_hash] = [path]
        return duplicates

    def join_dict(self, dict1, dict2):
        for key in dict2.keys():
            if key in dict1:
                dict1[key] = dict1[key] + dict2[key]
            else:
                dict1[key] = dict2[key]
    
    def hashfile(self, path, blocksize = 65536):
        afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()

    def print_results(self, dict1):
        results = list(filter(lambda x: len(x) > 1, dict1.values()))
        if len(results) > 0:
            print('Duplicates Are Found:')
            print('___________________')
            for result in results:
                for file in result:
                    print('\t\t%s' % file)
                print('___________________')
        else:
            print('No duplicate files found.')
 
def findDuplicate(parentFolder):
    # Duplicates in format {hash:[names]}
    duplicates = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Currently Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # print(file_hash)
            # Add or append the file path
            if file_hash in duplicates:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
    return duplicates


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Files Found:')
        print('___________________')
        for result in results:
            for file in result:
                print('\t\t%s' % file)
            print('___________________')
    else:
        print('No duplicate files found.')

if len(sys.argv) > 1:
    duplicates = {}
    folders = sys.argv[1:]
    finder = DuplicateFinder(folders)
    finder.print_results(finder.get_duplicates())
else:
    print('Usage: python app.py folder or python app.py folder1 folder2 folder3')