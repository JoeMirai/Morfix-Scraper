import os
from bs4 import BeautifulSoup

html_folder = 'html_output'

for filename in os.listdir(html_folder):
    if filename.endswith(".html"):
        file_path = os.path.join(html_folder, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            # Find the relevant div containing the text
            translation_div = soup.find('div', class_='normal_translation_div')

            if translation_div:
                # Extract the text within the div
                translation_text = translation_div.get_text(strip=True)

                # Print the result
                print(f"{filename[:-5]} > {translation_text}")
            else:
                print(f"No translation found in {filename}")
