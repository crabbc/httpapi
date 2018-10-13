import os, glob, hashlib, shutil

root = os.path.abspath(os.curdir)
files = os.walk(root)

def find_path(file_hash):
    flag = False
    path = root + '/files/'
    files = os.walk(path)
    for i in files:
        folder = str(i[0])
        curr_folder = i[1]
        filename = i[2]

        if flag:
            return folder+'/', filename[0]
        
        if curr_folder and curr_folder[0] == file_hash:
            flag = True

def get_hash(filename):
    path = root + '/files/temps/'
    file = open(str(path)+filename, 'r')
    h = hashlib.md5(file.read().encode('utf-8')).hexdigest()
    return h
    
def get_new_dir(filename):
    path = root + '/files/'
    h = get_hash(filename)
    new_dir = h[0]+h[1]
    if not os.path.exists(new_dir):
        os.makedirs(path+new_dir, exist_ok=True)
    if not os.path.exists(new_dir+'/'+h):
        os.makedirs(path+new_dir+'/'+h, exist_ok=True)
        
    new_path = path + new_dir+'/'+h
    old_path = path + '/temps/'
    shutil.move(old_path+filename, new_path)
    return h
