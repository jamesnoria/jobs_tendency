# Python libraries
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re
import time
from pathlib import Path

# Local libraries
from data import Data
from data_visualization import DataVisualization


def getting_links():
    """
    Getting all the pages(urls) from the site with a loop
    """
    page = 0
    urls = []
    while page < 12:
        page += 1
        link = f'https://www.computrabajo.com.pe/trabajo-de-programador?p={page}&q=programador'
        urls.append(link)

    return urls


def getting_jobs_info(urls):
    """
    Getting url from every job
    """
    job_links = []
    for url in urls:
        link = get(url)
        soup = BeautifulSoup(link.content, 'lxml')
        finder = soup.find_all(class_='js-o-link')
        for i in finder:
            job_links.append('https://www.computrabajo.com.pe' + i['href'])

    return job_links


def text_scraper(urls):
    """
    Getting the text from every url
    """
    # Format for the new folder:
    folder_base = 'jobs_' + time.strftime('%d_%m_%Y')
    folder_reports = 'reports_' + time.strftime('%d_%m_%Y')
    Path(folder_base).mkdir(exist_ok=True)
    Path(folder_reports).mkdir(exist_ok=True)
    # Saving each job in a file:
    job_counter = 0
    while job_counter < len(urls):
        for url in urls:
            page = get(url)
            soup = BeautifulSoup(page.content, 'lxml')
            finder = soup.find(class_='cm-12 box_i bWord')
            job_counter += 1
            filename = f'./{folder_base}/job_{job_counter}.txt'
            with open(filename, 'w+') as opened_file:
                opened_file.write(finder.ul.text)


def regex_finder(lang, regex):
    """
    Apply all regex to individual text files
    """
    folder_base = 'jobs_' + time.strftime('%d_%m_%Y')
    job_counter = 0
    lang = []
    while job_counter < 240:
        job_counter += 1
        filename = f'./{folder_base}/job_{job_counter}.txt'
        with open(filename, 'r') as opened_file:
            match = re.search(regex, opened_file.read())
            if match:
                lang.append(1)

    return sum(lang)


def get_dataframe(data, name):
    """
    Getting a dataframe from all jobs and numbers
    and generate a data visualization for each of them
    """
    folder_reports = 'reports_' + time.strftime('%d_%m_%Y')
    numbers, names = [], []
    for key, value in data.items():
        names.append(key)
        numbers.append(regex_finder(key, value))

        # Generating a dataframe with a .csv file as an output
        df = pd.DataFrame({
            'Technology': [name for name in names],
            'Numbers': [number for number in numbers]
        })

        df.to_csv(f'./{folder_reports}/{name}.csv')

        # Generating data visualization with DATA VISUALIZATION local library
        data_visualization = DataVisualization(folder_reports, name)
        data_visualization.data_show()


if __name__ == '__main__':

    # This code below allows the request to computrabajo.com to get all urls and data from every job.
    # This generate a folder with all the info inside of it.
    text_scraper(getting_jobs_info(getting_links()))

    # .csv files and data visualization
    jobs_data = Data()
    get_dataframe(jobs_data.programming_languages(), 'programming_languages')
    get_dataframe(jobs_data.frameworks(), 'frameworks')
    get_dataframe(jobs_data.complements(), 'complements')
    get_dataframe(jobs_data.data_bases(), 'data_bases')
    get_dataframe(jobs_data.cloud(), 'cloud')
