Goal: Verify that the SimpleStorage contract is deployed successfully and receives a valid address.
 Steps:
    1. Deploy the contract to a local network (Ganache).
    2. Verify that the get() method returns an initial value (e.g. 0).
    3. Expected result: The contract has a valid address and the initial value is 0.

    Functional test for set() and get() in SimpleStorage
  Goal: Verify that the set() function correctly updates the value, and get() returns the updated value.
    Steps:
    1. Call the set(42) function.
    2. Call the get() function.
    3. Expected result: get() returns the value 42.

    Negative test for SimpleStorageV2 (value constraint)
  Goal: Verify that the set() function in the modified contract rolls back the transaction when an invalid value is passed (e.g. > 1000).
Steps:Call set(2000) from another account or in the contract where the limit is set.
Expected result: The transaction is rolled back with the message "Value too high".

    SimpleStorage boundary value test
Goal: Check that the contract correctly handles the maximum possible value for the uint256 type.
    Steps:
    1. Call set(2**256 - 1).
    2. Verify that get() returns this value.
Expected result: The value is successfully set and returned.

    SimpleStorage event emission test
  Goal: Check that calling set() generates an event with the correct parameters.
  Steps: 
  1. Call set(77) and get a transaction receipt.
  2. Parse the logs for the event (e.g. DataSet).
  Expected result: An event with the specified value and sender address is emitted.

    Deployment Test for OwnerBasedStorage
Goal: Verify that the OwnerBasedStorage contract correctly sets the owner when deployed.
  Steps:
  1. Deploy the contract using the accounts[0] account.
  2. Verify that the owner() function returns accounts[0].
Expected Result: The owner is the account used for the deployment.

Negative Test for the set() Function in OwnerBasedStorage
Goal: Verify that the set() function rolls back the transaction if called from a non-owner.
  Step: Attempt to call set(999) from the accounts[1] account.
Expected Result: The transaction rolls back with the error "Only owner can set the data".

Separate Storage Test in UserStorage
Goal: Verify that different users can independently persist their values.
  Steps:
  1. User accounts[0] sets the value to 100.
  2. User accounts[1] sets the value to 200.
  3. Use getFor() to check that accounts[0] returns 100 and accounts[1] returns 200.
Expected result: The values ​​are stored independently for each user.

Integration test for connection via Infura (Sepolia)
Goal: Check that the application can connect to the public test network via Infura.
  Steps:
  1. Use the Infura URL for the Sepolia network.
  2. Verify that the w3.is_connected() call returns True and the current block number can be retrieved.
Expected result: Successful connection, block number > 0.

Load testing
Goal: Evaluate the performance of the contract when executing a large number of transactions.
  Steps:
  1. Run 1000 calls to set() (or similar) in a loop.
  2. Measure the total execution time and average gas consumption.
Expected Result: All transactions are completed in a reasonable time, without errors.


Мета: переконайтеся, що контракт SimpleStorage успішно розгорнуто та отримує дійсну адресу. 
Кроки:
Розгортання контракту в локальній мережі (Ganache). Переконайтеся, що метод get() повертає початкове значення (наприклад, 0). 
Очікуваний результат: контракт має дійсну адресу, а початкове значення дорівнює 0. 

Функціональний тест для set() і get() у SimpleStorage 
Ціль: переконайтеся, що функція set() правильно оновлює значення, а get() повертає оновлене значення. 
Кроки:
Викличте функцію set(42). Викличте функцію get(). Очікуваний результат: get() повертає значення 42. Негативний тест для SimpleStorageV2 (обмеження значення) Мета: переконайтеся, що функція set() у зміненому контракті відкочує транзакцію, коли передається недійсне значення (наприклад, > 1000).
Кроки:
Виклик set(2000) з іншого облікового запису або в договорі, де встановлено ліміт. 
Очікуваний результат: транзакція відкочується з повідомленням «Зависоке значення». 
Перевірка граничного значення SimpleStorage 
Мета: перевірте, чи правильно обробляє контракт максимально можливе значення для типу uint256. 
Кроки:
Набір викликів (2**256 - 1). Переконайтеся, що get() повертає це значення. Очікуваний результат: значення успішно встановлено та повернено. 

Перевірка випромінювання подій SimpleStorage. 
Мета: переконатися, що виклик set() генерує подію з правильними параметрами
Кроки:
Викличте set(77) і отримайте квитанцію про транзакцію. Проаналізуйте журнали для події (наприклад, DataSet). 
Очікуваний результат: генерується подія з указаним значенням і адресою відправника. 

Тест розгортання для OwnerBasedStorage 
Ціль: переконайтеся, що договір OwnerBasedStorage правильно встановлює власника під час розгортання. 
Кроки:
Розгорніть договір за допомогою облікового запису accounts[0]. Переконайтеся, що функція owner() повертає accounts[0]. 
Очікуваний результат: власником є ​​обліковий запис, який використовується для розгортання. 

Негативний тест для функції set() у OwnerBasedStorage 
Ціль: переконайтеся, що функція set() відкочує транзакцію, якщо її викликає невласник. 
Кроки:
Спроба викликати set(999) з облікового запису accounts[1]. 
Очікуваний результат: транзакція відкочується з помилкою «Лише власник може встановити дані». 

Окреме тестування сховища в UserStorage. 
Ціль: переконатися, що різні користувачі можуть незалежно зберігати свої значення.
Кроки:
User accounts[0] встановлює значення 100. User accounts[1] встановлює значення 200. Використовуйте getFor(), щоб перевірити, чи accounts[0] повертає 100, а accounts[1] повертає 200. 
Очікуваний результат: значення зберігаються незалежно для кожного користувача. 

Тест інтеграції для підключення через Infura (Sepolia) 
Мета: перевірити, чи програма може підключитися до публічної тестової мережі через Infura. 
Кроки:
Використовуйте URL-адресу Infura для мережі Sepolia. Переконайтеся, що виклик w3.is_connected() повертає значення True і поточний номер блоку можна отримати. 
Очікуваний результат: Успішне підключення, номер блоку > 0. 

Навантажувальне тестування 
Мета: Оцінити продуктивність контракту при виконанні великої кількості транзакцій. 
Кроки:
Запустіть 1000 викликів set() (або подібного) у циклі. Виміряйте загальний час виконання та середнє споживання газу. 
Очікуваний результат: усі транзакції виконано в прийнятний час, без помилок.