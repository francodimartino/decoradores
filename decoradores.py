
import time
import sys

def controlar_tiempo(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args, **kwargs)
        end=time.time()
        tiempo=end-start
        horas=int(tiempo/3600)
        minutos=int((tiempo-(horas*3600))/60)
        segundos=int(tiempo-(horas*3600)-(minutos*60))
        print(f"tiempo de ejecucion: {horas} horas, {minutos} minutos, {segundos} segundos")
    return wrapper

def log_en_archivo(func):
    def wrapper(*args, **kwargs):
        sys.stdout=open(func.__name__+".txt", "w")
        func(*args, **kwargs)
        sys.stdout.close()
    return wrapper


if __name__ == "__main__":
    @log_en_archivo
    def test_log():
        print("probando este decorador")
        
    @controlar_tiempo
    def test_tiempo():
        time.sleep(5)
        print("probando este decorador")

    test_log()
    test_tiempo()