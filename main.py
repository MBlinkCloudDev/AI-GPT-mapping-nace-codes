import json
from openai import OpenAI
import pandas as pd


SYSTEM_PROMPT_PATH = 'system_prompt_lksg.txt'
with open(SYSTEM_PROMPT_PATH, 'r', encoding='utf-8') as file:
    system_prompt = file.read()



project_api_key = ""   <------------------------ (add your OpenAI API-key here)
MODEL = "gpt-4-1106-preview"

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=project_api_key)



file = "nace-code-mapping.xlsx"
df = pd.read_excel(file, dtype={'NACE Class Code': str})
nace_codes = list(df["NACE Class Code"])


numberCodes = len(nace_codes)
d_list = []

print(f"Starting mapping of {numberCodes} categories.")
for i in range(numberCodes):

    #user_prompt = "How are NACE codes structured? Do they have a hierarchy? If so, what is the hierarchy of the NACE code '49.42' and '74.20'?"
    user_prompt = f"What is the hierarchical structure for the NACE code '{nace_codes[i]}'?"
    print(user_prompt)

    response = client.chat.completions.create(
      model=MODEL,
      response_format={ "type": "json_object" },
      max_tokens= 600,
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
      ]
    )
    result = json.loads(response.choices[0].message.content)
    print(result)
    d_list.append(result)

d_combined = {
    "Section Code": [d['Section Code'] for d in d_list],
    "Section Name": [d['Section Name'] for d in d_list],
    "Division Code": [d['Division Code'] for d in d_list],
    "Division Name": [d['Division Name'] for d in d_list],
    "Group Code": [d['Group Code'] for d in d_list],
    "Group Name": [d['Group Name'] for d in d_list],
    "Class Code": [d['Class Code'] for d in d_list],
    "Class Name": [d['Class Name'] for d in d_list],
}
df = pd.DataFrame(data=d_combined)
df.to_excel("naces6.xlsx")
