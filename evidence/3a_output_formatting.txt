"""Detect emotions with the Watson NLP service."""
import requests

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion."""
    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        timeout=30,
    )
    if response.status_code == 400:
        return dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {name: emotions[name] for name in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
