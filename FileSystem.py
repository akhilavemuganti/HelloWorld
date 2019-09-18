import os


# Create a folder
# filePath="/Users/akhilavemuganti/Desktop/PythonWorkSpace"
# os.makedirs(filePath)

def main():
    wd = os.getcwd()
    print(wd)

    # print(os.path.join(wd, 'FileSystem2'))
    #
    # if not os.path.exists(os.path.join(wd, 'FileSystem2')):
    #     os.makedirs(os.path.join(wd, 'FileSystem2'))

    folder_Path = os.path.join(wd, 'FileSystem')
    file_name = "test.txt"
    file_path = os.path.join(folder_Path, file_name)

    with open(file=file_path, mode="w") as file:
        file.write("ABCD")
        file.close()


main()

# import os
#
# def createFolder():
#     work_directory=os.getcwdb()
#     print(work_directory)
#
#     print(os.path.join(work_directory,"NewFolder"))
#
#     if not os.path.exists(os.path.join(work_directory,"NewFolder")):
#         os.makedirs(os.path.join(work_directory,"NewFolder"))
#
#     folderPath=os.path.join(work_directory,"NewFolder")
#     fileName="Test1.txt"
#     path=os.path.join(folderPath,fileName)
#
#     file1=open(fileName,mode="w")
#     file1.write("This is a test file created using python")
#     file1.close()
#
#
# createFolder()


# #Create a file in the above folder created
# if os.path.exists(filePath):
#     print("1")
#     os.makedirs("FileSystem")
# else:
#     print("0")
#     os.makedirs(filePath)
#     os.makedirs("FileSystem")
#
# textFile=open("/Users/akhilavemuganti/Desktop/PythonWorkSpace/FileSystem/TestFile.txt","w+")
# textFile.write("This is a test file")
#
# #
