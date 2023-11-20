from develop import utils

def main():
    filename = 'operations.json'
    amount_of_operations = int(input("Введите количество операций: "))

    data = utils.get_data(filename)
    operations_executed = utils.get_operations_executed(data)
    last_num_operations = utils.get_last_num_operations(operations_executed, amount_of_operations)
    operations_formatted = utils.get_operations_formatted(last_num_operations)

    for string in operations_formatted:
        print(f"{string}\n")


if __name__ == "__main__":
    main()