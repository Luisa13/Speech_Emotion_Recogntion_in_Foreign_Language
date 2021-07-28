# Speech Emotion Recognition in a Foreign Language
Classify and recognize emotions through vi%e signal in a foreign language
This work attemps to performs a speech emotional recognition through three languages. For this purpose, three different models have been implemented and trained in english and subsequently tested in other two languages which never took part in the training (french and german). It is assumed that speech audio signals carry emotional information that can be retrieved  and hence MFCC (Mel-Frecuency Cepstral Coefficients) are extracted since they are recognized as best suited  to represents emotions through prosody. Different classifiers based on convolutional neural network architecture were used. The results show that the CNN-LSTM outperform over the other options with a 92.06% of accuracy in a monolinguistic classification in english. On the other hand, appliying the same approach in a cross language classification did not deliver satisfactory results.

### Requirements
* Python 3.6 or higher
* Librosa 0.8.1
* Tensorflow 2.0
* OpenCV 3.4.2

### Project Structure
```
Project
|_______data
|       |_______processed
|       |_______raw
|_______models
|_______notebook
|_______reports
|_______src
       |_______data
       |_______features
       |_______model
```




### Author and License
Luisa Sanchez Avivar 2021 under licence of [GNU AGPL v 3.0](https://github.com/Luisa13/SpeechEmotionRecognition/blob/master/LICENSE)
