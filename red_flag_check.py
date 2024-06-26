import test_reports
from openai import OpenAI

def get_assistant_response(report):
    client = OpenAI()
    
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=report
    )
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id="asst_BLDpQeApl9O0OrfydnVc4wdm",
    )
    
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        if messages.data:
            first_message = messages.data[0]
            return first_message.content[0].text.value
    
    return run.status

# Example usage:
# response = get_assistant_response(test_reports.JAMES_REPORT)
# print(response)
