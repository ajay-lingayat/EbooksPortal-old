import sys, os

import mysql.connector as connector
from ConsoleMessenger import ConsoleMessage

from manage import main
from EbooksPortal.settings.dev import DATABASES, MODEL_APPS, SEED_MODELS

global console
console = ConsoleMessage()

class Database:
    def __init__(self, commands):
        if len(commands) < 2:
            console.danger('Database credentials not provided!')
            exit(0)
        elif len(commands) == 2:
            console.danger('Password not provided!')
            exit(0)

        self.commands = commands
        self.user = commands[1]
        self.password = commands[2]
    
    def create(self):
        try:
            mydb = connector.connect(
                host='localhost',
                user=self.user,
                password=self.password
            )
            mycursor = mydb.cursor()

            for key in DATABASES.keys():
                db = DATABASES[key]

                raw_queries = [
                    f"CREATE DATABASE {db['NAME']};",
                    f"CREATE USER '{db['USER']}'@'localhost' IDENTIFIED BY '{db['PASSWORD']}';",
                    f"GRANT ALL PRIVILEGES ON {db['NAME']}.* TO '{db['USER']}'@'localhost';",
                ]
                for raw_query in raw_queries:
                    try:
                        output = mycursor.execute(raw_query)
                        console.success('Success', output)
                    except Exception as e:
                        console.danger(e)

            mydb.commit()
        except Exception as e:
            console.danger('Error in Database Creation.')
            console.danger(e)

    def migrate(self):
        try:
            commands = ['manage.py', 'makemigrations']+MODEL_APPS
            console.info('COMMAND', ' '.join(commands))
            main(commands=commands)

            commands = ['manage.py', 'migrate']
            console.info('COMMAND', ' '.join(commands))
            main(commands=commands)
        except Exception as e:
            console.danger('Error in Database Migration.')
            console.danger(e)

    def load_data(self):
        found = os.path.isfile('seed.json')

        if not found:
            commands = ['manage.py', 'dumpdata'] + SEED_MODELS
            commands += ['--format=json', '--indent=4']
            command = f'python {" ".join(commands)} > seed.json'
            console.info('COMMAND', command)
            os.system(command)
            found = os.path.isfile('seed.json')

        if found:
            commands = ['manage.py', 'loaddata', 'seed.json']
            console.info('COMMAND', ' '.join(commands))
            main(commands=commands)


if __name__ == "__main__":
    db = Database(sys.argv)
    db.create()
    db.migrate()
    
    try:
        if "createsuperuser" in sys.argv:
            console.info('COMMAND', 'python manage.py createsuperuser')
            main(commands=['manage.py', 'createsuperuser'])
    except Exception as e:
        console.danger(e)

    try:
        if "loaddata" in sys.argv:
            db.load_data()
    except Exception as e:
        console.danger(e)