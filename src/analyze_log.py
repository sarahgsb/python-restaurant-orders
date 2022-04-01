from utils.analyze import orders_file, maria, arnaldo, joao, days_joao


def analyze_log(path_to_file):
    try:
        files = orders_file(path_to_file)
        maria_order = maria(files)
        arnaldo_order = arnaldo(files)
        joao_orders = joao(files, 'hamburguer')
        joao_days = days_joao(files, 'terça-feira')

        with open("./data/mkt_campaign.txt", "w") as file:

            file.write(f"{maria_order}\n")
            file.write(f"{arnaldo_order}\n")
            file.write(f"{joao_orders}\n")
            file.write(f"{joao_days}\n")

    except FileNotFoundError:
        if (not path_to_file.endswith('.csv')):
            raise FileNotFoundError(f'Extensão inválida: "{path_to_file}"')

        raise FileNotFoundError(f'Arquivo inexistente: "{path_to_file}"')
