import extract_pdf
import models
import diagnose_prompt
import care_plan_prompt
import test_reports
import stats_finder

PROVIDER_ASSISTANT_PROMPT = """
Use the following information to help a provider write a portal message to a patient that helps them understand a recent radiology report and what options are available for care.

# Diagnosis
{diagnosis}

# Care Plan
{care_plan}

Instructions:
- Please be empathetic and friendly in your disposition and explain things in simple terminology.
- The goal of this message is to alleviate concerns, explain findings and set up the discussion in the follow-up visit so that the provider and patient can use shared decision to determine the next steps in treatment.
"""

def provider_assist(care_plan, diagnosis):
    return models.call_openai(PROVIDER_ASSISTANT_PROMPT.format(diagnosis=diagnosis, care_plan=care_plan)).choices[0].message.content


def care_plan(report=test_reports.JAMES_REPORT):
    with open('acp_guidelines.md', 'r') as out_file:
        context = out_file.read()
    return models.call_openai(care_plan_prompt.CARE_PLAN_PROMPT.format(context=context, report=report)).choices[0].message.content

def summary_diagnosis(report=test_reports.JAMES_REPORT):
    with open('ajnr.md', 'r') as out_file:
        context = out_file.read()
    return models.call_openai(diagnose_prompt.DIAGNOSE_PROMPT.format(context=context, report=report)).choices[0].message.content

def summary_age(report=test_reports.JAMES_REPORT):
    return stats_finder.stat_finder(report=report)

def fetch_patient_age():
    return 65

def summary(diagnosis_summary, stats_diagnosis_age):
    return f"{diagnosis_summary} \n\n\n\n {stats_diagnosis_age}"

def main(): 
    print("hey there")
    care = care_plan()
    diagnosis = summary_diagnosis()
    response = provider_assist(care, diagnosis)
    print("CARE*******\n\n\n\n\n")
    print(care)
    print("DIAGNOSIS*******\n\n\n\n\n")
    print(diagnosis)
    print("PROVIDER_ASSISTANT_RESPONSE*******\n\n\n\n\n")
    print(response)
    # print(summary(summary_diagnosis(), summary_age()))
    # print(models.call_openai(diagnose_prompt.DIAGNOSE_PROMPT.format(context="", report=test_reports.REPORT)).choices[0].message.content)
    # print(stats_finder.stat_finder_age(test_reports.JAMES_REPORT))


# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main()
    response = extract_pdf.sync_extract_report_from_pdf('red_flags.pdf')
    extract_pdf.store_extracted_info(response, 'red_flags.md')
    print(f'Extraction response: {response}')
