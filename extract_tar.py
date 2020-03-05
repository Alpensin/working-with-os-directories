import tarfile

s_file = r"C:\TEMP\ports.tar.gz"  #Путь до архива
t_folder = r'C:\TEMP\extr' # Папка куда разархивировать
with tarfile.open(s_file) as tf:
    tf.extractall(t_folder)
print("ready")
