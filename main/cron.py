from django_cron import CronJobBase, Schedule
from django.core.management import call_command
from datetime import datetime
import yadisk

yaToken = 'AgAAAAAhYXh_AAbOPCRUNGtsREbYq1YZlGGjYYU' # Токен для выгрузки дампа на Яндекс.Диск

class doDump(CronJobBase):
    RUN_EVERY_MINS = 60 * 24 # Вызываем каждые 24 часа
    RUN_AT_TIMES = ['15:34'] # В 15 часов

    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=RUN_EVERY_MINS) # Задаем график работы автоматической выгрузки
    code = "main.doDump" # Код для выполнения

    def do(self):
        file_json = open('dump.json', 'w') # Открываем файл для выгрузки БД в формате json
        call_command('dumpdata', format='json', indent=3, stdout=file_json)
        file_json.close()

        file_xml = open('dump.xml', 'w') # Открываем файл для выгрузки БД в формате xml
        call_command('dumpdata', format='xml', indent=3, stdout=file_xml)
        file_xml.close()

        y = yadisk.YaDisk(token=yaToken)
        date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
        json = "C:/Users/1/PycharmProjects/pythonProject/Kursach/dump.json"
        xml = "C:/Users/1/PycharmProjects/pythonProject/Kursach/dump.xml"
        y.mkdir(f"Kursach/{date}")
        y.upload(json, f"Kursach/{date}/dump.json")
        y.upload(xml, f"Kursach/{date}/dump.xml")
