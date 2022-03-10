# pyscript to connect  host application

import paramiko
from colorama import Fore
import os


class ScheduleMeOutExceptions(Exception):
	def __init__(self, outerr):
		self.message = outerr if outerr else 'ScheduleMeOutExceptions raised'
		

class ScheduleMe:

	def __init__(self, host, user, pswd):

		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.client.connect(hostname=host, username=user, password=pswd)
		# self.client = ssh_client
		self.msg_prefix = "(ScheduleMe ⏰): "
		self.msg_from_scheduleMe = f"Successfully connected to {host}" if self.__ping__() else "Failed"
		self.base_dir = os.path.dirname(__file__)

	def __ping__(self):
		try:
			sin, sout, serr = self.client.exec_command('ls -d */', timeout=5)
			return True
		except Exception as e:
			print(e)
			return False

	def setup_required(self):
		sin, sout, serr = self.client.exec_command('ls -d */', timeout=5)
		dir_ = self.file_to_string(sout) 
		directories = [x.strip() for x in list(dir_.strip().split('/'))]
		# print(directories)
		return False if 'SchedulePie' in directories else True
	
	def file_to_string(self,stream,to_string=True):
		message = stream.readlines()
		if type(message) == list:
			message = " ".join(message)
		return message
	
	def execute_cmds(self, cmd, in_=None):

		try:
			print(Fore.BLUE+f"{self.msg_prefix}Executing CMD :{cmd}")
			stdin, stdout, stderr = self.client.exec_command(cmd)
			if in_:
				stdin.write(f"{in_}\n")
			# print(stderr)
			if stderr.read(1):
				print("std error we got ")
				raise ScheduleMeOutExceptions(self.file_to_string(stderr))
			
			return True,self.file_to_string(stdout) 
		except ScheduleMeOutExceptions as e:
			print(Fore.RED+f"{self.msg_prefix}Failed CMD :{cmd}")
			return False,'connection closed' if not e.message else e.message

	def setting__up(self):
		try:
			print(Fore.BLUE+f"{self.msg_prefix}Setting up initiated...")
			file_path = self.execute_cmds('pwd')[1]  
			file_path = file_path.strip()
			print(Fore.BLUE+f"{self.msg_prefix} Creating a SchedulePie folder in {file_path}")
			folder_name = 'SchedulePie'
			if not self.execute_cmds(f'mkdir {folder_name};')[0]:
				raise ScheduleMeOutExceptions('Failed to create folder')
			ftp_client = self.client.open_sftp()
			for each_file in os.listdir(f"migrate"):
				source = f"migrate/{each_file}"
				destination_file = f"{file_path}/{folder_name}/{each_file}"
				ftp_client.put(source, destination_file)
			ftp_client.close()
			print(Fore.GREEN+f"{self.msg_prefix} OK Done...")
		except Exception as e:
			print(Fore.RED+f"{self.msg_prefix}{e}")


if __name__ == '__main__':
	# connection_obj = ScheduleMe("","","")
	# print(connection_obj.msg_from_scheduleMe)
	# connection_obj.__ping__()
	# print(connection_obj.execute_cmds('ls -la /usr/bin/crontab'))
	# (True, '-rwxr-sr-x 1 root crontab 39352 Nov 16  2017 /usr/bin/crontab\n')
	
	# print(connection_obj.execute_cmds("chmod 777 /usr/bin/crontab"))
	# cmd = "crontab -l 2>/dev/null| cat - <(echo \"* * * * * python /home/dxuser/example.py\") | crontab -"
	print(connection_obj.execute_cmds("crontab -l"))



	# connection_obj.setting__up()
