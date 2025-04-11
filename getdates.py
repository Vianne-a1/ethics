import re

def count_dates(file_path, dates_file_path, count_file_path):
    date_pattern = r'((\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|(\d{1,2} (?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)|May|Jun(?:e)|Jul(?:y)|Aug(?:ust)|Sep(?:tember)|Sept|Oct(?:ober)|Nov(?:ember)|Dec(?:ember)) \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)|Mar(?:ch)|Apr(?:il)|May|Jun(?:e)|Jul(?:y)|Aug(?:ust)|Sep(?:tember)|Sept|Oct(?:ober)|Nov(?:ember)|Dec(?:ember)) .* \d{1,2},* \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)|Mar(?:ch)|Apr(?:il)|May|Jun(?:e)|Jul(?:y)|Aug(?:ust)|Sep(?:tember)|Sept|Oct(?:ober)|Nov(?:ember)|Dec(?:ember)),* \d{4})|(\d{1,2}/\d{4})|(?<!\d)([12][0-9]{3})(?!\d)|(\d{1,2}/\d{4}))'

    try:
        total_dates_count = 0  # Sum of all dates
        with open(dates_file_path, 'w') as dates_file, open(count_file_path, 'w') as count_file:
            with open(file_path, 'r') as file:
                for line_num, line in enumerate(file, start=1):
                    matches = re.findall(date_pattern, line)
                    unique_dates = {match for group in matches for match in group if match}  
                    count_in_line = len(unique_dates)

                    if count_in_line > 0:
                        for date in unique_dates:
                            print(f"Line {line_num}: {date}")  
                            dates_file.write(f"Line {line_num}: {date}\n")
                        
                        # Write count of dates to `count_output.txt`
                        print(f"Line {line_num}: {count_in_line} date(s)")  
                        count_file.write(f"Line {line_num}: {count_in_line} date(s)\n")
                    
                    total_dates_count += count_in_line 

            # Write total count to `count_output.txt`
            count_file.write(f"\nTotal dates found across all lines: {total_dates_count}\n")
            print(f"\nTotal dates found across all lines: {total_dates_count}")  # Print total count
            print(f"Results have been written to {dates_file_path} and {count_file_path}")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'datefile.dat'  
dates_file_path = 'dates_output.txt'  
count_file_path = 'count_output.txt'  
count_dates(file_path, dates_file_path, count_file_path)