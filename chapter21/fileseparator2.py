import os,shutil

#NOTE :you can write every single extension inside tuple
dict_extensions={
    "audio_extensions" :('.mp3','.m4a','.wav','.flac'),
    "video_extensions": ('mp4','.mkv','.MKV','.flv','.mpeg'),
    "document_extension" : ('.doc','.pdf','.txt'),
    "image_extensions": ('.jpg','.jpeg','.png')
}


folderpath=input("enter your path : ")

def file_finder(folder_path,file_extension):
    # files=[]
    # for file in os.listdir(folder_path):
    #     for extension in file_extension:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]

# print(file_finder(folder_path,video_extensions))
for extension_type,extension_tuple in dict_extensions.items():
    folder_name= extension_type.split('_')[0] + ' Files'
    folder_path=os.path.join(folderpath,folder_name)
    # print(folder_path)
    os.mkdir(folder_path)
    # print(f"calling file finder....{extension_type} and {extension_tuple}")
    for item in (file_finder(folderpath,extension_tuple)):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
    # print(f"calling file finder....{extension_type} and {extension_tuple}")
    # print(file_finder(folder_path,extension_tuple))
