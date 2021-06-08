import librosa
import numpy as np
from tqdm import tqdm
import pandas as pd
import pickle
import os

class MEL():
    '''
    Esta clase gestiona la generacion de las caracteristicas MEL
    '''

    def __init__(self, df_data, outpath=''):
        self.df_data = df_data
        self.outpath = outpath

    def get_features(self, modifier):
        '''
        Extrae las caracteristicas de un conjunto de pistas de audio a
        partir de un dataframe usando librosa

        Aguments
        ---------
          df : dataframe
            Dataframe que contiene el path donde se encuentra la pista de audio
          modifier: Function
            Funcion que modifica los datos

        Return
        -------
        data: np.array
          Caracteristicas extraidas

        '''
        bar_data_range = tqdm(range(len(self.df_data)))
        data = pd.DataFrame(columns=['data'])
        for index in bar_data_range:
            data_features = modifier(self.df_data.path[index])
            data.loc[index] = [data_features]

        return data

    def get_features_single_file(self, pathfile):
        '''
        Extrae las caracteristicas  de una unica pista de audio usando MFCC
        a traves de librosa.

        Aguments
        ---------
          pathfile: str
            Path del archivo del que se extraeran las caracteristicas

        Return
        -------
          data_features

        '''
        data_features = np.array([])
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # mel = librosa.feature.melspectrogram(y=X, sr=sample_rate, n_mels=self.n_features, fmax=8000)
        mel = librosa.feature.melspectrogram(y=X, sr=sample_rate)
        mel = np.mean(mel.T, axis=0)
        data_features = np.hstack((data_features, mel))
        return data_features

    def get_features_white_noise(self, pathfile):
        '''
        Extrae las caracteristicas  de una unica pista de audio usando MFCC
        a traves de librosa habiendoles aplicado ruido blanco.

        Aguments
        ---------
          pathfile: str
            Path del archivo del que se extraeran las caracteristicas

        Return
        -------
          data_features

        '''
        data_features = np.array([])
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_wn = self.white_noise(X)
        mel = librosa.feature.melspectrogram(y=x_data_wn, sr=sample_rate)
        mel = np.mean(mel.T, axis=0)
        data_features = np.hstack((data_features, mel))

        return data_features

    def white_noise(self, data):
        '''
        Agrega ruido blanco a una pista de audio
        '''
        wn_spectrum = np.random.randn(len(data))
        data_wn = data + 0.005 * wn_spectrum
        return data_wn

    def get_features_shiftted(self, pathfile):
        '''
        Extrae las caracteristicas  de una unica pista de audio usando MFCC
        a traves de librosa habiendo desplazado las frecuencias perviamente.

        Aguments
        ---------
          pathfile: str
            Path del archivo del que se extraeran las caracteristicas

        Return
        -------
          data_features

        '''
        data_features = np.array([])
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_sf = self.shift_audio_sample(X)
        mel = librosa.feature.melspectrogram(y=x_data_sf, sr=sample_rate)
        mel = np.mean(mel.T, axis=0)
        data_features = np.hstack((data_features, mel))

        return data_features

    def shift_audio_sample(self, data, f_low=-5, f_high=5, spec=1):
        '''
        Desplaza una señal acustica en un rango de frecuencia
        '''
        d_range = int(np.random.uniform(low=f_low, high=f_high) * spec)
        data_shiftted = np.roll(data, d_range)

        return data_shiftted

    def get_features_pitch(self, pathfile):
        '''
        Aplica modulacion del tono en cada muestra y despues extrae las caracteristicas
        usando el algoritmo MFCC

        Aguments
        ---------
          pathfile: str
            Path del archivo del que se extraeran las caracteristicas

        Return
        -------
          data_features

        '''
        data_features = np.array([])
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_pt = self.pitch_shift(X)
        mel = librosa.feature.melspectrogram(y=x_data_pt, sr=sample_rate)
        mel = np.mean(mel.T, axis=0)
        data_features = np.hstack((data_features, mel))

        return data_features

    def pitch_shift(self, data, bins_per_octave=12, pitch_pm=2):
        '''
        Modula el tono y modifica la velocidad de una pista de audio
        '''
        pitch_change = pitch_pm * 2 * (np.random.uniform())
        data_pitch = librosa.effects.pitch_shift(data.astype('float64'), 16000, n_steps=pitch_change,
                                                 bins_per_octave=bins_per_octave)
        return data_pitch

    def read_features_dataAugmentation(self):
        '''
        Devuelve y guarda en formato pkl de manera independiente las caracteristicas
        con tecnicas de aumento de datos
        '''
        # Leemos las caracteristicas estandar (sin data augmentation)
        features_standard = self.get_features(self.get_features_single_file)
        try:
            pickle.dump(features_standard, open(self.outpath + 'featuresMEL_standard_RAVDESS.pkl', 'wb'))
        except Exception as ex:
            print(ex)
        print("Caracteristicas estandar serializadas")
        # Leemos para Ruido Blanco
        features_wn = self.get_features(self.get_features_white_noise)
        try:
            pickle.dump(features_wn, open(self.outpath + 'featuresMEL_wn_RAVDESS.pkl', 'wb'))
        except Exception as ex:
            print(ex)
        print("Caracteristicas con ruido blanco serializadas")

        # Leemos para Desplazamiento del Sonido
        features_shiftted = self.get_features(self.get_features_shiftted)
        try:
            pickle.dump(features_shiftted, open(self.outpath + 'featuresMEL_shiftted_RAVDESS.pkl', 'wb'))
        except Exception as ex:
            print(ex)
        print("Caracteristicas con desplazamiento serializadas")

        # Leemos para Modificacion del Tono
        features_pitch = self.get_features(self.get_features_pitch)
        try:
            pickle.dump(features_pitch, open(self.outpath + 'featuresMEL_pitch_RAVDESS.pkl', 'wb'))
        except Exception as ex:
            print(ex)
        print("Caracteristicas con modulacion del tono serializadas")

        return features_standard, features_wn, features_shiftted, features_pitch

