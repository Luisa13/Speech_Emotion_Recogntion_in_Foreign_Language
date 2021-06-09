import pandas as pd
import os

class SpeechDataProcess():
    '''
    Gestiona las diferentes bases de datos para el reconocimiento de emociones.
    Cuando se instancia el objeto se debe proveer el nombre del dataset.
    Datasets actualmente soportados:
    - RAVDESS
    - SAVEE
    - TESS

    '''
    def __init__(self, database_name, path = ''):
        self.path = path
        self.database_name = database_name
        self.DATABASES = {'RAVDESS', 'SAVEE', 'TESS'}

    def read(self):
        '''
        Devuelve en un dataframe con la estructura [emotion, path] la base de datos.
        :return: DataFrame
        '''
        if self.database_name not in self.DATABASE:
            print("Error: Esa base de datos no esta soportada :(\n")
            return pd.DataFrame()

        if self.database_name == self.DATABASES[0]:
            return self.__read_RAVDESS()
        elif self.database_name == self.DATABASES[1]:
            return self.__read_SAVEE()
        elif self.database_name == self.DATABASE[2]:
            return self.__read_TESS()


    def __read_RAVDESS(self):
        '''

        :return:
        '''
        emotion = []
        path = []

        # Extraemos de cada archivo de sonido sus datos
        for dir in os.listdir(self.path):
            path_dir = os.listdir(self.path + dir)  # todos los archivos de audios asociados a un directorio
            for filepath in path_dir:
                info_vector = filepath.split('.')[0].split('-')
                n_emotion = int(info_vector[2])
                str_path = self.path + dir + '/' + str(filepath)
                path.append(str_path)
                emotion.append(n_emotion)

        df = pd.DataFrame(columns=['emotion', 'path'])
        df['emotion'] = emotion
        df['path'] = path
        return df

    def __read_SAVEE(self):
        '''

        :return:
        '''
        emotion = []
        path = []

        for dir in os.listdir(self.path):
            path_dir = os.listdir(self.path + dir)  # todos los archivos de audios asociados a un directorio
            for filename in path_dir:
                str_path = self.path + dir + '/' + str(filename)
                path.append(str_path)
                if filename[0] == 'a':
                    emotion.append("angry")
                elif filename[0] == 'h':
                    emotion.append("happy")
                elif filename[0] == 'f':
                    emotion.append("fear")
                elif filename[0] == 'd':
                    emotion.append("disgust")
                elif filename[0] == 'n':
                    emotion.append('neutral')
                elif filename[0] == 's':
                    if filename[1] == 'a':
                        emotion.append("sad")
                    elif filename[1] == 'u':
                        emotion.append("surprise")

        df = pd.DataFrame(columns=['emotion', 'path'])
        df['emotion'] = emotion
        df['path'] = path
        return df


    def __read_TESS(self):
        '''

        :return: DataFrame
        '''
        emotion = []
        path = []

        for dir in os.listdir(self.path):
            path_dir = os.listdir(self.path + dir)  # todos los archivos de audios asociados a un directorio
            label = dir.split('_')[1]
            for filename in path_dir:
                str_path = self.path + dir + '/' + str(filename)
                path.append(str_path)
                emotion.append(label.lower())

        df = pd.DataFrame(columns=['emotion', 'path'])
        df['emotion'] = emotion
        df['path'] = path
        return df