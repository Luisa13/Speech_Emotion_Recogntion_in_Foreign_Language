import librosa
import numpy as np
from tqdm import tqdm
import pandas as pd
import soundfile as sf
import os

class SpeechFeatures():
    def __init__(self, df):
        self.df = df

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
        bar_data_range = tqdm(range(len(self.df)))
        data = pd.DataFrame(columns=['data'])
        for index in bar_data_range:
            data_features = modifier(self.df.path[index])
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
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        mfcc = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40)
        data_features = np.mean(mfcc.T, axis=0)

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
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_wn = self.white_noise(X)
        mfcc = librosa.feature.mfcc(y=x_data_wn, sr=sample_rate, n_mfcc=40)
        data_features = np.mean(mfcc.T, axis=0)

        return data_features

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
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_wn = self.shift_audio_sample(X)
        mfcc = librosa.feature.mfcc(y=x_data_wn, sr=sample_rate, n_mfcc=40)
        data_features = np.mean(mfcc.T, axis=0)

        return data_features

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
        X, sample_rate = librosa.load(pathfile, res_type='kaiser_fast')
        # X = librosa.core.load(random_sample)[0]

        x_data_wn = self.pitch_shift(X)
        mfcc = librosa.feature.mfcc(y=x_data_wn, sr=sample_rate, n_mfcc=40)
        data_features = np.mean(mfcc.T, axis=0)

        return data_features

    def pitch_shift(self, data, bins_per_octave=12, pitch_pm=2):
        '''
        Modula el tono y modifica la velocidad de una pista de audio
        '''
        pitch_change = pitch_pm * 2 * (np.random.uniform())
        data_pitch = librosa.effects.pitch_shift(data.astype('float64'), 16000, n_steps=pitch_change,bins_per_octave=bins_per_octave)

        return data_pitch

    def white_noise(self, data):
        '''
        Agrega ruido blanco a una pista de audio
        '''
        wn_spectrum = np.random.randn(len(data))
        data_wn = data + 0.005 * wn_spectrum
        return data_wn

    def shift_audio_sample(self, data, f_low=-5, f_high=5, spec=1):
        '''
        Desplaza una se;al acustica en un rango de frecuencia
        '''
        d_range = int(np.random.uniform(low=f_low, high=f_high) * spec)
        data_shiftted = np.roll(data, d_range)

        return data_shiftted

    def generate_ravdess_dataAugmentation(self, augmented_path='', pitch=True, stretch=True, step_list={1}, rate_list={1},
                                      verbose=False):
        '''
        Genera archivos de audio basado en las modificaciones que se especifican en los parametros.
        La informacion de las pistas de audio se le pasa al funcion mediante un dataframe.
        '''
        for index, row in self.df.iterrows():
            # Data augmentation basado en desplazar el tono
            if pitch:
                self.save_augmented_pitch(row['path'], step_list, augmented_path + '/' + row['emotion'], index, verbose)
                if verbose:
                    print("Generadas {} muestras de {}".format(len(step_list), row['emotion']))
            # Data augmentation basado en stretching
            if stretch:
                self.save_augmented_stretch(row['path'], rate_list, augmented_path + '/' + row['emotion'], index, verbose)
                if verbose:
                    print("Generadas {} muestras de {}".format(len(rate_list), row['emotion']))


    def save_augmented_pitch(dirdata, step_list, outpath, index, verbose=False):
        '''
        Modifica desplazando el tono una pista de audio y la guarda. Esta funcion
        guarda las pistas generadas creando una carpeta con el nombre de la clase
        a la que pertenece. La modificacion de dicho tono se basa en una lista dada
        en los parametros
        Arguments
        ---------
          dirdata: str
          step_list: list
          outpath: str
        Return
        ---------
          void
        '''
        for i, n_steps in enumerate(step_list):
            y, sr = librosa.load(dirdata, duration=2.97)
            y_changed_pitch = librosa.effects.pitch_shift(y, sr, n_steps=n_steps)
            # outpath = LPATH_AUGMENTED + '/' + row['emotion']
            if not os.path.exists(outpath):
                os.makedirs(outpath)
            filename = outpath + '/augmented_pitch_0' + str(i) + '_0' + str(index) + '.wav'
            sf.write(filename, y_changed_pitch, sr)

    def save_augmented_stretch(dirdata, rate_list, outpath, index, verbose=False):
        '''
        Modifica una pista de audio estirando el tiempo un rango fijado. Dicho rango
        (o rangos) se especifica en una lista como parametro. Esta funcion
        guarda las pistas generadas creando una carpeta con el nombre de la clase
        a la que pertenece
        Arguments
        ---------
          dirdata: str
          step_list: list
          outpath: str
        Return
        ---------
          void

        '''
        for i, rate in enumerate(rate_list):
            y, sr = librosa.load(dirdata, duration=2.97)
            y_changed_shitf = librosa.effects.time_stretch(y, rate=rate)
            # augmented_path = LPATH_AUGMENTED + '/' + row['emotion']
            if not os.path.exists(outpath):
                os.makedirs(outpath)
            filename = outpath + '/augmented_stretch_0' + str(i) + '_0' + str(index) + '.wav'
            sf.write(filename, y_changed_shitf, sr)

