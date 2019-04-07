import json
from watson_developer_cloud import VisualRecognitionV3, \
    WatsonApiException

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='dIfnxtt6Ve-X8TJk88-vuOgG1xe07gGROCJtrh0JRrrY')

with open('C:/Users/ofirh/PycharmProjects/almog/positive.zip', 'rb') as positive, \
     open('C:/Users/ofirh/PycharmProjects/almog/negative.zip', 'rb') as negative:
    try:
        response = visual_recognition.create_classifier(
            'ofir',
            ofir_positive_examples=positive,
            negative_examples=negative).get_result()
        print(json.dumps(response, indent=2))
    except WatsonApiException as ex:
        print("Status code: {}\nError message: {}\nError info: \n{}" \
            .format(ex.code, ex.message, json.dumps(ex.info, indent=1)))