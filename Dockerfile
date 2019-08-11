FROM python:3.6
RUN pip3 install bs4
RUN pip3 install lxml
RUN pip3 install requests
COPY QisDataScraper.py .
COPY grades.txt .
CMD ["python3", "QisDataScraper.py"]
