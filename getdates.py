import re

def find_dates(file_path):
    date_pattern = r'(/((\d{1,2}(/|-)){2}\d{2,4})|(\d{1,2} ((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)) \d{4})|(((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)).* \d{1,2},* \d{4})|(((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)),* \d{4})|(\d{1,2}/\d{4})|([12][0-9]{3})|((19|20)\d{2})/gm)'

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(date_pattern, content)
            dates = [match for group in matches for match in group if match]
            counter = len(dates)
            if dates:
                print(f"Dates found in the file ({counter} total):")
                for date in dates:
                    print(date)
                print(f"\nTotal dates found: {counter}")
            else:
                print("No dates found in the file.")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'datefile.dat'
find_dates(file_path)