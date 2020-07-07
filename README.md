# object_detection

## https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
## https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85
## https://github.com/datitran/raccoon_dataset
## Gather Images, split train/test = 80/20 or 90/10
### `python transform_image_resolution.py -d images/train/ -s 800 600`
### `python transform_image_resolution.py -d images/test/ -s 800 600`
## ImgLabel
### `python xml_to_csv.py`
### This creates two files in the images directory:
#### test_labels.csv
#### train_labels.csv
### Before we can transform the newly created files to TFRecords we need to change a few lines in the generate_tfrecords.py file.
```python
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
```


```js
var a = {};
```