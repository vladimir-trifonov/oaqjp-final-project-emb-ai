"""Live Watson service tests; run inside the IBM course lab."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check the five required dominant emotions."""

    def test_emotions(self):
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(emotion_detector(text)["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
