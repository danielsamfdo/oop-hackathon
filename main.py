import extract_pdf
import models
import diagnose_prompt
import care_plan_prompt
import test_reports
import stats_finder
import red_flag_check
import send_to_ehr
import requests
import json
import time
import os

PROVIDER_ASSISTANT_PROMPT = """
Use the following information to help a provider write a portal message to a patient that helps them understand a recent radiology report and what options are available for care.

# Diagnosis
{diagnosis}

# Care Plan
{care_plan}

Instructions:
- Please be empathetic and friendly in your disposition and explain things in simple terminology.
- The goal of this message is to alleviate concerns, explain findings and set up the discussion in the follow-up visit so that the provider and patient can use shared decision to determine the next steps in treatment.

Format in plain text, with no emphasis markings, for example (* or _) used in your output.
"""

def provider_assist(care_plan, diagnosis):
    provider_assist_prompt = PROVIDER_ASSISTANT_PROMPT.format(diagnosis=diagnosis, care_plan=care_plan)
    print("PROVIDER_ASSISTANT_PROMPT*******\n\n\n\n\n")
    # print(provider_assist_prompt)
    return models.call_openai(provider_assist_prompt).choices[0].message.content


def care_plan(report=test_reports.JAMES_REPORT):
    with open('acp_guidelines.md', 'r') as out_file:
        context = out_file.read()
    care_plan_promptt = care_plan_prompt.CARE_PLAN_PROMPT.format(context=context, report=report)
    # print("CAREPLANPROMPT*******\n\n\n\n\n")
    # print(care_plan_promptt)
    return models.call_openai(care_plan_promptt).choices[0].message.content

def summary_diagnosis(report=test_reports.JAMES_REPORT):
    with open('ajnr.md', 'r') as out_file:
        context = out_file.read()
    diagnosis_promptt = diagnose_prompt.DIAGNOSE_PROMPT.format(context=context, report=report)
    # print("DIAGNOSISPROMPT*******\n\n\n\n\n")
    # print(diagnosis_promptt)
    return models.call_openai(diagnosis_promptt).choices[0].message.content

def summary_age(report=test_reports.JAMES_REPORT):
    return stats_finder.stat_finder(report=report)

def fetch_patient_age():
    return 65

def summary(diagnosis_summary, stats_diagnosis_age):
    return f"{diagnosis_summary} \n\n\n\n {stats_diagnosis_age}"

def download_pdf(url_string):
    try:
        response = requests.get(url_string)
        response.raise_for_status()
        
        documents_path = os.path.expanduser("~/Documents")
        destination_path = os.path.join(documents_path, "downloaded_report.pdf")
        
        with open(destination_path, "wb") as file:
            file.write(response.content)
        
        print(f"Document pulled successfully")
        return True
    except requests.RequestException as e:
        print(f"Download error: {str(e)}")
    except IOError as e:
        print(f"Error saving PDF: {str(e)}")
    return False

def poll_and_download_file():
    url = "https://fumage-jamesleonard-oophackathon.canvasmedical.com/DiagnosticReport?patient=0aabd3daaafc4880932b917624defbfa"
    headers = {
        "Authorization": "Bearer v8rGupHrkWCUUAGmBWzWsCiF9zNKlk",
        "accept": "application/json"
    }
    retry_interval = 5  # Retry every 5 seconds

    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            # print(data)
            
            entry_array = data.get("entry", [])
            if entry_array:
                resource = entry_array[0].get("resource", {})
                presented_form = resource.get("presentedForm", [])
                if presented_form:
                    pdf_url = presented_form[0].get("url")
                    if pdf_url:
                        print(f"URL found: {pdf_url}")
                        if download_pdf(pdf_url):
                            return True
        except requests.RequestException as e:
            print(f"Error: {str(e)}")
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {str(e)}")
        
        print(f"Download not successful. Retrying in {retry_interval} seconds...")
        time.sleep(retry_interval)

def main(): 
    # First, poll and download the file
    if poll_and_download_file():
        # Use red_flag_check to check for red flags
        result_of_red_flag = red_flag_check.get_assistant_response(test_reports.JAMES_REPORT)
        # If result_of_red_flag is 'HUMAN' then print the result_of_red_flag and exit
        if result_of_red_flag == 'HUMAN':
            print("EXITING EARLY*******\n\n\n\n\n")
            print(result_of_red_flag)
            return

        care = care_plan()
        print("CARE*******\n\n\n\n\n")
        print(care)
        diagnosis = summary_diagnosis()
        print("DIAGNOSIS*******\n\n\n\n\n")
        print(diagnosis)
        response = provider_assist(care, diagnosis)
        print("PROVIDER_ASSISTANT_RESPONSE*******\n\n\n\n\n")
        print(response)
        send_to_ehr.send_to_ehr(response)


if __name__=="__main__": 
    main()
