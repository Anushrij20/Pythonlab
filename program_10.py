# -*- coding: utf-8 -*-
"""Program_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GfD458zBa0iiWAEUhMFpk5M1WI_0wQNO

**A Merge multiple PDF into one New PDF file**
"""

!pip install PyPDF2
from PyPDF2 import PdfWriter, PdfReader
num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('/content/drive/MyDrive/Python lab Manual.pdf', 'rb')
pdf2 = open('/content/drive/MyDrive/Python skill enhancementprogram.pdf', 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)
with open('output.pdf', 'wb') as output:
     pdf_writer.write(output)

"""**Fetch Weather Data from JSON**"""

import json

def fetch_weather_data_from_json(file_path):
    try:
        with open(file_path, "r") as json_file:
            weather_data = json.load(json_file)
            return weather_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in the file: {file_path}")
    except Exception as e:
        print(f"Error occurred while reading the JSON file: {e}")
    return None

if __name__ == "__main__":
    file_path = "/content/drive/MyDrive/weather.json"
    weather = fetch_weather_data_from_json(file_path)

    if weather:
        print("Current Weather Data:")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['conditions']}")
    else:
        print("Failed to fetch weather data from the JSON file.")



from google.colab import drive
drive.mount('/content/drive')

