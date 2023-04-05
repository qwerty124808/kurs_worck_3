from kurs_worck_3 import operation

def tests_get_filtered_transaction():
    assert operation.filtered_transaction(list_text).item.get("state")
    