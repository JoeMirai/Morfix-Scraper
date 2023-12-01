import os
import requests
words = ["Courageous","Adventurous","Self-disciplined","Affectionate","Observant","Determined","Ambitious","Diligent","Easygoing","Fair","Objective","Impartial","Considerate","Blunt","Laid-back","Adaptable","Quick-witted","Conscientious","Extroverted","Reserved","Introverted","Agreeable","Neurotic","Eradicate","Coexist","Situating","Co-location","Comprehension","Possess","Yield","Concessions","Incline","Tend","Banking-on","Progressively","Ambiguous"]  # Replace with your list of words


def create_folder_if_not_exist(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def save_html(url, folder_path, word):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder_path, f"{word}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"HTML for '{word}' saved successfully.")
    else:
        print(f"Failed to fetch HTML for '{word}'. Status code: {response.status_code}")

def main():
    global words

    base_url = "https://www.morfix.co.il/"
    output_folder = "html_output"

    create_folder_if_not_exist(output_folder)

    for word in words:
        url = f"{base_url}{word}"
        save_html(url, output_folder, word)

if __name__ == "__main__":
    main()
