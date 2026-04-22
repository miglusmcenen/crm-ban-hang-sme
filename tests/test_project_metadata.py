from pathlib import Path


def test_crm_runtime_database_is_ignored():
    assert 'app.db' in Path('.gitignore').read_text(encoding='utf-8')
