import wget


train = "https://s3.amazonaws.com/ava-dataset/trainval/"
dir_path = '../../../data/AVA/trainval/'

print("train")
vid_name = list()
with open("trainval.txt", 'r') as f:
    tmp = f.readline()
    while tmp:
        vid_name.append(tmp)
        tmp = f.readline()

for v in vid_name:
    try:
        wget.download(train+v[:-1], out=dir_path)
        print(v)
    except:
        print("failed", v)


##############
print("test")
test = "https://s3.amazonaws.com/ava-dataset/test/"
dir_path = '../../../data/AVA/test/'

vid_name = list()
with open("test.txt", 'r') as f:
    tmp = f.readline()
    while tmp:
        vid_name.append(tmp)
        tmp = f.readline()

for v in vid_name:
    try:
        wget.download(test+v[:-1], out=dir_path)
        print(v)
    except:
        print("failed", v)

