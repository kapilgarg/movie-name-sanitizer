# movie-name-sanitizer
Extract movie name from torrent-style file names.
It Uses spacy's ner model, trained with data to regocnize movie names from torrent style file names
## Train Model
**1. data format**
```
    data_train  = [
      ('Minions The Rise of Gru 2022 BluRay ReMux 1080p AVC TrueHD 7.1 DTS AC3-MgB.mkv (22294327228 bytes)'
        {
          'entities': [
            (0, 23, 'movie')
          ]
        }),
      
      ('Oppenheimer.2023.1080p.LM.HD-TeleSync.DUAL.DD2.0.H.264-xCLuMsYx.mkv',
       {
         'entities': [
           (0, 11, 'movie')
         ]
       })
    ]
```
## Extract movie name from a file name
```
import spacy
_sanitizer = spacy.load('movie-name-sanitizer')

name = filename.replace(".", " ").lower()
doc = _sanitizer(name)
data = {}
for ent in doc.ents:
    data[ent.label_] = ent.text
return data

```

<img src="/images/sanitizer.gif" width="75%">  
