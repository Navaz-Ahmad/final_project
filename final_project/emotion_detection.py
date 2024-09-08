import requests

# Define the emotion detection function
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Sending the request to Watson NLP API
    response = requests.post(url, json=input_json, headers=headers)

    # Ensure the response is successful
    if response.status_code == 200:
        # Extract and return the emotion analysis result
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"
