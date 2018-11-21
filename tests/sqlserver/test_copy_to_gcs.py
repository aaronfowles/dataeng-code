from dataeng_code.sqlserver import copy_to_gcs


def test_do_something():
    assert copy_to_gcs.do_something() == 'something'
