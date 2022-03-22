import urllib.request
import re
import extractor

CLEAN_TAGS = re.compile('<.*?>')
CLEAN_PUNCTUATION = re.compile('[^a-zA-Z\s\d]')
CLEAN_SPACES = re.compile('\s+')

URL = "https://raw.githubusercontent.com/davidsbatista/Annotated-Semantic-Relationships-Datasets/master/datasets/hlt-naacl08-data.txt"

def clean_sentence(raw_string):
  without_tags = re.sub(CLEAN_TAGS, '', raw_string)
  without_punctuation = re.sub(CLEAN_PUNCTUATION, '', without_tags)
  cleaned_spaces = re.sub(CLEAN_SPACES, ' ', without_punctuation)
  return cleaned_spaces.strip()

data = urllib.request.urlopen(URL)
for line in data:
    sent = clean_sentence(line.decode())
    print("="*50)
    print(sent)
    extractor.proccess_sentence(sent)
    print("="*50)