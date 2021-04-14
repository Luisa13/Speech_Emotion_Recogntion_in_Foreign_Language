
## TODO
* -[ ] Read [this article](https://towardsdatascience.com/how-i-understood-what-features-to-consider-while-training-audio-files-eedfb6e9002b) about feature importance, extract information and write the corresponding conclusion 
 
* ### English
The goal is to get an accuracy good enough to extend it to the other languages
* -[x] **1_SER_RAVDESS_English:**
* -[X] Why SGD (what's SGD, which type of problems it solves)
> * Split data set by gender
> * Use SGD as optimizer
> * Result: Got 55% accuracy and highly overfitted
> * -[X] Accuracy and loss plots in one row
> * -[X] Shows prediction table

* -[x] **2_SER_RAVDESS_English_Simplified:**
> * Simplified the model
> * RMS as optimizer
> * -[x] Accuracy and loss plots in one row
> * -[X] sparse_categorical_crossentropy? [consider this](https://datascience.stackexchange.com/questions/41921/sparse-categorical-crossentropy-vs-categorical-crossentropy-keras-accuracy) (inly format issues)
> * -[X] Shows prediction table
 * -[ ] Why RMS (what's RMS, which type of problems it solves, why's better the the other one) [see](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)

* -[x] **3_SER_RAVDESS_English_Augmentation**
* -[ ] Load correctly h5 feature files

> * [X] Audio sample to play
> * [X] Shiftting: whole experiment
> * [X] Pitch tuning: whole experiment
> * [X] White noise: whole experiment
> * [x] Combination pitch and shiftting: Whole experiment
> * -[X] Split experiment with tunning
> * -[X] Add readme
> * -[X] Save new images with corrected y_test
* [ ] Explain how number of features affect to the overfitting

* -[x] **3_SER_RAVDESS_English_Tunning**
* -[X] Add L2 Regularization
* -[ ] Add lrfn
* -[ ] Add lrfn + early stopping
* -[ ] Add lrlrp + early stopping + lrfn

* ### Add Another Language

**GENERAL TODO**
* [ ] Explain dataset RAVDESS
* [ ] Titles and seccions definitions
* [ ] Clean code up and SPANISH


## REFERENCES
#### Technical Examples
 * [SER python project](https://towardsdatascience.com/building-a-speech-emotion-recognizer-using-python-4c1c7c89d713): Consigue un 79.3 y explica MEL y MFCC
 * [FrontEnd for Audio Classification - GoogleAI](https://ai.googleblog.com/2021/03/leaf-learnable-frontend-for-audio.html?m=1)
 * [Breaking down the components in SER](https://towardsdatascience.com/automatic-speech-recognition-breaking-down-components-of-speech-85d065061517)
 * [TF audio processing](https://www.tensorflow.org/tutorials/audio/simple_audio)

#### Agumentation Techniques
* [Data Augmentation for speech recognition](https://towardsdatascience.com/data-augmentation-for-speech-recognition-e7c607482e78)
* [Data Augmentation for Audio](https://medium.com/@makcedward/data-augmentation-for-audio-76912b01fdf6)
* [D.A. examples in kaggle](https://www.kaggle.com/CVxTz/audio-data-augmentation)
* [Augmentation methods](https://www.kaggle.com/haqishen/augmentation-methods-for-audio)

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
