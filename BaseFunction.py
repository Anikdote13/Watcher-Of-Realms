import pyautogui as pag
import time
import logging
from datetime import datetime

class BaseFunction:

    logging.basicConfig(level=logging.INFO, 
                    filename=f".//logs//{datetime.now().strftime('%d-%m-%Y')}.log",
                    filemode="a",
                    format="%(asctime)s - %(levelname)s(%(lineno)d)-(%(filename)s)-(%(funcName)s) == %(message)s",
                    encoding="UTF-8")
    
    def find_image(self, image, confidence=0.9):
        """Ищет изображение на экране

        Args:
            image (string): путь до изображение
            confidence (float): коэфициент совпадения

        Returns:
            int: 1 - изображение найдено, 0 - не найдено
        """
        try:
            pag.locateOnScreen(image, confidence=confidence)
            logging.info(f"Изображение найдено: {image}")
            # print(f"Изображение найдено: {image}")
            isFind = 1
        except:
            isFind = 0
            
        return isFind
    
    def find_and_click_image(self, image, confidence=0.9, wait=0.2):
        """Ищет изображение на экране и нажимает на него

        Args:
            image (string): путь до изображение
            confidence (float): коэфициент совпадения
        """
        try:
            coor = pag.locateCenterOnScreen(image, confidence=confidence)
            if coor is not None:
                pag.click(coor.x, coor.y)
                time.sleep(wait)
            logging.info(f"Изображение найдено: {image}. Нажимаю на координаты x = {coor.x}, y = {coor.y}")
            # print(f"Изображение найдено: {image}. Нажимаю на координаты x = {coor.x}, y = {coor.y}")
        except:
            pass
        
    def click(self, coor_x, coor_y, wait=0.2):
        """Нажимает на координаты 'x' и 'y'

        Args:
            coor_x (int): координата 'x'
            coor_y (int): координата 'y'
        """
        pag.click(coor_x, coor_y)
        logging.info(f"Нажимаю на координаты x = {coor_x}, y = {coor_y}")
        time.sleep(wait)