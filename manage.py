# -*- coding:utf-8 -*-

from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand

from mynews import create_app
from mynews.exts import db
from mynews.models import News, Site, Category

import config

app = create_app(config.DevConfig)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, Site=Site, News=News, Category=Category)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
