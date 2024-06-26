import requests
import json
import time
import os

url = "https://fumage-jamesleonard-oophackathon.canvasmedical.com/DiagnosticReport?patient=0aabd3daaafc4880932b917624defbfa"
headers = {
    "Authorization": "Bearer v8rGupHrkWCUUAGmBWzWsCiF9zNKlk",
    "accept": "application/json"
}

is_download_complete = False

def download_pdf(url_string):
    global is_download_complete
    try:
        response = requests.get(url_string)
        response.raise_for_status()
        
        documents_path = os.path.expanduser("~/Documents")
        destination_path = os.path.join(documents_path, "downloaded_report.pdf")
        
        with open(destination_path, "wb") as file:
            file.write(response.content)
        
        print(f"PDF downloaded successfully. Saved at: {destination_path}")
        is_download_complete = True
    except requests.RequestException as e:
        print(f"Download error: {str(e)}")
    except IOError as e:
        print(f"Error saving PDF: {str(e)}")

def perform_request():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        entry_array = data.get("entry", [])
        if entry_array:
            resource = entry_array[0].get("resource", {})
            presented_form = resource.get("presentedForm", [])
            if presented_form:
                pdf_url = presented_form[0].get("url")
                if pdf_url:
                    print(f"URL found: {pdf_url}")
                    download_pdf(pdf_url)
                    return
        
        print("Failed to find the URL in the JSON response")
    except requests.RequestException as e:
        print(f"Error: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {str(e)}")

retry_interval = 5  # Retry every 5 seconds
while not is_download_complete:
    perform_request()
    if not is_download_complete:
        print(f"Download not successful. Retrying in {retry_interval} seconds...")
        time.sleep(retry_interval)