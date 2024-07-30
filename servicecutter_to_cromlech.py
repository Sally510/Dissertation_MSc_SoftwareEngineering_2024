import json
import yaml

def convert_json_to_yaml(json_file_path, yaml_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        if 'useCases' not in data:
            raise KeyError("The key 'useCases' was not found in the JSON file.")
        
        operations = []
        for use_case in data['useCases']:
            operation = {
                'name': use_case['name'],
                'consistency': 'L',
                'frequency': 1,
                'forced_operations': [],
                'database_access': []
            }
            
            entities_read = {}
            entities_written = {}
            
            for entity in use_case['nanoentitiesRead']:
                entity_name, attribute = entity.split('.')
                if entity_name not in entities_read:
                    entities_read[entity_name] = []
                entities_read[entity_name].append(attribute)
            
            for entity in use_case['nanoentitiesWritten']:
                entity_name, attribute = entity.split('.')
                if entity_name not in entities_written:
                    entities_written[entity_name] = []
                entities_written[entity_name].append(attribute)
            
            for entity_name, attributes in entities_read.items():
                operation['database_access'].append({
                    'entity_name': entity_name,
                    'read_attributes': attributes
                })
            
            for entity_name, attributes in entities_written.items():
                found = False
                for access in operation['database_access']:
                    if access['entity_name'] == entity_name:
                        access['write_attributes'] = attributes
                        found = True
                        break
                if not found:
                    operation['database_access'].append({
                        'entity_name': entity_name,
                        'write_attributes': attributes
                    })
            
            operations.append(operation)
        
        yaml_data = {'operations': operations}
        
        with open(yaml_file_path, 'w') as yaml_file:
            yaml.dump(yaml_data, yaml_file, sort_keys=False, default_flow_style=False)
        
        print(f"YAML file has been successfully generated at {yaml_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

json_file_path = 'trading\service_cutter\\trading_2_user_representations.json'
yaml_file_path = 'trading\cromlech\\trading_cromlech.yaml'
convert_json_to_yaml(json_file_path, yaml_file_path)
