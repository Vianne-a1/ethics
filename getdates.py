import re

def find_dates(file_path):
    date_pattern = r'((\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|(\d{1,2} (?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).* \d{1,2},* \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?),* \d{4})|(\d{1,2}/\d{4})|(?<!\d{3} )([12][0-9]{3})|(\d{1,2}/\d{4}))'

    try:
        with open(file_path, 'r') as file:
            total_unique_dates = set()
            print("Dates found in the file:")
            for line_num, line in enumerate(file, start=1):
                matches = re.findall(date_pattern, line)
                unique_line_dates = {match for group in matches for match in group if match}  
                if unique_line_dates:
                    for date in unique_line_dates:
                        print(f"Line {line_num}: {date}")
                    total_unique_dates.update(unique_line_dates)  
            
            total_count = len(total_unique_dates)
            if total_count > 0:
                print(f"\nTotal unique dates found: {total_count}")
            else:
                print("No dates found in the file.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'datefile.dat'
find_dates(file_path)