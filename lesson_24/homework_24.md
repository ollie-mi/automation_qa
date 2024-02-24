### Практика з x-path
складність: легка

1. Оберіть сайт, який ви збираєтеся тестувати
2. Напишіть не менш ніж 10 x-path до елементів сайту, що важливі для перевірки його функцональності.

Ваші відповіді і адресу сайту додате у цей файл нижче.
Робота виконується в новій гілці і здається як PR у репозиторій викладача.


Сайт - https://zakaz.ua/uk/

1. login_button = '//*[@data-testid="login-button"]'
2. add_address_bar = '//*[@data-marker="Address Management Bar"]'
3. novus_button = '//*[@data-marker="NOVUS"]'
4. novus_signin_button = '//*[@data-testid="sign_in_button"]'
5. novus_mobile_input = '//*[@id="login"]'
6. novus_password_input = '//*[@id="login-password"]'
7. novus_submit_button = '//*[@id="sign_in"]/div[3]/button[1]'
8. novus_first_product_in_promotions = '//*[@id="PageWrapBody_desktopMode"]/div[4]/section/div[2]/div/div[1]/a'
9. novus_product_view_add_to_cart = '//*[@id="BigProductCardTopInfo__addButtons"]/div/button'
10. novus_cart_button = ''//*[@data-testid="cart_button"]''