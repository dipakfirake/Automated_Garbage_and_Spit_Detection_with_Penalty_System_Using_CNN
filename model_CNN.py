import numpy as np

import os
from PIL import Image
from numpy import *


# input image dimensions
img_rows, img_cols = 224, 224

# number of channels
img_channels = 3

#%%
#  data

path1 = r'd:/sarasvati biradar/SarasvatiBitmap 24-25/24c9333-Automated Garbage and spit detection/100% code/Garbage and spit detection/data/0'    #path of folder of images    
path2 = r'd:/sarasvati biradar/SarasvatiBitmap 24-25/24c9333-Automated Garbage and spit detection/100% code/Garbage and spit detection/0'  #path of folder to save images    

listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "JPEG")

imlist = os.listdir(path2)

im1 = array(Image.open('input_data_resized/' + imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# # create matrix to store all flattened images
# immatrix = array([array(Image.open('input_data_resized/'+ im2)).flatten()
#               for im2 in imlist],'f')
               
# label=np.ones((num_samples,),dtype = int)
# label[0:245]=0
# label[245:288]=1


# size(label)

# data,Label = shuffle(immatrix,label, random_state=2)
# train_data = [data,Label]

# img=immatrix[439].reshape(img_rows,img_cols)
# # plt.imshow(img)
# # plt.imshow(img,cmap='gray')
# print (train_data[0].shape)
# print (train_data[1].shape)

# #%%

# #batch_size to train
# batch_size = 32
# # number of output classes
# nb_classes = 7
# # number of epochs to train
# nb_epoch = 100


# # number of convolutional filters to use
# nb_filters = 64
# # size of pooling area for max pooling
# nb_pool = 2
# # convolution kernel size
# nb_conv = 3

# #%%
# (X, y) = (train_data[0],train_data[1])


# # STEP 1: split X and y into training and testing sets

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols , 1)
# X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols , 1)

# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')

# X_train /= 255
# X_test /= 255

# print('X_train shape:', X_train.shape)
# print(X_train.shape[0], 'train samples')
# print(X_test.shape[0], 'test samples')

# # convert class vectors to binary class matrices
# Y_train = np_utils.to_categorical(y_train, nb_classes)
# Y_test = np_utils.to_categorical(y_test, nb_classes)

# i = 20
# #plt.imshow(X_train[i, 0], interpolation='nearest')
# print("label : ", Y_train[i,:])

# #%%

# model = Sequential()

# # #model.add(Convolution2D(nb_filters, nb_conv, nb_conv, padding='same',input_shape=(1, img_rows, img_cols)))
# # model.add(Convolution2D(64,3, 3, strides=(4, 4), padding='same',input_shape=(1, img_rows, img_cols), activation='relu'))
# # convout1 = Activation('relu')
# # model.add(convout1)
# # model.add(Convolution2D(nb_filters, nb_conv, nb_conv))
# # convout2 = Activation('relu')
# # model.add(convout2)
# # model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
# # model.add(Dropout(0.5))

# # model.add(Flatten())
# # model.add(Dense(128))
# # model.add(Activation('relu'))
# # model.add(Dropout(0.5))
# # model.add(Dense(nb_classes))
# # model.add(Activation('softmax'))
# # model.compile(loss='categorical_crossentropy', optimizer='adadelta')
# # model.add(Conv2D(
# #         96, 11, strides=(4, 4), input_shape=(IMAGE_SIZE, IMAGE_SIZE, CHANNELS), activation='relu'))
# # model.add(MaxPooling2D(pool_size=(3, 3), strides=2))
# # model.add(BatchNormalization())

# #     # Second Convolution Block
# # model.add(Conv2D(256, 5, strides=(1, 1),
# #                           activation='relu', padding='same'))
# # model.add(MaxPooling2D(pool_size=(3, 3), strides=2))
# # model.add(BatchNormalization())

# #     # Third Convolution Block
# # model.add(Conv2D(384, 3, strides=(1, 1),
# #                           activation='relu', padding='same'))
# # model.add(MaxPooling2D(pool_size=(3, 3), strides=2))

# #     # Fourth Convolution Block
# # model.add(Conv2D(384, 3, strides=(1, 1),
# #                           activation='relu', padding='same'))

# #     # Fifth Convolution Block
# # model.add(Conv2D(256, 3, strides=(1, 1),
# #                           activation='relu', padding='same'))
# # model.add(Dropout(0.5))

# #     # Fully connected layer
# # model.add(Flatten())

# #     # First hidden unit
# # model.add(Dense(512, activation='relu', kernel_initializer='uniform'))
# # model.add(Dropout(0.5))

# #     # Second hidden unit
# # model.add(Dense(512, activation='relu', kernel_initializer='uniform'))
# # model.add(Dropout(0.5))

# #     # Output layer
# # model.add(Dense(CLASSES, activation='softmax',
# #                          kernel_initializer='uniform'))

# # model.summary()
# LEARN_RATE = 1.0e-4
#  # Model Architecture and Compilation
# model = AlexNet(7, 200, 1)
# adam = Adam(lr=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
# model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
    
# from keras.callbacks import ModelCheckpoint 
# from keras import callbacks
    
# filename='model_train_new.csv'
# csv_log=callbacks.CSVLogger(filename, separator=',', append=False)

# early_stopping=callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=0, verbose=0, mode='min')
# checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True, mode='auto')
    
# #steps_per_epoch = int(len(Y_train) / BATCH_SIZE)  # 300
# #    validation_steps = int(len(Y_test) / BATCH_SIZE)  # 90
    
# callbacks_list = [csv_log,early_stopping,checkpoint]
# #%%

# hist = model.fit(X_train, Y_train, batch_size=batch_size, epochs=100,
#               verbose=1, validation_data=(X_test, Y_test))



# model.save('best_model.h5')
# model.save('best_model_CSV.csv')
# # hist = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch,
# #               show_accuracy=True, verbose=1, validation_split=0.2)


# # visualizing losses and accuracy

# train_loss=hist.history['loss']
# val_loss=hist.history['val_loss']
# train_acc=hist.history['accuracy']
# val_acc=hist.history['val_accuracy']
# xc=range(nb_epoch)

# # plt.figure(1,figsize=(7,5))
# # plt.plot(xc,train_loss)
# # plt.plot(xc,val_loss)
# # plt.xlabel('num of Epochs')
# # plt.ylabel('loss')
# # plt.title('train_loss vs val_loss')
# # plt.grid(True)
# # plt.legend(['train','val'])
# # print(plt.style.available) # use bmh, classic,ggplot for big pictures
# # plt.style.use(['classic'])

# # plt.figure(2,figsize=(7,5))
# # plt.plot(xc,train_acc)
# # plt.plot(xc,val_acc)
# # plt.xlabel('num of Epochs')
# # plt.ylabel('accuracy')
# # plt.title('train_acc vs val_acc')
# # plt.grid(True)
# # plt.legend(['train','val'],loc=4)
# # #print plt.style.available # use bmh, classic,ggplot for big pictures
# # plt.style.use(['classic'])




# #%%      

# score = model.evaluate(X_test, Y_test, verbose=0)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])
# print(model.predict_classes(X_test[1:20]))
# print(Y_test[1:20])



# #%%

# # visualizing intermediate layers

# # output_layer = model.layers[1].get_output()
# # output_fn = theano.function([model.layers[0].get_input()], output_layer)

# # # the input image

# # input_image=X_train[0:1,:,:,:]
# # print(input_image.shape)

# # plt.imshow(input_image[0,0,:,:],cmap ='gray')
# # plt.imshow(input_image[0,0,:,:])


# # output_image = output_fn(input_image)
# # print(output_image.shape)

# # # Rearrange dimension so we can plot the result 
# # output_image = np.rollaxis(np.rollaxis(output_image, 3, 1), 3, 1)
# # print(output_image.shape)


# # fig=plt.figure(figsize=(8,8))
# # for i in range(32):
# #     ax = fig.add_subplot(6, 6, i+1)
# #     #ax.imshow(output_image[0,:,:,i],interpolation='nearest' ) #to see the first filter
# #     ax.imshow(output_image[0,:,:,i],cmap=matplotlib.cm.gray)
# #     plt.xticks(np.array([]))
# #     plt.yticks(np.array([]))
# #     plt.tight_layout()
# # plt

# # Confusion Matrix

# from sklearn.metrics import classification_report,confusion_matrix

# Y_pred = model.predict(X_test)
# print(Y_pred)
# y_pred = np.argmax(Y_pred, axis=1)
# print(y_pred)
 
# #                        (or)

# # y_pred = model.predict_classes(X_test)
# # print(y_pred)

# p=model.predict(X_test) # to predict probability

# target_names = ['class 0(Normal)', 
#                 'class 1(Abnormal_Agenesis_of_the_Corpus_Callosum)',
#                 'class 2(Abnormal_Agenesis_of_the_Septi_Pellucidi)',
#                 'class 3(Abnormal_Cerebellar_Hypoplasia)',
#                 'class 4(Abnormal_Dandy_Walker_VariantMalformation)',
#                 'class 5(Abnormal_Megacisterna_Magna)',
#                 'class 6(Abnormal_Venous_Malformation)']
# size(target_names)
# print(classification_report(np.argmax(Y_test,axis=1), y_pred,target_names=target_names))
# print(confusion_matrix(np.argmax(Y_test,axis=1), y_pred))

# # saving weights

# fname = "weights-Test-CNN.h5"
# model.save_weights(fname,overwrite=True)



# # Loading weights

# fname = "weights-Test-CNN.h5"
# model.load_weights(fname)