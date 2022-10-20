# In[ ]:


# convert class labels from strings to integers
label_encoder = LabelEncoder()
label_encoder = label_encoder.fit(y)
label_encoded_y = label_encoder.transform(y)


# In[ ]:


# convert integers into dummy variables (i.e. one hot encoded)
one_hot_y = np_utils.to_categorical(label_encoded_y)


# In[ ]:


# one hot encode inputs
one_hot_x = one_hot_encoder.fit_transform(X)


# In[ ]:


# create model
model = Sequential()
model.add(Dense(10, input_dim=one_hot_x.shape[1], activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(one_hot_y.shape[1], activation='softmax'))


# In[ ]:


# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[ ]:


# Fit the model
model.fit(one_hot_x, one_hot_y, epochs=50, batch_size=10)


# In[ ]:


# evaluate the model
scores = model.evaluate(one_hot_x, one_hot_y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[ ]:


# calculate predictions
predictions = model.predict(one_hot_x)


# In[ ]:


# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)


# In[ ]:


# create model
model = Sequential()
model.add(Dense(10, input_dim=one_hot_x.shape[1], activation='relu'))
model.add(Dense(10, activation='relu'))