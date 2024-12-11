import os
import yaml

def load_config():
    # Determine the path to the config file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    
    # Open and read the YAML file
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config

# Example usage (optional test)
if __name__ == "__main__":
    cfg = load_config()
    print("Loaded configuration:", cfg)

