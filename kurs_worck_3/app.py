import json
from operation import *

def main():
    history_operations = reade_transactions_history()
    filter_history = filtered_transaction(history_operations)
    last_op = last_operations(filter_history)
    data = out_data(last_op)

if __name__ == "__main__":
    main()
