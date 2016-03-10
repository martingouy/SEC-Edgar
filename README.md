SEC-Edgar-Crawler
=============

 Getting filings of various comapanies at once is really a pain but SEC-Edgar-Crawler does that for you.
 you can Download all companies  periodic reports, filings and forms from EDGAR database in a single command.

Installation
------------- 
 You may have to install the package using pip.
 ```bash
 $ pip install git+https://github.com/martingouy/SEC-Edgar
 ```

Runing
-------
 
 Now to run it start python shell
   ```bash
  >>> from SECEdgar.crawler import SecCrawler
  >>> secCrawler = SecCrawler()
  >>> secCrawler.filing_10K('AAPL', '20010101', '10')
   ```
 This will download the AAPL company's last 10 10-K filings since January 2001