import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, hash(password), age)
        self.users.append(new_user)
        self.current_user = new_user

    def  log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            is_found = False
            for video in self.videos:
                if new_video.title == video.title:
                    is_found = True
                    break
            if not is_found:
                self.videos.append(new_video)

    def get_videos(self, word):
        ret = []
        for video in self.videos:
            if video.title.lower().find(word.lower()) != -1:
                ret.append(video.title)
        return ret

    def watch_video(self, name):
         if self.current_user is None:
             print("Войдите в аккаунт, чтобы смотреть видео")
         else:
             for video in self.videos:
                 if video.title == name:
                    if video.adult_mode is True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return
                    for i in range(1, video.duration+1):
                        print(i)
                        time.sleep(1)
                    print('Конец видео')


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # ur.log_in('nick1','pass1')
    # ur.watch_video("video")
    # ur.register('nick1','pass1', 10)
    # ur.watch_video("video")
    # ur.log_out()
    # ur.watch_video("video")
    # ur.register('nick1', 'newpass1', 20)
    # ur.log_in('nick1','pass1')
    # ur.watch_video("Для чего девушкам парень программист?")

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
