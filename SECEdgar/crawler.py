# -*- coding:utf-8 -*-
# This script will download all the 10-K, 10-Q and 8-K
# provided that of company symbol and its cik code.

import requests
import os
import errno
from bs4 import BeautifulSoup
from config import DEFAULT_DATA_PATH


class SecCrawler():

    def __init__(self):
        self.hello = "Welcome to Sec Cralwer!"
        print("Path of the directory where data will be saved: " + DEFAULT_DATA_PATH)

    def make_directory(self, company_code):
        # Making the directory to save comapny filings
        path = DEFAULT_DATA_PATH

        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise

    def save_in_directory(self, company_code, doc_list, doc_name_list):
        # Save every text document into its respective folder
        for j in range(len(doc_list)):
            base_url = doc_list[j]
            r = requests.get(base_url)
            data = r.text
            path = os.path.join(DEFAULT_DATA_PATH, doc_name_list[j])

            with open(path, "a+") as f:
                f.write(data.encode('ascii', 'ignore'))


    def filing_10K(self, company_code, priorto, count):

        self.make_directory(company_code)

        # generate the url to crawl
        base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(company_code)+"&type=10-K&dateb="+str(priorto)+"&owner=exclude&output=xml&count="+str(count)
        print ("started 10-K " + str(company_code))

        r = requests.get(base_url)
        data = r.text

        # get doc list data
        doc_list, doc_name_list = self.create_document_list(data)

        try:
            self.save_in_directory(company_code, doc_list, doc_name_list)
        except Exception,e:
            print str(e)

        print "Successfully downloaded all the files"

    def create_document_list(self, data):
        # parse fetched data using beatifulsoup
        soup = BeautifulSoup(data)
        # store the link in the list
        link_list = list()

        # If the link is .htm convert it to .html
        for link in soup.find_all('filinghref')[: count - 1]:
            url = link.string
            if link.string.split(".")[len(link.string.split("."))-1] == "htm":
                url += "l"
            link_list.append(url)
        link_list_final = link_list

        print ("Number of files to download {0}".format(len(link_list_final)))
        print ("Starting download....")

        # List of url to the text documents
        doc_list = list()
        # List of document names
        doc_name_list = list()

        # Get all the doc
        for k in range(len(link_list_final)):
            required_url = link_list_final[k].replace('-index.html', '')
            txtdoc = required_url + ".txt"
            docname = txtdoc.split("/")[-1]
            doc_list.append(txtdoc)
            doc_name_list.append(docname)
        return doc_list, doc_name_list

