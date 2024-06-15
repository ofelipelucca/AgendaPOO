from src.UI.UI_Principal import Principal

if __name__ == "__main__":
    app = Principal()
    app.mainloop()
    app.adicionar_evento(2024, 6, 1, "Compromisso", "João", "#FF6347", "Aniversário do João")