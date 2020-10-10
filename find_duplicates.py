import os
import hashlib


def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


duplicates = []
hash_keys = {}

rootdir = str(os.getcwd()) + "\\Images\\"

total_files = 0
total_hashed_files = 0

for root, dirs, files in os.walk(rootdir):
    total_files += len(files)


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        f = os.path.join(subdir, file)
        hash = file_hash(f)

        if hash in hash_keys:
            duplicates.append(f)
            os.remove(f)
            print('Removed: ', f)

        else:
            hash_keys[hash] = [f]

        total_hashed_files += 1

        if total_hashed_files % 100 == 0:
            print('{} / {}'.format(total_hashed_files, total_files))
