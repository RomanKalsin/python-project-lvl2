from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    ansver = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff('tests/fixtures/json/file1.json', 'tests/fixtures/json/file2.json') == ansver
    assert generate_diff('tests/fixtures/yaml/file1.yaml', 'tests/fixtures/yaml/file2.yml') == ansver

