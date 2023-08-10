"""
merging PDF's for batch quarterly upload of eyewash/inspection forms into QMS system.

Quarterly Breakdown:
Q1: 1 JAN - 31 MAR
Q2: 1 APR - 30 JUN
Q3: 1 JUL - 30 SEP
Q4: 1 OCT - 31 DEC
"""

import os
import PyPDF2


test_vars = {'bothell_2023_q2_dir': r"C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q2"}


def make_list_of_file_paths(directory_path):
    """
    :param directory_path: argument data type = rawstring (ex: r"path\to\directory")
    :return: list of file pathways for every file in the directory passed into function
    """
    directory = directory_path
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    return file_paths


