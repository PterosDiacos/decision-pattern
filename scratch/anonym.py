#%%
from utils import get_simple_client

client = get_simple_client()

#%%
system_prompt = (
    "You are a helpful assistant that reviews the biography of a historical figure "
    "and removes personal identifying information .")

message_template = (
    "Below is a summary of the major decisions made by Byzantine Emperor {0} "
    "Rewrite this summary by replacing any specific personal, occupational, temporal, or geographical terms "
    "with vague or generic terms.\n\n{1}"
)

person_name = "Michael IV"
path_circ_desc = "v0.1/circ decs-michael iv.txt"
path_anonymized = "v0.1/anonymized-michael iv.txt"

with open(path_circ_desc) as fin:
    circ_desc = fin.read()
    message = message_template.format(person_name, circ_desc)

content = client(
    system_prompt=system_prompt,
    message=message,
    temperature=1.0,
    max_tokens=2048
    )

with open(path_anonymized, "w") as fout:
    fout.write(content)
#%%
