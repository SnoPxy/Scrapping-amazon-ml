import sys
import os
import customtkinter as ctk
from tkinter import messagebox

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.mercadoLivreController import mercadoLivreController
from controllers.amazonController import amazonController

ctk.set_appearance_mode("System")

def start_search():
    search_term = product_entry.get()
    max_price = price_entry.get()
    platform = platform_selector.get()
    link_count = link_entry.get()
    
    if not search_term or not platform:
        messagebox.showwarning("Aviso", "Por favor, preencha o termo de busca e escolha uma plataforma.")
        return

    if not link_count.isdigit() or int(link_count) <= 0:
        messagebox.showwarning("Aviso", "Por favor, insira uma quantidade válida de links.")
        return

    link_count = int(link_count)

    if platform.lower() == 'mercado livre':
        ml_controller = mercadoLivreController()
        ml_controller.main(search_term, max_price, link_count)
        print(f'Buscando "{search_term}" no {platform} para {link_count} links.')
    elif platform.lower() == 'amazon':
        az_controller = amazonController()
        az_controller.main(search_term, max_price, link_count)
        print(f'Buscando "{search_term}" no {platform} para {link_count} links.')
    elif platform.lower() == 'ambos':
        ml_controller = mercadoLivreController()
        ml_controller.main(search_term, max_price, link_count)
        az_controller = amazonController()
        az_controller.main(search_term, max_price, link_count)
    
    messagebox.showinfo("Sucesso", "A busca foi concluída e a planilha foi criada!")
    display_message(link_count)

def display_message(link_count):
    message_label = ctk.CTkLabel(frame, text=f"Planilha criada com {link_count} links!", font=("Arial", 12))
    message_label.pack(pady=5)


window = ctk.CTk()
window.title("Projeto de Web Scraping")


window.geometry("750x650")
window.minsize(750, 500)
window.maxsize(850, 768)


frame = ctk.CTkFrame(master=window, width=620, height=550)
frame.pack(side="left", padx=55, pady=20)
frame.pack_propagate(False)


title_label = ctk.CTkLabel(
    master=frame,
    text="Programa de Pesquisa",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)


description_label = ctk.CTkLabel(
    master=frame,
    text="Busque produtos nos sites Mercado Livre e/ou Amazon.",
    font=("Arial", 12, "bold")
)
description_label.pack(pady=10)


platform_label = ctk.CTkLabel(frame, text="Escolha a plataforma:", font=("Arial", 12))
platform_label.pack(pady=8)

platform_selector = ctk.CTkComboBox(frame, values=["Mercado Livre", "Amazon", "Ambos"])
platform_selector.pack(pady=5)


product_label = ctk.CTkLabel(frame, text="Produto:", font=("Arial", 12, "bold"))
product_label.pack(pady=8)

product_entry = ctk.CTkEntry(frame, placeholder_text="Digite o produto")
product_entry.pack(pady=5)

link_label = ctk.CTkLabel(frame, text="Quantidade de Links:", font=("Arial", 12, "bold"))
link_label.pack(pady=8)

link_entry = ctk.CTkEntry(frame, placeholder_text="Digite a quantidade de links")
link_entry.pack(pady=5)

price_label = ctk.CTkLabel(frame, text="Valor Máximo:", font=("Arial", 12, "bold"))
price_label.pack(pady=8)

price_entry = ctk.CTkEntry(frame, placeholder_text="Digite o valor máximo")
price_entry.pack(pady=5)


search_button = ctk.CTkButton(frame, text="Iniciar Busca", command=start_search)
search_button.pack(pady=20)

window.mainloop()
