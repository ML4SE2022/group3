import yaml

with open('config.yaml') as f:
    config = yaml.load(f)

print(config)