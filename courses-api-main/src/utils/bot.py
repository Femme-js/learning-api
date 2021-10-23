import os
import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument

DIALOGFLOW_PROJECT_ID = "financewiz18"
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

def bot(text):
    text_to_be_analyzed = text

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    
    reply =  response.query_result.fulfillment_text
    return reply