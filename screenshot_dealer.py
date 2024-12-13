from pyautogui import screenshot
from win10toast import ToastNotifier
from time import sleep

def deal_screenshot():
    try:
        print("Привет!Эта программа делает скриншот с расширением png на твой компьютер.")
        timer =int(input("Каков будет обратный отсчет в секундах перед скриншотом? >>>>"))
        if timer <=0:
            print("Вы ввели недопустимые параметры")
            return None
        else:
            for i in range(timer):
                print(f"До снимка экрана осталось: {timer} секунд")
                timer -= 1
                sleep(0.8)
                if timer <=0:
                    sleep(0.5)
                    my_screenshot =screenshot("screenshot.png")
                    sleep(1.5)
                    ToastNotifier().show_toast("Скриншот сделан!","Ваш скриншот сохранен в файл screenshot.png")
                    sleep(0.5)
                    return None
    except ValueError:
        print("Вы ввели недопустимые параметры")
        return None
if __name__ =="__main__":
    deal_screenshot()



