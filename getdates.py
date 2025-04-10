def read_dat_file(file_path):
    try:
        with open(file_path, 'r') as file:  
            data = file.readlines()  
            return data
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = '/workspaces/ethics/datefile.dat'
data = read_dat_file(file_path)
if data:
    for line in data:
        print(line.strip())  