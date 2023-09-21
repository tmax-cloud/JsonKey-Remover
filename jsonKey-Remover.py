import json
import os

def process_all_of(data):
    if isinstance(data, dict):
        if 'allOf' in data:
            # allOf의 값이 딕셔너리인 경우
            if isinstance(data['allOf'], dict):
                for key, value in data['allOf'].items():
                    data[key] = value

            # allOf의 값이 리스트인 경우
            elif isinstance(data['allOf'], list):
                for inner_data in data['allOf']:
                    for key, value in inner_data.items():
                        data[key] = value

            del data['allOf']

            return process_all_of(data)  # 다시 재귀적으로 확인
        for key, value in data.items():
            data[key] = process_all_of(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            data[i] = process_all_of(item)
    return data

# target 디렉토리 내의 모든 파일을 순회합니다.
for filename in os.listdir('target'):
    if filename.endswith('.json'):
        with open(os.path.join('target', filename), 'r') as file:
            original_data = json.load(file)
        
        processed_data = process_all_of(original_data)
        
        # 결과를 result 디렉토리에 저장합니다.
        # 디렉토리가 존재하지 않는 경우 생성합니다.
        if not os.path.exists('result'):
            os.makedirs('result')
        
        with open(os.path.join('result', filename), 'w') as file:
            json.dump(processed_data, file, indent=4)
