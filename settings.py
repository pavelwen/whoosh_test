
user_id = 'postgres'
password = '123456'
server = 'localhost'
database = 'info'
DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s/%s' % (user_id, password, server, database)
del user_id, password, server, database