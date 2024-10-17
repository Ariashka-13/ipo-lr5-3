myfile=open("text.txt", "r") #открыть файл
words = 0 #счетчик количества слов
with open("text.txt", "r") as myfile: #для оборачивания выполнения блока инструкций
    for i in myfile:#использование цикла
        words=len(i.split()) #подсчет количества слов
print("Количество слов: ", words) #вывод количества слов
