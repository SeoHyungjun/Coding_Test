import datetime
print(*str(datetime.datetime.utcnow())[:10].split('-'), sep = '\n')