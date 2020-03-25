from common.dbconnector import DualRedisConnector


if __name__ == '__main__':
    drc = DualRedisConnector()
    print(drc.first_cursor.keys())
    print(drc.second_cursor.keys())
    print(drc.first_cursor.get('564'))
