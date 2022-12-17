
import requests
from bs4 import BeautifulSoup

job_titlse1 = []
locations_names1 = []
company_name1 = []
time_job1 = []
page_num=0
while True:
    if(page_num>975) :
        break
    result=requests.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3392551106&geoId=92000000&keywords=Python%20(Programming%20Language)&location=Worldwide25&start={page_num}")
    src=result.content
    soup=BeautifulSoup(src,"html.parser")

    job_titlse=soup.find_all("h3",{"class":"base-search-card__title"})
    locations_names=soup.find_all("span",({"class":"job-search-card__location"}))
    company_name=soup.find_all("a",({"class":"hidden-nested-link"}))
    time_job=soup.find_all("time")


    for i in range(len(job_titlse)):
        job_titlse1.append(job_titlse[i].text.strip())
        locations_names1.append(locations_names[i].text.strip())
        company_name1.append(company_name[i].text.strip())
        time_job1.append(time_job[i].text.strip())

    page_num+=25

for i in range(len(job_titlse)):
    print(f'{job_titlse1[i]},,,{locations_names1[i]},,,{company_name1[i]},,,{time_job1[i]}\n')





