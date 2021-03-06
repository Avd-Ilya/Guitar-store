# Guitar-store
### СУБД 3 курс 

### Состав команды:
- Авдеев (БД товаров)
- Трудов (БД магазина)
- Мамедова (БД логи)


### №1. Проектирование системы
Предметная область: интернет магазин гитар  

Описание предметной области:
1) Интернет магазин содержит товары
2) Товары относятся к подкатегориям и категориям
3) Товары имеют название, цену, производиетля и прочие характеристики
4) Клиент имеет возможность оформлять заказ, содержащий товары 
5) При оформлении заказа клиент указывает пункт выдачи  
6) Заказ имеет статус 
7) Клиент может активировать промокод на скидку при оформлении заказа
8) Администратор может редактировать информацию о товарах, заказах, пользователях

Функциональные требования
1) Авторизация пользователя 
2) Просмотр товаров 
3) Добавление товаров в корзину 
4) Оформление заказа 
5) Отмена заказа 
6) Редактирование информации администратором
7) Показ наиболее популярных товаров

БД "Товары"

![Реляционная схема БД "Товары"](/images/DB_Product_ERDPlus.png)

БД "Магазин"

![Реляционная схема БД "Магазин"](/images/DB_Store_ERDPlus.jpg)

БД "Логи"

API (MongoDB)  
Чтобы запустить API, запустите скрипт main.py. Это запустит сервер http://127.0.0.1:8000. Перейдите http://127.0.0.1:8000/docs, чтобы протестировать работу с БД.

1. Начальная страница 
![endpoints_page](/images/fastapi1.png)
2. Посмотреть всех пользователей в БД
![find_all](/images/get_all.png)
3. Посмотреть одного пользователь по ID в БД
![find_one](/images/get_one.png)
4. Добавить пользователя
![create_user](/images/create.png)
5. Обновить информацию о пользователе
![update_user](/images/update.png)
6. Удалить пользователя
![delete_user](/images/delete.png)


Аналогично с коллекцией "logProduct"

Запросы: 
1) Самый просматриваемый товар за неделю
2) Самый покупаемый товар за все время
3) Самый просматриваемый товар за месяц






















