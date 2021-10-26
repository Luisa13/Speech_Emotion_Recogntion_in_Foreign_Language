# Speech Emotion Recognition in a Foreign Language
Is one able to recognize the sentiments behind a conversation in a unknown language? Is is possible to distinguish the same emotions in a foreign language that one does in their mother tongue? The emotional background hidden in the speach is a key factor in the human communication.
This work attemps to performs a speech emotional recognition through three languages. For this purpose, three different models have been implemented and trained in english and subsequently tested in other two languages which never took part in the training (french and german). It is assumed that speech audio signals carry emotional information that can be retrieved  and hence MFCC (Mel-Frecuency Cepstral Coefficients) are extracted since they are recognized as best suited  to represents emotions through prosody. Different classifiers based on convolutional neural network architecture were used. The results show that the CNN-LSTM outperform over the other options with a 92.06% of accuracy in a monolinguistic classification in english with six classes. On the other hand, appliying the same approach in a cross language classification did not deliver satisfactory results.

![image](https://user-images.githubusercontent.com/3811449/138940119-6fc90d68-d81d-4e08-8113-a9c3b6fffb96.png)

![image](https://user-images.githubusercontent.com/3811449/138965337-bf9a3c9e-df0f-44a2-9b29-d9c84f4103d3.png)


![image](https://user-images.githubusercontent.com/3811449/138965191-08856635-c233-4fcb-9320-d9198d69b61d.png)

![image](https://user-images.githubusercontent.com/3811449/138965623-7c42de66-ded6-46dc-931f-ceea3848d3aa.png)








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


### References

### Author and License
Luisa Sanchez Avivar 2021 under licence of [GNU AGPL v 3.0](https://github.com/Luisa13/SpeechEmotionRecognition/blob/master/LICENSE)
