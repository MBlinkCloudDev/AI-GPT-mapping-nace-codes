# AI-GPT-mapping-nace-codes
This script uses OpenAI's API to create a table of NACE codes out of the official PDF.



# possible improvements
- check if model actually reads the PDF in the system-prompt (if not, then parse, and provide as text)
- shorten the PDF (that only the tables are read by the model)
- set the temperature to low level (e.g. 0.3), so that model is less random, and more deterministic
- build check/test, so that codes and sections are mapped correctly (e.g. compare the input with the output code)
- write values to database (in each iteration), and put try and except, to make the code more stable
