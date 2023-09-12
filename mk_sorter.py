import os
import shutil
import datetime

if __name__ == "__main__":
    source_dir = "."
    files = os.scandir(source_dir)

    relevant_files = []
    for file in files:
        if file.is_file():
            relevant_files.append(file.name)
    relevant_files.remove('mk_sorter.py')

    all_no_extensions = []
    muxed_no_extensions = []
    for file in relevant_files:
        no_extension = file[:file.rfind('.')]
        if no_extension in all_no_extensions:
            muxed_no_extensions.append(no_extension)
        else:
            all_no_extensions.append(no_extension)

    if not os.path.exists("./unmuxed/"):
        os.mkdir("./unmuxed/")
        log = open("./unmuxed/log.txt", "x")
    else:
        if not os.path.exists("./unmuxed/log.txt"):
            log = open("./unmuxed/log.txt", "x")
        else:
            log = open("./unmuxed/log.txt", "a")
    
    log.write(f'{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} - start')
    log.write("\nFollowing files moved to unmuxed folder:")

    for file in relevant_files:
        no_extension = file[:file.rfind('.')]
        if not no_extension in muxed_no_extensions:
            shutil.move(file, "./unmuxed/")
            log.write(f"\n\t{file}")
    log.write(f'\n{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")} - end\n')
    log.write("close\n\n")
    log.close()