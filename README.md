# Midas
Midas is a low code self-supervised production grade RAG agent creation.

## Using Midas
```python
# Import
from midas.agent import Midas

# Create an Agent
my_agent = Midas("agent_name")
my_agent.set_objective("agent_instructions")

my_agent.add_criteria(
    [
        {"criteria_name": "criteria_string"},
    ]
)

# Running an Agent
result = my_agent.run(convo_id)

# Training an Agent
my_agent.train(convo_ids)

# Saving an Agent
my_agent.save('../agent.json')

# Loading an Agent
my_agent = Midas().load('../agent.json')
```


## Setup Instructions

1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. Set up virtualenv
```
pyenv install 3.12.0
pyenv virtualenv 3.12.0 midas
```
3. Activate virtualenv
```
pyenv activate midas
```
4. Download required python packages
```
pip install -r requirements.txt
```