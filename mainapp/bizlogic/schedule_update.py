from telegram import ParseMode
from tga.management.commands.bot import *
request = Request(
    connect_timeout=0.5,
    read_timeout=1.0,
)
bot = Bot(
    request=request,
    token=settings.TOKEN,
    base_url=getattr(settings, 'PROXY_URL', None),
)
bot.send_message(chat_id=542277086, text=f'<strong>ПЕРЕЗВОНИ</strong>\n{phone}\n\n{name}',
                             parse_mode=ParseMode.HTML)


from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)