import re

def find_dates(file_path):

    date_pattern = r'((\d{1,2}(/|-)){2}\d{2,4})|(\d{1,2} \w{3,} \d{4})|(\w{3,}.* \d{1,2},* \d{4})|(\w{3,},* \d{4})|(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})|(\d{2}-\d{2}-\d{4})'

    # ((\d{1,2}(/|-)){2}\d{2,4})|(\d{1,2} \w{3,} \d{4})|(\w{3,}.* \d{1,2},* \d{4})|(\w{3,},* \d{4})

    try:
        with open(file_path, 'r') as file: 
            content = file.read()  

            matches = re.findall(date_pattern, content)

            dates = [match for group in matches for match in group if match]
            
            if dates:
                print("Dates found in the file:")
                for date in dates:
                    print(date)
            else:
                print("No dates found in the file.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'datefile.dat'
find_dates(file_path)