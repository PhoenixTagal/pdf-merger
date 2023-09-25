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

destination_true_north_inspection_directories = {'1551_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q3',
                                                 '1551_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\1551\2023\Q4',
                                                 '1165_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q3',
                                                 '1165_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\1165\2023\Q4',
                                                 'bothell_2023_q3': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q3',
                                                 'bothell_2023_q4': r'C:\Users\ptagal\Adaptive Biotechnologies\Environmental Health and Safety - Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q4'}


source_directory_values = source_directories.values()
destination_directory_values = destination_true_north_inspection_directories.values()




# for i in source_directory_values:
#     print(i)
#
# for directory in source_directory_values:
#     for filename in os.listdir(directory):
#         if filename.endswith(".pdf"):  # Check if the file is a PDF
#             source_path = os.path.join(directory, filename)
#             destination_path = os.path.join(destination_directory, filename)
#             shutil.copy2(source_path, destination_path)
