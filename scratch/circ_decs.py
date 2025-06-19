#%%
from utils import get_simple_client

client = get_simple_client()

#%%
system_prompt = (
    "You are a helpful assistant that reviews the biography of a historical figure "
    "and summarizes their life and acts by tracing the major decisions they made.")

message_template = (
    "Below is a biography of Byzantine Emperor {0}. Extract and number the major decisions {0} made in chronological order. "
    "Describe each decision using three bullet points: "
    "the circumstances that led to it, the decision made by {0}, and the consequences.\n\n{1}"
)

person_name = "Basil II"
path_biogrpahy = "bio-basil ii.txt"
path_circ_desc = "circ decs-basil ii.txt"

with open(path_biogrpahy) as fin:
    bio = fin.read().split("\n")
    bio = "\n".join(s.strip() for s in bio)
    message = message_template.format(person_name, bio)

#%%
content = client(
    system_prompt=system_prompt, 
    message=message, 
    temperature=1.0, 
    max_tokens=3000
    )
with open(path_circ_desc, "w") as fout:
    fout.write(content)

#%%
