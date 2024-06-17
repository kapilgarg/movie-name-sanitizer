import spacy

_sanitizer = spacy.load('movie-name-sanitizer')

def sanitize(name:str) -> dict :
    """
    Sanitize the torrent name of a movie returns a dictionary containing details extracted from name.
    ex:
    name : [TorrentCounter.to].Tumbbad.2018.Hindi.1080p.WEB-DL.x264.[1.5GB].[MP4]
    returns : 
    {
        'movie': 'tumbbad', 
        'year': '2018', 
        'resolution': '1080p', 
        'quality': 'web-dl',         
    }    
    """
    
    name = name.replace("."," ").lower()
    doc = _sanitizer(name)
    data = {}
    for ent in doc.ents:
        data[ent.label_] = ent.text
    return data


 

