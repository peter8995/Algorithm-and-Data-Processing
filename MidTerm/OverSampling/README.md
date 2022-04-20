```
147/147 [==============================] - 1s 5ms/step - loss: 0.2508 - accuracy: 0.8922
consider avoiding using them.
Accuracy: 0.920
1/1 [==============================] - 0s 11ms/step
Predicted: 0.000
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 input_1 (InputLayer)        [(None, 4)]               0

 multi_category_encoding (Mu  (None, 4)                0
 ltiCategoryEncoding)

 normalization (Normalizatio  (None, 4)                9
 n)

 dense (Dense)               (None, 32)                160

 re_lu (ReLU)                (None, 32)                0

 dense_1 (Dense)             (None, 32)                1056

 re_lu_1 (ReLU)              (None, 32)                0

 dense_2 (Dense)             (None, 1)                 33

 classification_head_1 (Acti  (None, 1)                0
 vation)

=================================================================
Total params: 1,258
Trainable params: 1,249
Non-trainable params: 9
```