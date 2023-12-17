#python-dotenv : Helps to load local environmental files storing API KEYS IN specific file that is Hidden
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv() 
api_key=os.getenv("OPENAI_API_KEY")

model=ChatOpenAI(openai_api_key=api_key) #Interface Component 
#Makes Connection to the gpt

template="You need to convert {input_language} to {output_langauge}."
human_template="{text}"

chat_prompt=ChatPromptTemplate.from_messages([
    ("system",template),
    ("human",human_template),
])

mess=chat_prompt.format_messages(input_language="English",
                                 output_langauge="Spanish",
                                 text="I love Development")
res=model.predict_messages(mess)
print(res.content)      