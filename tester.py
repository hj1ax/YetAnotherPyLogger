import logger as Log

# print(REVERSED + "Hola" + RESET)
# print(BOLD + "Hola")
# print(UNDERLINE + "Hola" + RESET)

Log.ERROR("An Error Occurred Unexpectedly")
Log.WARNING("Something strange is happening")
Log.SUCCESS("Everything is working fine")
Log.INFO("Something is working...")

#print(RESET + BACK_BLUE + "Some Text")
print(Log.reset)

class Logger:
    pass

log = Log.LoggerBuilder()
log.startPattern()
log.setColor(Log.Colors.RED).setStyle(Log.Styles.BOLD)
log.setText("[-] Error: ")
log.resetStyle()
log.setInputText()
log.resetStyle()
log.endPattern()
log.setPublic()


