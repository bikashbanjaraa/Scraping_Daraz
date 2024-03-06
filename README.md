GitHub Actions Setup for Scrapy Spider
Overview:

This repository contains a Scrapy spider (daraz) set up to scrape data from the Daraz website, and a GitHub Actions workflow (main.yml) that runs the spider every 2 hours and pushes the scraped data into an SQLite database.
Setup Steps:

Scrapy Spider (daraz):
      The Scrapy spider (daraz) is configured to scrape product information from the Daraz website.
      The spider extracts data such as product URL, image URL, name, rating, price, and number of items sold of page ankle shoes and watch section.

SQLite Pipeline (pipelines.py):
      The repository includes an SQLite pipeline (pipelines.py) that inserts the scraped data into an SQLite database (scrapy_items.db).
      Table name is items. so, we can search with query 'select * from items'.
      The SQLitePipeline class handles the opening and closing of the database connection and the insertion of items into the items table.

GitHub Actions Workflow (main.yml):
        The .github/workflows directory contains a GitHub Actions workflow file (scrapy.yml).
        The workflow is set to run on a schedule every 2 hours (0 */2 * * *) and allows for manual triggering.
        Steps in the workflow:
            Checks out the repository.
            Sets up Python environment.
            Installs necessary dependencies (scrapy and scrapy-playwright).
            Runs the Scrapy spider (scrapy crawl daraz).
            Pushes the scraped data into the SQLite database by running the pipelines.py script.

How to Use:

Run the Scrapy Spider Manually:
        we can manually trigger the workflow by going to the "Actions" tab in the repository, selecting "Scrapy Spider", and clicking "Run workflow".

  Check Workflow Status:
        Navigate to the "Actions" tab in the repository to view the status of the workflow runs.
        The status will indicate whether the spider ran successfully and pushed data into the database.

  View Database:
        The scrapy_items.db SQLite database will contain the scraped data in a table named items.
        we can view the contents of the table using ' https://inloop.github.io/sqlite-viewer/'
