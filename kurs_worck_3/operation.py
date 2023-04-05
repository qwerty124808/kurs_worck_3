import json
from datetime import datetime, date

def reade_transactions_history():
    """
        читает историю транзакций из operations.json
    """
    with open("kurs_worck_3\operations.json", "r", encoding="utf-8") as file:
        history_transaction = json.load(file)
        return(history_transaction)

def filtered_transaction(list_text):
    """
        фильтрует и сортирует спиисок транзакций
    """
    filter_text = []
    for item in list_text:
        if  item.get("state") == "EXECUTED":
            filter_text.append(item)
    sorted_text = sorted(filter_text, key=lambda row: row.get('date'), reverse=True)
    return sorted_text
        
def last_operations(sorted_text):
    """
        выводит список последних 5 транзакций
    """
    last_five_operations = []
    for index in range(0,5):
        last_five_operations.append(sorted_text[index])
    return last_five_operations
       

def out_data(last_five_operations):
    """
        редактирует данные о последних 5 транзакциях и делает красивый вывод
    """
    for operation in last_five_operations:
        converting_date = datetime.strptime(operation.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        date_operation = converting_date.strftime("%d.%m.%Y") # дата операции
        description = operation.get("description")            # тип операции
        to_ = operation.get("to").split()                     # куда перевод
        operationAmount = operation.get("operationAmount")    # информация о сумме и валюте 
        amount = operationAmount["amount"]                    # сумма
        currency = operationAmount["currency"]                # информация о валюте
        name = currency["name"]                               # валута
        if "from" in operation:
            from_ = operation.get("from").split()             # откуда перевод
            if len(from_) != 2:
                from_[0] = from_[0]+from_[1]
                from_[1] = from_[2]
            print(f"{date_operation} {description}\n{from_[0]} {from_[1][0:4]} {from_[1][4:6]}** **** {from_[1][-4:]} -> {to_[0]} **{to_[1][-4:]}")
            print(f"{amount} {name}\n")    
        else:
            from_ = ["",""]
            print(f"{date_operation} {description}\nОТКРЫТИЕ ВКЛАДА -> {to_[0]} **{to_[1][-4:]}")
            print(f"{amount} {name}\n")
                
history_operations = reade_transactions_history()
filter_history = filtered_transaction(history_operations)
last_operations = last_operations(filter_history)
data = out_data(last_operations)


