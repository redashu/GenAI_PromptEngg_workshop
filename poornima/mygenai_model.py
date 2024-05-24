import google.generativeai as genai 
from google.colab import userdata
myai_cred=userdata.get('GOOGLE_API_KEY')
print(myai_cred)

# lets authenitcate google gemini using above cred 
for i in dir(genai):
  if 'conf' in i:
    print(i)
# single line
#[i for i in dir(genai) if 'conf' in i ]
genai.configure(api_key=myai_cred)
# printing supported models
for j in genai.list_models():
  if 'generateContent' in j.supported_generation_methods:
    print(j.name)
# selecting particular model 
ashuai_model=genai.GenerativeModel('gemini-1.5-flash-latest')
# lets take input from user 
my_prompt=input("Enter your Prompt Here...>>> ")
# now supply prompt to ashuai_model to generate new content 
ashuai_response=ashuai_model.generate_content(my_prompt)
print(ashuai_response.text)
# converting markdwon into human readable text
from IPython.display import  Markdown
import textwrap
# creating a markdwon to text function 
def my_mark_to_text(mytext):
  mytext = mytext.replace('.','*')
  return Markdown(textwrap.indent(mytext,'>',predicate=lambda _: True))
# calling function to convert markdown into human text
print("@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@___________________@@")
print("Please wait we are converting and printing back ")
my_mark_to_text(ashuai_response.text)