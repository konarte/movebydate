import os
from datetime import datetime

#Получить текущую директорию, где запущен скрипт
#dir = os.path.abspath(os.curdir)
#Получить текущую директорию, где расположен скрипт
#os.path.abspath(__file__)



def movefle(source, dest):
    # Source file path source = 'data.csv'
    # destination file path dest = 'app/data.csv'
 
    # try renaming the source path
    # to destination path
    # using os.rename() method
    try:
        os.rename(source, dest)
        print("File is moved successfully")
 
    # If Source is a file
    # but destination is a directory
    except IsADirectoryError:
        print("Source is a file but destination is a directory.")
 
    # If source is a directory
    # but destination is a file
    except NotADirectoryError:
        print("Source is a directory but destination is a file.")
 
    # For permission related errors
    except PermissionError:
        print("Operation not permitted.")
 
    # For other errors
    except OSError as error:
        print(error)
         



directory = os.path.abspath(os.curdir)

for entry in os.scandir(directory):
    if entry.is_file() and not entry.name.endswith('.py'):
        print(entry.path)
        dirname =  str(entry.path).rsplit(sep='\\',maxsplit=1)[0]
        filename = str(entry.path).rsplit(sep='\\',maxsplit=1)[1]
        print(filename)
        stat = os.stat(entry.path)
        #print(stat)
        path2dir = str(datetime.fromtimestamp(stat.st_mtime)).split(sep=' ',maxsplit=1)[0]
        #print(str(datetime.fromtimestamp(stat.st_mtime)))
        print(path2dir)
        try:
            os.mkdir(path2dir)
        except OSError:
            print ("Создать директорию %s не удалось" % path2dir)
        else:
            print ("Успешно создана директория %s " % path2dir)
    
        print(filename, dirname+'\\'+path2dir+'\\'+filename)
        movefle(filename, dirname+'\\'+path2dir+'\\'+filename)

       


