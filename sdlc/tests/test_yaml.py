import yaml

with open('src/sdlc/config/agents.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(type(data['agents']))