# scheduleMe CLI

import click
from art import text2art
from ssh_client import ScheduleMe

@click.command()
def scedule_me_init():
	title = text2art('scheduleMe',font= 'big')
	click.echo(click.style(title,blink=True,fg='green'))
	click.echo(click.style("Connecting ssh server via scheduleMe module\n"))
	click.echo("Provide following info for SSH connection")
	hostname = click.prompt(click.style("Hostname",fg="blue"),type=str)
	username = click.prompt(click.style("Username",fg="blue"),type=str)
	password = click.prompt(click.style("Password",fg="blue"),type=str)
	sheduler = ScheduleMe(hostname,username,password)
	click.echo(click.style(sheduler.msg_from_scheduleMe,fg='green'))
	if sheduler.msg_from_scheduleMe != 'Failed':
		if sheduler.setup_required():
			# print("-- -- --")
			sheduler.setting__up()
		else:
			
			click.echo(click.style("Select your action:\n",fg='yellow'))
			# click.echo(click.style("[1] Setting up\n",fg='red'))
			click.echo(click.style("[1] Add a new corn job \n",fg='red'))
			click.echo(click.style("[2] listing existing cron jobs \n",fg='red'))
			click.echo(click.style("[3] Remove cron jobs \n",fg='red'))

			user_input = click.prompt(click.style('Select your option',fg='blue'),type=int)
			if user_input == 1:
				
				print('* for any value, if you want learn more about crontab - refer https://crontab.guru/')
				minute = click.prompt(click.style('Minute',fg='blue'),type=str)
				hour = click.prompt(click.style('Hour',fg='blue'),type=str)
				Month_day = click.prompt(click.style('Month day',fg='blue'),type=str)
				Month = click.prompt(click.style('Month',fg='blue'),type=str)
				JOB =  click.prompt(click.style('Job',fg='blue'),type=str)
				job_cmd = f"crontab -l 2>/dev/null| cat - <(echo \" {minute} {hour} {Month_day} {Month} {JOB} \") | crontab -"
				print('Do you want create following cron job, if yes please press [Y] else [N]')
				click.echo(click.style(job_cmd,fg='green'))
				var_ = click.prompt('Please type your action',type=str)

				if var_ == 'Y':
					out,msg = sheduler.execute_cmds(job_cmd)
					if out:
						click.echo(click.style(msg,fg='green'))
					else:
						click.echo(click.style(msg,fg='red'))
					
				elif var_ == 'N':
					click.echo(click.style("ack\n",fg='red'))
				else:
					click.echo(click.style("Wrong input\n",fg='red'))

			elif user_input == 2:
				out,msg = sheduler.execute_cmds('crontab -l')
				if out:
					click.echo(click.style(msg,fg='green'))
				else:
					click.echo(click.style(msg,fg='red'))
			elif user_input == 3:
				print(3)
			else:
				click.echo(click.style('You select a wrong option',fg='blue'))
	click.echo(click.style('OK GoodBye',fg='yellow'))


if __name__ == '__main__':
	scedule_me_init()