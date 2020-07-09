# object_detection

## https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
## https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85
## https://github.com/datitran/raccoon_dataset
## Gather Images, split train/test = 80/20 or 90/10
### train, file1-file80
### test, file81-file100
### `python transform_image_resolution.py -d images/train/ -s 800 600`
### `python transform_image_resolution.py -d images/test/ -s 800 600`
## ImgLabel https://github.com/tzutalin/labelImg
### `cd ~/labelImg`
### In data/predefined_classes.txt define the list of classes that will be used for your training.
### `python labelImg.py`
### `python xml_to_csv.py`
### This creates two files in the images directory:
#### test_labels.csv
#### train_labels.csv
### Before we can transform the newly created files to TFRecords we need to change a few lines in the generate_tfrecords.py file.
~~~~{.python}
def class_text_to_int(row_label):
    if row_label == 'Raspberry_Pi_3':
        return 1
    elif row_label == 'Arduino_Nano':
        return 2
    elif row_label == 'ESP8266':
        return 3
    elif row_label == 'Heltec_ESP32_Lora':
        return 4
    else:
        return None
~~~~
### Now the TFRecords can be generated by typing:
### `python generate_tfrecord.py --csv_input=data/train_labels.csv --image_dir=images/train --output_path=train.record`
### `python generate_tfrecord.py --csv_input=data/test_labels.csv --image_dir=images/test --output_path=test.record`

### Creating a label map
#### The label map maps an id to a name. We will put it in a folder called training, which is located in the object_detection directory. The labelmap for my detector can be seen below.
```javascript
item {
    id: 1
    name: 'Steel_Pole'
}
item {
    id: 2
    name: 'Wood_Pole'
}
```
#### The id number of each item should match the id of specified in the generate_tfrecord.py file.


https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs