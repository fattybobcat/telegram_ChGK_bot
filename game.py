import time
from threading import Thread

TIMER = 80
#отдельная функция с таймером
def start_timer():
    timer_count = TIMER
    print("У вас есть {} сек.! \nВремя пошло!".format(timer_count))
    while timer_count >5:
      #  if timer_count >=5:
        time.sleep(timer_count//2)

        timer_count -= timer_count //2
        print("Осталось: {} сек.".format(timer_count))
    print("Осталось: {} сек.".format(timer_count))
    time.sleep(5)
    timer_count -= 5
    print("Время вышло!", timer_count)
th = Thread(target=start_timer, args=())




th.start()

