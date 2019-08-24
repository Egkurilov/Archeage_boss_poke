import ts3
import config


def client_with_group_list(msg):
    with ts3.query.TS3Connection(host=config.ts3_host) as ts3conn:
        try:
            ts3conn.login(
                client_login_name=config.ts3_login,
                client_login_password=config.ts3_password
            )
        except ts3.query.TS3QueryError as err:
            print("Login failed:", err.resp.error["msg"])
            exit(1)

        ts3conn.use(sid=config.ts3_sid)
        resp = ts3conn.clientlist()
        # получить клиентов
        for client in resp:
            # если это живые клиенты
            if client['client_type'] == '0':
                # print(client['client_nickname'])
                # получить группы сервера
                group_list = ts3conn.servergroupsbyclientid(cldbid=client['client_database_id'])
                for group in group_list:
                    # сверить группы со списком
                    if group['name'] == config.favorite_group:
                        # pocked client с сообщением
                        ts3conn.clientpoke(msg='Эржан вставай ' + msg, clid=client['clid'])
