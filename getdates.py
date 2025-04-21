import re

def find_dates(file_path):
    date_pattern = r'((\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|(\d{1,2} (?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).* \d{1,2},* \d{4})|((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?),* \d{4})|(\d{1,2}/\d{4})|(?<!\d{3} )([12][0-9]{3})|(\d{1,2}/\d{4}))'

    try:
        with open(file_path, 'r') as file:
            total_unique_dates = set()
            date_lines = []
            count_lines = []

            print("Dates found in the file:\n")  # Print header in terminal

            for line_num, line in enumerate(file, start=1):
                matches = re.findall(date_pattern, line)
                unique_line_dates = {match for group in matches for match in group if match}
                date_count = len(unique_line_dates)

                if unique_line_dates:
                    line_output = f"Line {line_num}: {', '.join(unique_line_dates)}"
                    print(line_output)  # Print to terminal
                    date_lines.append(line_output)
                    total_unique_dates.update(unique_line_dates)
                    count_lines.append(f"Line {line_num}: {date_count} date(s)")

        # Writing extracted dates per line to a text file
        with open("dates_found.txt", "w") as date_file:
            date_file.write("\n".join(date_lines) if date_lines else "No dates found.")

        # Writing the total count to another file
        total_count = len(total_unique_dates)
        with open("date_count.txt", "w") as count_file:
            count_file.write(f"Total unique dates found: {total_count}\n\n")
            count_file.write("\n".join(count_lines))

        print(f"\nTotal unique dates found: {total_count}")  # Print total count to terminal
        print("Extraction complete. Check 'dates_found.txt' and 'date_count.txt'.")

    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'datefile.dat'
find_dates(file_path)