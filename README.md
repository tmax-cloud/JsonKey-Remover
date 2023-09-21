# JsonKey-Remover

## Prerequsites
1. Python3
2. Pip

## Usage
1. 다음 명령어를 실행하여 pyyaml 모듈을 다운 받는다.
    ```
    pip install pyyaml
    ```
2. target 디렉토리 하위에(없을시 디렉토리 생성 필요) allOf 키를 제거하고자 하는 json 파일들을 넣는다.
3. 다음 명령어를 실행한다.
    ```
    python3 jsonKey-Remover.py
    ```
4. Result 디렉토리가 생기고 내부에 allOf 키가 제거된 json 파일들이 생성되는 것을 확인한다.