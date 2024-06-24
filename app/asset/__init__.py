# Baca data dari file dan konversi menjadi list
import os

filepath = 'app/asset/datakhodam.txt'

def read_file_to_list():
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = file.read().splitlines()
        else:
            data = []
            
        return data
    
    except:
        return

data_list = read_file_to_list()


# Simpan data list ke file
def save_list_to_file(data_list):
    try:
        with open(filepath, 'w') as file:
            for item in data_list:
                file.write(f'{item}\n')
        
        return True
    except:
        return