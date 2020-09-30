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


# example API usage

Log.INFO("some text") #prints "[?] INFO: some text" with colors
Log.enable_save_to_txt("C:/SomeFolder") #stars saving following logs to txt into path, if empty saves to class position
Log.WARNING("something's happening") #prints "[!] WARNING: something's happening" with colors both to cmd and to txt
Log.enable_date_timestamp("dd/mm/yy") #starts printing text with date timestamp with the given format (default = "dd/mm/yy")
Log.enable_time_timestamp("hh:mm:ss") #stars printing text with time timestamp  with the given format (default = "hh:mm:ss")
Log.disable_colors()
Log.enable_colors()
