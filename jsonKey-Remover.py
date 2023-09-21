import os
import json
import yaml
import argparse

def process_allOf(data):
    if isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, (dict, list)):
                data[index] = process_allOf(item)
    elif isinstance(data, dict):
        if 'allOf' in data:
            allOf_content = data['allOf']
            del data['allOf']

            if isinstance(allOf_content, list):
                for content in allOf_content:
                    data.update(content)
            elif isinstance(allOf_content, dict):
                data.update(allOf_content)

        for key, value in data.items():
            if isinstance(value, (dict, list)):
                data[key] = process_allOf(value)
    return data

def main(output_format):
    input_dir = "target/"
    output_dir = "result/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            with open(os.path.join(input_dir, filename), 'r') as file:
                data = json.load(file)

            processed_data = process_allOf(data)

            output_filename = os.path.join(output_dir, filename)

            if output_format == "yaml":
                with open(output_filename.replace('.json', '.yaml'), 'w') as outfile:
                    yaml.dump(processed_data, outfile, default_flow_style=False)
            else:
                with open(output_filename, 'w') as outfile:
                    json.dump(processed_data, outfile, indent=4)
                    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSON files to remove allOf and save in desired format.')
    parser.add_argument('--format', choices=['json', 'yaml'], default='json', help='Output format (default: json)')

    args = parser.parse_args()
    main(args.format)
