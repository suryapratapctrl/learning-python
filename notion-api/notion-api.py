#imports
import requests
import json
from datetime import datetime

# get notion api key and database id
from dotenv import load_dotenv
import os

load_dotenv()

notion_api_key = os.getenv("notion_api_key")

db_id = os.getenv("db_id")

#define content for notion page
page_name='test page 02'
today=datetime.now().isoformat() # notion needs ISO format
content="""#HEADING 1
##HEADING 2
###HEADING 3
# Here is a regular paragraph
# we can use **bold**,*italic*, or ***bold italic*** text"""

#define content blocks for the page
children_blocks=[]
#SETUP HEADER FOR NOTION API REQUEST
headers={
  'Authorization':'Bearer '+ notion_api_key,
    'Content-type':'application/json',
    "Notion-Version":'2022-06-28'
}

#setup data for notion api request
data={
  'parent':{'database_id':db_id},
  'childern':children_blocks,
  'properties':{
    'Name':{
      'title':[
        {'text':{'content':page_name}}
      ]
    },
    "Date":{
      "date":{
        'start':today
      }
    }
  },
}

#send post request
response=requests.post(
  "https://api.notion.com/v1/pages",
  headers=headers,
  data=json.dumps(data)
)

#verify status
if response.status_code==200:
  print('page is created successfully!')
  print('page id:',response.json()['id'])
else:
  print('failed to create page')
  print(response.status_code,response.text)  