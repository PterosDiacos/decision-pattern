#%%
from utils import get_simple_client

client = get_simple_client()

#%%
system_prompt = (
    "You are a helpful assistant that reviews an anonymized biography "
    "and aims identify the historical figure in question.")

message_template = (
    "Below is an anonymized summary of the major decisions made by a Byzantine Emperor. "
    "Bassed on the course of events, identify the figure by name.\n\n{0}"
)

path_anonymized = "v0.1/anonymized-basil ii.txt"
with open(path_anonymized) as fin:
    anonymized_desc = fin.read()
    message = message_template.format(anonymized_desc)

content = client(
    system_prompt=system_prompt,
    message=message,
    temperature=1.0,
    max_tokens=2048)


#%%
