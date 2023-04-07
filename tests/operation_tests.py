from kurs_worck_3 import operation

def test_get_filtered_transaction():
  test_list = [  {
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2017-05-19T12:51:49.023880",
    "operationAmount": {
      "amount": "6381.58",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
    "to": "Счет 58518872592028002662"
  },
  {
    "id": 921286598,
    "state": "EXECUTED",
    "date": "2018-03-09T23:57:37.537412",
    "operationAmount": {
      "amount": "25780.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 26406253703545413262",
    "to": "Счет 20735820461482021315"
  },
  {
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {
      "amount": "991.49",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 71687416928274675290",
    "to": "Счет 87448526688763159781"
  },
  {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265"
  }]
  
  test_list_2 = [{
    "id": 27192367,
    "state": "CANCELED",
    "date": "2018-12-24T20:16:18.819037",
    "operationAmount": {
      "amount": "991.49",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 71687416928274675290",
    "to": "Счет 87448526688763159781"
  }]

  test_out_1 = [ 
    {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265"
  },
  {
    "id": 921286598,
    "state": "EXECUTED",
    "date": "2018-03-09T23:57:37.537412",
    "operationAmount": {
      "amount": "25780.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 26406253703545413262",
    "to": "Счет 20735820461482021315"
  },
  {
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2017-05-19T12:51:49.023880",
    "operationAmount": {
      "amount": "6381.58",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
    "to": "Счет 58518872592028002662"
  }
  ]
  test_out_2 = []


  assert operation.filtered_transaction(test_list) == test_out_1
  assert operation.filtered_transaction([]) == test_out_2
  
def test_last_five_operations():
  input_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  output_1 = [1, 2, 3, 4, 5]
  assert operation.last_operations(input_1) == output_1

def test_out_data():
  test_input = [
    {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  },
  {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07T06:17:14.634890",
    "operationAmount": {
      "amount": "48150.39",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 2842878893689012",
    "to": "Счет 35158586384610753655"
  },
  {
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
      "amount": "30153.72",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
  },
  {
    "id": 482520625,
    "state": "EXECUTED",
    "date": "2019-11-13T17:38:04.800051",
    "operationAmount": {
      "amount": "62814.53",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 38611439522855669794",
    "to": "Счет 46765464282437878125"
  },
  {
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05T12:04:13.781725",
    "operationAmount": {
      "amount": "21344.35",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 77613226829885488381"
  }
  ]
  output = ["08.12.2019 Открытие вклада\nОТКРЫТИЕ ВКЛАДА -> Счет **5907\n41096.24 USD\n",
            "07.12.2019 Перевод организации\nVisaClassic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n",
            "19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n",
            "13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** 9794 -> Счет **8125\n62814.53 руб.\n",
            "05.11.2019 Открытие вклада\nОТКРЫТИЕ ВКЛАДА -> Счет **8381\n21344.35 руб.\n"
           ]
  assert operation.out_data(test_input) == output


    