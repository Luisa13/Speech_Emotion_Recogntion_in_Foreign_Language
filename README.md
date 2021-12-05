# Speech Emotion Recognition in a Foreign Language
Is one able to recognize the sentiments behind a conversation in a unknown language? Is is possible to distinguish the same emotions in a foreign language that one does in their mother tongue? The emotional background hidden in the speach is a key factor in the human communication.
This work attemps to performs a speech emotional recognition through three languages. For this purpose, three different models have been implemented and trained in english and subsequently tested in other two languages which never took part in the training (french and german). It is assumed that speech audio signals carry emotional information that can be retrieved  and hence MFCC (Mel-Frecuency Cepstral Coefficients) are extracted since they are recognized as best suited  to represents emotions through prosody. Different classifiers based on convolutional neural network architecture were used. The results show that the CNN-LSTM outperform over the other options with a 92.06% of accuracy in a monolinguistic classification in english with six classes. On the other hand, appliying the same approach in a cross language classification did not deliver satisfactory results.

![image](https://user-images.githubusercontent.com/3811449/138940119-6fc90d68-d81d-4e08-8113-a9c3b6fffb96.png)

*system proposal*


![image](https://user-images.githubusercontent.com/3811449/138965337-bf9a3c9e-df0f-44a2-9b29-d9c84f4103d3.png)

*Architechture based on unidimensional CNN and corresponding performance*

![image](https://user-images.githubusercontent.com/3811449/138965191-08856635-c233-4fcb-9320-d9198d69b61d.png)

*Architechture based on bidimensional CNN and corresponding performance*

![image](https://user-images.githubusercontent.com/3811449/138965623-7c42de66-ded6-46dc-931f-ceea3848d3aa.png)

*Architechture based on bidimensional CNN - LSTM and corresponding performance*



### Datasets for training
- **SAVEE** : (*Surrey Audio-Visual Expressed Emotion*)  It is an emotion recognition dataset that consists of recordings from 4 male actors in 7 different emotions, 480 British English utterances in total. The sentences were chosen from the standard TIMIT corpus and phonetically-balanced for each emotion [[1]](#1).

- **TESS** : (*Toronto emotional speech set* ) Set of 200 target words were spoken in the carrier phrase "Say the word__ " by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions (anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 data points (audio files) in total [[2]](#2)..

### Datasets for test
- **EMO-DB**: It's the freely available German emotional database. The database is created by the Institute of Communication Science, Technical University, Berlin, Germany. The database contains a total of 535 utterances. The EMODB database comprises of seven emotions: 1) anger; 2) boredom; 3) anxiety; 4) happiness; 5) sadness; 6) disgust; and 7) neutral. The data was recorded at a 48-kHz sampling rate and then down-sampled to 16-kHz.

- **CaFE**: ( _Canadian French Emotional_) This speech dataset contains six different sentences, pronounced by six male and six female actors, in six basic emotions plus one neutral emotion. The six basic emotions are acted in two different intensities. It's [freely available](https://zenodo.org/record/1478765#.YazF8KTMIrg) under a Creative Commons license (CC BY-NC-SA 4.0) and was digitally recorded at a high-resolution (192 kHz sampling rate, 24 bits per sample).

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

<a id="1">[1]</a>  Jackson P., & ul Haq S. (2011). [Surrey Audio-Visual Expressed Emotion (SAVEE) database](http://kahlan.eps.surrey.ac.uk/savee/).

<a id="2">[2]</a>  Kate Dupuis, M. Kathleen Pichora-Fuller (2010), University of Toronto, Psychology Department. [doi.org/10.5683/SP2/E8H2MF](https://tspace.library.utoronto.ca/handle/1807/24487)


### Author and License
Luisa Sanchez Avivar 2021 under licence of [GNU AGPL v 3.0](https://github.com/Luisa13/SpeechEmotionRecognition/blob/master/LICENSE)
