<p align="center">
      <img src="https://i.ibb.co/KWwTWWK/PQx-Wbey-B2-Ngr-Eo5-KOMXdmw.png" width="726">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python Version">
   <img src="https://img.shields.io/badge/Version-1.0-lightgrey" alt="Game Version">
</p>

## About

Парсер собирает данные оценки metacritic, оценки пользователей, год релиза по играм и платформе с сайта [Metacritic.com](https://www.metacritic.com)

## Documentation

Данный проект полностью рабочий. Для его запуска необходимо скачать проект. Поместить в главную папку csv файл с названием игр и платформ (в сокращенном виде). 
Пример есть в репозитории под названием **Game_Platform_Example**. Для работы парсера нужно иметь файл `chromedriver.exe` для Google Chrome.
Для остальных браузеров необходимо скачать на сайте [www.selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/).
Парсер сохраняет найденные данные в файл **Game_Score.csv** среди них это **Critic_Score**, **User_Score**, **Year_of_Release**


## Distribute

Особенности парсера:
+ Парсер находит точные вхождения, когда название искомой игры соответствует названию игры на сайте, однако не учитывает регистр и различные знаки
+ Ищет **Critic_Score**, **User_Score**, **Year_of_Release**, когда каких-то данных нет, собирает всю доступную информацию
+ Сохраняет всю полученную информацию в случае каких-либо сбоев
+ Ищет информацию по 17 платформам
