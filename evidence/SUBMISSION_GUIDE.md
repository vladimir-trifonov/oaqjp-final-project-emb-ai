# Submission answers

Questions 2, 4, 8, 10, 12, 13, 15: paste the corresponding numbered .txt file in this folder. These contain the final implementation.

Question 16: paste 8b_static_code_analysis.txt (actual local score: 10.00/10).

Questions 1 and 6: after publishing the prepared changes to your fork main branch, use:

- Question 1: https://github.com/vladimir-trifonov/oaqjp-final-project-emb-ai/blob/main/README.md
- Question 6: https://github.com/vladimir-trifonov/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

Use these links after the project changes are published to main.

Questions 3, 5, 7, 9: require real Watson service output. Run these in the IBM lab from /home/project/final_project; do not replace your actual path in local output.

```sh
python3
from emotion_detection import emotion_detector
print(emotion_detector('I am really mad about this'))
exit()
python3 test_emotion_detection.py
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

Save the actual output under the rubric names 2b_application_creation, 3b_formatted_output_test, 4b_packaging_test, and 5b_unit_testing_result.

Questions 11 and 14: run python3 server.py in the lab, open the app, analyze a sentence and capture 6b_deployment_test.png. Clear the input and analyze again; capture 7c_error_handling_interface.png. Screenshots have not been generated locally.
