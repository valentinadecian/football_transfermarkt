from llama_cpp import Llama
from IPython.display import display, Markdown

llm = Llama(model_path="C:/Users/valen/Downloads/Llama-3.2-3B-Instruct-Q4_K_M.gguf")

# Ask Llama some ideas to make data analysis with our dataset

system_message = """You are a data analysis expert. You are very concise and effective."""
user_message = """I have a dataset containing information about transfers of football players among various seasons. The dataset has a tabular format, it contains 79646 records and 10 columns. The columns are:
- player_id: unique id
- transfer_date: date of the transfer
- transfer_season: season of the transfer
- from_club_id: id of the football club the player is transferred from
- to_club_id: id of the football club the player is transferred to
- from_club_name: name of the football club the player is transferred from
- to_club_name: name of the football club the player i transferred to
- transfer_fee: amount of money the arrival club payed to the departure club for buying the player (contains many nulls)
- market_value_in_eur: actual market value of the player (contains many nulls)
- player_name: name of the player

Can you suggest 3 interesting questions about this dataset that could be answered through data analysis? Tell me only the questions, don't tell me how to do the jobs.
"""

messages = [{'role' : 'system', 'content' : system_message}, {'role' : 'user', 'content' : user_message}]
response = llm.create_chat_completion(messages=messages, temperature=0.2)
response_content = response['choices'][0]['message']['content']

with open('results/other/llama_suggestions.txt', 'w') as file:
    file.write(response_content)