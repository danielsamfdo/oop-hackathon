import requests
from llama_parse import LlamaParse

LLM_MODELS = {}

LLM_MODELS['openai'] = {}
LLM_MODELS['llamaindex'] = {
    'key' : "",
}


def store_data(url, file_name):
    with open(file_name, 'wb') as out_file:
        content = requests.get(url, stream=True).content
        out_file.write(content)
    print(content)

def store_extracted_info(content, file_name):
    with open(file_name, 'w') as out_file:
        out_file.write(content)


def sync_extract_report_from_pdf(data_file_name, output_format="markdown", options = {"model": "llamaindex"}):
    """
        Extracting the report from pdf into a specified output format.

        Args:
        data: Bytes of the data that are in the PDF.
        output_format: Data format of the output.
        options: Parameters that can be configurable for the extraction report.
    """
    # bring in deps

    parser = LlamaParse(
        api_key=LLM_MODELS[options['model']]['key'],  # can also be set in your env as LLAMA_CLOUD_API_KEY
        result_type=output_format  # "markdown" and "text" are available
    )

    documents = parser.load_data(data_file_name)
    return documents[0].text

