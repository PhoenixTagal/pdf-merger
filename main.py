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


test_vars = {'bothell_2023_q2_dir': r"C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\Bothell\2023\Q2",
             'bothell_2023': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\Bothell\2023',
             '1165_2023': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1165\2023',
             '1551_2023': r'C:\Users\ptagal\OneDrive - Adaptive Biotechnologies\Environmental Health and Safety\500 Environmental\510 Regulated Waste Management\Hazardous Waste\Inspection Forms\Eyewash & Shower Inspections\1551\2023'}


def make_list_of_file_paths(directory_path):
    """
    :param directory_path: arg data type = rawstring (ex: r"path\to\directory")
    :return: list of file pathways for every file in the directory passed into function
    """
    directory = directory_path
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    return file_paths


def merge_pdfs(input_paths, output_path):
    """
    :param input_paths: pass the output of make_list_of_file_paths()
    :param output_path: arg datatype = str or rawstring if you want to save to specific directory
    :return: a new pdf file consisting of all merged pdfs from delcared directory (ex: fr"{test_vars['1551_2023']}\Q2\Q2 Eyewash and Shower Inspections.pdf")
    """
    pdf_merger = PyPDF2.PdfMerger()

    for path in input_paths:
        with open(path, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)


file_path = fr"{test_vars['1551_2023']}\Q2"

merge_pdfs(input_paths=make_list_of_file_paths(file_path), output_path=fr"{file_path}\Q2 1551 Eyewash and Shower Inspections.pdf")

