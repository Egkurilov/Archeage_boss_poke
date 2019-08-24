import ts3

ts3_login = 'Qqwe'
ts3_password = 'VwxcR6cM'

favorite_group = 'Smiley'

def client_with_group_list(msg):
    with ts3.query.TS3Connection(host="139.59.152.82") as ts3conn:
        try:
            ts3conn.login(
                client_login_name=ts3_login,
                client_login_password=ts3_password
            )
        except ts3.query.TS3QueryError as err:
            print("Login failed:", err.resp.error["msg"])
            exit(1)

        ts3conn.use(sid=12)
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
                    if group['name'] == favorite_group:
                        # pocked client с сообщением
                        ts3conn.clientpoke(msg='Эржан вставай ' + msg, clid=client['clid'])
