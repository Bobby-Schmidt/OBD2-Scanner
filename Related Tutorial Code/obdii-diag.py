import obd

connection = obd.OBD(portstr='/dev/tty.OBDII-Port')

r = connection.query(obd.commands.GET_DTC)

print r.value