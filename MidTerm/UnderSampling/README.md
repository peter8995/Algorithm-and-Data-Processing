```
Best val_accuracy So Far: 1.0
1/1 [==============================] - 0s 16ms/step
Predicted: 1.000
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

 batch_normalization (BatchN  (None, 32)               128
 ormalization)

 re_lu (ReLU)                (None, 32)                0

 dense_1 (Dense)             (None, 32)                1056

 batch_normalization_1 (Batc  (None, 32)               128
 hNormalization)

 re_lu_1 (ReLU)              (None, 32)                0

 dense_2 (Dense)             (None, 1)                 33

 classification_head_1 (Acti  (None, 1)                0
 vation)

=================================================================
Total params: 1,514
Trainable params: 1,377
Non-trainable params: 137
_________________________________________________________________
```