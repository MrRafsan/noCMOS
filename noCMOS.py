import ntplib
import datetime, time
import subprocess
import shlex





try:

	client = ntplib.NTPClient()
	response = client.request('pool.ntp.org')
	currentDT = datetime.datetime.fromtimestamp(response.tx_time)
	day = currentDT.day
	monthinteger = currentDT.month
	year = currentDT.year
	hour = currentDT.hour
	minute = currentDT.minute

	month = datetime.date(1900, monthinteger, 1).strftime('%B')
	#it will print april

#	subprocess.call(shlex.split("timedatectl set-ntp false"))  # May be necessary
	subprocess.call(shlex.split(f"sudo date -s '{day} {month} {year} {hour}:{minute}:00'"))
	subprocess.call(shlex.split("sudo hwclock -w"))

except OSError:

	print('\n')
	print('Internet date and time could not be reported by server.')
	print('There is not internet connection.')