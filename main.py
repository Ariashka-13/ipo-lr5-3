myfile=open("D:\\profiles\\TsarevA_81\\Desktop\\ипо\\лр 5\\3\\text.txt", "r") #открыть файл
words = 0 #счетчик количества слов
with open("D:\\profiles\\TsarevA_81\\Desktop\\ипо\\лр 5\\3\\text.txt", "r") as myfile: #для оборачивания выполнения блока инструкций
    for i in myfile:#использование цикла
        words=len(i.split()) #подсчет количества слов
print("Количество слов: ", words) #вывод количества слов
