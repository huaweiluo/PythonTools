#coding:utf-8
import os
import sys
import shutil
import xlsxwriter

#获取当前路径
#path = os.getcwd()
#print(path)

file_type_list = ['png', 'jpeg', 'jpg']

def get_file_list(folder):
    filelist = [] # 存储要copy的文件全名
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_type = file.split('.')[-1]
            if (file_type in file_type_list):
                file_fullname = os.path.join(dirpath, file) # 文件全名
                filelist.append(file_fullname)
    return filelist

def copy_file(src_file_list, dst_folder):
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)
        
    fileName_list = []
    for file in src_file_list:
        shutil.copy(file, dst_folder)
        fileName = file.split('/')[-1]
        fileName_list.append(fileName)
        
    return fileName_list

def removedir(rootdir):
    for root, dirs, files in os.walk(rootdir, topdown=False):
        for name in files:
            os.remove(os.path.join(rootdir, name))
        for name in dirs:
            os.rmdir(os.path.join(rootdir, name))
    os.rmdir(rootdir)

def generate_excel(expenses):
    workbook = xlsxwriter.Workbook('./images_list.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column(1, 1, 30)

    bold_format = workbook.add_format({'bold': True})
    worksheet.write('A1', 'index', bold_format)
    worksheet.write('B1', 'imageName', bold_format)

    row = 1
    col = 0
    index = 1

    for item in (expenses):
        worksheet.write_string(row, 0, str(index))
        worksheet.write_string(row, col+1, str(item))
        row += 1
        index += 1
        
    workbook.close()

if (__name__=="__main__"):
    print(sys.argv)
#    print(len(sys.argv))
#    print(sys.argv[0])

    if len(sys.argv)<2:
        print ("Please enter source folder.")
        sys.exit()

    if len(sys.argv)<3:
        print ("Please enter destination folder.")
        sys.exit()

    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]

    filelist = get_file_list(src_folder)
#    print(filelist)

    if os.path.exists(dst_folder):
        removedir(dst_folder)
        
    fileName_list = copy_file(filelist, dst_folder)

#    print(fileName_list)

    generate_excel(fileName_list)

    print ("src_folder:%s\ndst_folder:%s\ncopy success..." % (src_folder, dst_folder))

