## LAST TECHNICAL REFERENCES
Nombre | Descripcion | Codigo   | Tutorial
-------|-------------|----------|-------
**Tushar** |RAVDESS with CNN and MFCC and mel spectograms with 1d cnn. Also compares other algo. applied to the same problem liek VGG16.|[github](https://github.com/tushar2025/Speech-Emotion-Detection)| [tutorial](https://medium.com/@tushar.gupta_47854/speech-emotion-detection-74337966cf2)
**DiegoErios**| TESS + RAVDESS en una complicada arquitectura CNN 1D consigue un 73.00 |[github](https://github.com/diegoerios/capstoneproject-speech-emotion-machine-learning/blob/master/speech_emotion_final_notebook.ipynb)| [tutorial](https://medium.com/@diego-rios/speech-emotion-recognition-with-convolutional-neural-network-ae5406a1c0f7)
**Kaggle RAVDESS** | Hace una mezcla de datasets, entre ellos RAVDESS, extrae MEL y MFCC y entrena con **CNN 2D**. 66% acc | [kaggle](https://www.kaggle.com/yfliao/audio-emotion-part-6-2d-cnn-66-accuracy)  |  X  
**RAVDESS 2D CNN comparator** | complejisimo pero completo proyecto usando RAVDESS con diferentes enfoques en CNN 2D, pero usa pytorch|[github](https://github.com/Data-Science-kosta/Speech-Emotion-Classification-with-PyTorch/blob/master/notebooks/stacked_cnn_attention_lstm.ipynb)| X
**Mkosaka** |RAVDESS con mel y MFCC con 1d y 2d. Implementa bastantes modelos entre ellos VG16. Muy recomendable, aunque la forma que tiene de leer las imagenes es confusa |[github](https://github.com/mkosaka1/Speech_Emotion_Recognition) | X
**RAVDESS Transformer** | Muy muy complejo. Modelo usa transformer y CNN sobre RAVDESS que es aumentado con AWGN | [github](https://github.com/IliaZenkov/transformer-cnn-emotion-recognition)| X
**Ayushgoal** | RAVDESS y SAVEE con tecnicas de data augmentation y cnn y lstm (2D)| [github](https://github.com/ayushgoyal7796/Speech-Emotion-Recognition) | X
**BAIABAIA** | ser cross language techniques |[github](https://github.com/aascode/Speech-Emotion-Recognition-4)| X




## TODO
* -[ ] Read [this article](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) about feature importance, extract information and write the corresponding conclusion 
 
* ### English
The goal is to get an accuracy good enough to extend it to the other languages
* -[x] 1_SER_RAVDESS_English
* -[x] 2_SER_RAVDESS_English_Simplified
* -[ ] Why RMS (what's RMS, which type of problems it solves, why's better the the other one) [see](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)
* -[x] 3_SER_RAVDESS_English_Augmentation
* -[ ] Load correctly h5 feature files
* -[x] 3_SER_RAVDESS_English_Tunning


**GENERAL TODO**
* [ ] Titles and seccions definitions
* [ ] Clean code up and SPANISH
* [ ] Explain how number of features affect to the overfitting
* [ ] 
</br>



## REFERENCES
#### Technical Examples
 * [Dummys Guide to MFCC](https://medium.com/prathena/the-dummys-guide-to-mfcc-aceab2450fd)
 * [SER python project](https://towardsdatascience.com/building-a-speech-emotion-recognizer-using-python-4c1c7c89d713): Consigue un 79.3 y explica MEL y MFCC
 * [FrontEnd for Audio Classification - GoogleAI](https://ai.googleblog.com/2021/03/leaf-learnable-frontend-for-audio.html?m=1)
 * [Breaking down the components in SER](https://towardsdatascience.com/automatic-speech-recognition-breaking-down-components-of-speech-85d065061517)
 * [TF audio processing](https://www.tensorflow.org/tutorials/audio/simple_audio)
 * [Speedometer gauge component in ReactJS](https://github.com/palerdot/react-d3-speedometer)
 * [SER EDA](https://github.com/rajamohanharesh/Emotion-Recognition/tree/master/Codes)
 

#### Agumentation Techniques
* [Data Augmentation for speech recognition](https://towardsdatascience.com/data-augmentation-for-speech-recognition-e7c607482e78)
* [Data Augmentation for Audio](https://medium.com/@makcedward/data-augmentation-for-audio-76912b01fdf6)
* [D.A. examples in kaggle](https://www.kaggle.com/CVxTz/audio-data-augmentation)
* [Augmentation methods](https://www.kaggle.com/haqishen/augmentation-methods-for-audio)
* [Flask + React application for ML](https://thevatsalsaglani.medium.com/training-and-deploying-a-multi-label-image-classifier-using-pytorch-flask-reactjs-and-firebase-28c6150c04c)

### Datasets
- [SER Datasets](https://github.com/SuperKogito/SER-datasets)
- [Persian Dataset](https://www.kaggle.com/mansourehk/shemo-persian-speech-emotion-detection-database)
- [datasets search in kaggle](https://www.kaggle.com/search?q=dataset+speech+emotion+recognition+in%3Adatasets)

#### ML Organization
* [Organinzing ML project](https://www.jeremyjordan.me/ml-projects-guide/)
* [CookieCutter: Structure dataScience project](https://drivendata.github.io/cookiecutter-data-science/)
* [ML project structure template](https://github.com/ThomasRobertFr/ml-project-structure)
* [create ml app](https://github.com/shreyashankar/create-ml-app)

* [Peer Review](https://www.kdnuggets.com/2020/04/peer-reviewing-data-science-projects.html) A collection of questions to ensure the correctness of results
