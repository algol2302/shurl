# shurl
Простой сервис генерации коротких ссылок

Сервис можно протестировать в виртуальном окружении, файл requirements.txt доступен в репозитории. Приложение тестировалось в Linux, прилагаются необходимые скрипты для миграций и запуска тестового сервера.

Приложение состоит из проекта shurl (совпадает с названием папки shurl), где хранятся все настройки и самого приложения shurlapp, где содержаться файлы urls, models, views и папка template с html-шаблонами. 

После выполнения миграций (файл ./migrate.sh) и запуска проекта (./runserver.sh), можно в адресной строке ввести адрес сервера приложения (по-умолчанию это «127.0.0.1:8000») и должен появится текст с предложение ввести URL. После нажатия кнопки «Создать»  ниже появится ссылка типа «127.0.0.1:8000/Gaf3B», которую можно скопировать и открыть в браузере, после чего произойдет переход на нужную страницу. Если сервер будет иным, то необходимо отредактировать в шаблоне https://github.com/algol2302/shurl/blob/master/shurlapp/templates/shurl_create_or_find.html строку <p><input value="127.0.0.1:8000/{{ shurl }}"></p>.

В dev ветке предполагается написание приложения для api
