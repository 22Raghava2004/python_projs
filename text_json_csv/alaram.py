import time
import datetime
import pygame

def set_alaram(alaram_time):
    print(f"alaram is set for {alaram_time}")
    sound_file="C:\\Users\\ragha\\Downloads\\python proj\\mymusic.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time==alaram_time:
            print("time to wake up😂😂😂😂😂")
            is_running=False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            


            while pygame.mixer.music.get_busy():
                finish_music=input("q to finish the music")  # wait for music to finish playing
                time.sleep(1)  # sleep for a short duration to avoid busy waiting
                if finish_music=="q":
                    pygame.mixer.music.stop()
                    break
                else:
                    print("invalid input")
                    continue

            is_running=False    

        time.sleep(1)# sleep for 1 second before checking again


if __name__ == "__main__":
    alaram_time=input("enter the alaram time in HH:MM:SS format")
    set_alaram(alaram_time)