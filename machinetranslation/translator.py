import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['Zq3eAFzPschKXEuWKizD2HrB-WzKChj-pdhVmStwWaAD']
#url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/103ec3d6-72d7-4070-8602-7387e3146d01']
authenticator = IAMAuthenticator('Zq3eAFzPschKXEuWKizD2HrB-WzKChj-pdhVmStwWaAD')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
def english_to_french(english_text):
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/103ec3d6-72d7-4070-8602-7387e3146d01')
    translation = language_translator.translate(
        text='Hello, how are you today?',
        model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    english_text= translation['translations'][0]['translation']

    return english_text
english_to_french('Hello')
def french_to_english(french_text):
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/103ec3d6-72d7-4070-8602-7387e3146d01')
    translation = language_translator.translate(
        text='Bonjour',
        model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    french_text= translation['translations'][0]['translation']

    return french_text
print(english_to_french(''))
print(french_to_english('Bonjour'))
