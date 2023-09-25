"""
This script copys saved eye/wash and shower inspections from the ehs facilities onedrive shortcut directory to the directory linked to the EHS truenorth site.
"""

import shutil
import os

source_directories = {'1551_2023_q3': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q3',
                      '1551_2023_q4': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q4',
                      '1165_2023_q3': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q3',
                      '1165_2023_q4': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q4',
                      'bothell_2023_q3': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q3',
                      'bothell_2023_q4': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q4'}

destination_true_north_inspection_directories = {'1551_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q3',
                                                 '1551_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q4',
                                                 '1165_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q3',
                                                 '1165_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q4',
                                                 'bothell_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q3',
                                                 'bothell_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health & Safety - Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q4'}


source_directory_values = source_directories.values()
destination_directory_values = destination_true_north_inspection_directories.values()

for source_dir, destination_dir in zip(source_directory_values, destination_directory_values):
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_dir, os.path.relpath(source_path, source_dir))

            # Check if the file already exists in the destination directory
            if not os.path.exists(destination_path):
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy2(source_path, destination_path)
                print(f"File '{file}' copied to '{destination_dir}'")
            else:
                print(f"File '{file}' already exists in '{destination_dir}' and was skipped")

print("File copying o EHS TrueNorth sharepoint site directory completed.")

