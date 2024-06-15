from src.Interfaces.Inter_Calendario import Inter_Calendario

from typing import Dict, List
from datetime import datetime, timedelta

class Calendario(Inter_Calendario):
    def __init__(self) -> None:
        self.__mapa_Horario: Dict[str, List[str]] = {}
        self.__agenda: Dict[str, Dict[str, List[str]]] = {}

    def inserir(self, key: str, atividades: List[str] = []) -> None:
        if len(atividades) == 0:
            #Implementa o inserir só com um parâmetro
            if key not in self.__agenda:
                self.__agenda[key] = {}
             
            for horario, lista_atividades in self.__mapa_Horario.items():
                if horario in self.__agenda[key].keys():
                    self.__mapa_Horario[horario] = self.__agenda[key][horario] + self.__mapa_Horario[horario]
                
            self.__agenda[key].update(self.__mapa_Horario)
            self.__mapa_Horario.clear()
            
        else:
            #Implementa o inserir com 2 parâmetros
            if key not in self.__mapa_Horario:
                self.__mapa_Horario[key] = []
                
            self.__mapa_Horario[key].extend(atividades)

    def sizeMapaHorario(self) -> int:
        return len(self.__mapa_Horario)

    def sizeAgenda(self) -> int:
        return len(self.__agenda)
    
    def ordenarAgenda(self) -> None:
        for dia in self.__agenda:
            self.__agenda[dia] = sorted(self.__agenda[dia].items(), key=lambda x: datetime.strptime(x[0], "%H:%M"))
            self.__agenda[dia] = {key: valor for key, valor in self.__agenda[dia]}
    
    def _imprimirCalendario(self, dia_inicial: str) -> None:
        data_inicial = datetime.strptime(dia_inicial, "%d/%m/%Y")

        for i in range(7):
            proxima_data = data_inicial + timedelta(days=i)

            print("\n" + f"{proxima_data.day}/".rjust(3, "0") + f"{proxima_data.month}/".rjust(3, "0") + f"{proxima_data.year}:")
            
            if proxima_data.strftime("%d/%m/%Y") in self.__agenda:
                for horario, atividades in self.__agenda[proxima_data.strftime("%d/%m/%Y")].items():
                    print(f"\n\t{horario} - {', '.join(atividades)}")
            else:
                print("\n\tNenhuma atividade cadastrada")
