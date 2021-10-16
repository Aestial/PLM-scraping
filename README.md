# PLM scraping

Data scraping solution for the [PLM webpage](https://www.medicamentosplm.com) using Python 3.9 and Scrapy 2.4

## Install

1. (Optional) Create a virtual environment in the *.venv* hidden directory:
        
        python -m venv .venv
2. Install dependencies:

        pip install -r requirements.txt


## How to use

1. Run the spider crawl:

        scrapy crawl {spider} -o {output_file}.jl


## Helper scripts

1. **sort.py** : Generates a *jsonlines* file with the data of the input *.jl* file sorted by the specified field.

        python sort.py {input_file}.jl {output_file}.jl {field}

        