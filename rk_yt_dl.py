from pytube import YouTube
from hurry.filesize import size

def rk_downloader(url):
    try:
        yt = YouTube(url)
        bcs = yt.streams.get_highest_resolution()
        gn_data = {
            'title': bcs.title,
            'filename': str(bcs.title)+'_'+(bcs.resolution)+'.mp4',
            'size': size(bcs.filesize),
            'resolution': bcs.resolution,
            'url': bcs.url,
            'thumb': yt.thumbnail_url,
            'status': True
        }
    except Exception as e:
        gn_data = {'error': str(e), 'status': False}
    
    return gn_data