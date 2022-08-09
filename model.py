










## Saving the model to disk
pickle.dump(classifier,open('model.pkl','wb'))

## Load the model to compare the result
model = pickle.load(open('model.pkl','rb'))

## Call model to predict
data = [3,3,3,1.0,2,1,1,52]



##CHANGE THE INPUT TO NUMPY ARRAY
input_data_as_numpy_array = np.asarray(data)
#RESHAPE THE NUMPY ARRAY BECAUSE WE NEED TO PREDICT THE TARGET
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler2.fit_transform(input_data_reshaped)
prediction = model.predict(input_data_reshaped)
if prediction[0] == 0:
    print('The patient does not have a Diabetes')
else:
    print('The patient has a Diabetes')

print(prediction)
