from email.mime import base
from glob import glob
from operator import index
from pydoc import plain
from typing import BinaryIO
from urllib import response
from webbrowser import get
from xml.dom.minidom import Document
from zipfile import ZipFile
from flask import Flask, jsonify, redirect, render_template,request, send_file, url_for
from pytube import YouTube,Playlist
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        url = request.form["txUrl"]
        #qs = url.split('/');
        #print(qs[3])
      #===========================================
      #     DOWNLOADIGN PLAY LISTS
      #===========================================
        if url != '':
            if request.form.get("pl") !=  "1":
                print('this is me at the top')
                print(request.form.get("highres"))
                if request.form.get("highres") ==  "1":
                    yt = YouTube(url).streams.get_highest_resolution()
                else:
                    yt = YouTube(url).streams.get_lowest_resolution()
                
                buffer = BytesIO()
                yt.stream_to_buffer(buffer)
                buffer.seek(0)
                return send_file(
                    buffer,
                    as_attachment=True,
                    attachment_filename = yt.default_filename ,
                    mimetype="video/mp4"
                )
                #print(yt.title)
                #stream =  yt.streams.filter('mp4')
                #stream.download()
                #print(yt.streams)
                #videoid = yt.video_id
                #yt.exists_at_path,yt.title,NULL,True,NULL,NULL
            else:
                if request.form.get("pl") ==  "1":
                    P = Playlist(url)
                    buffer = BytesIO()
                    
                    for video in P.videos:
                        print('getting vids for playlist')
                        print(video.title)
                        if request.form.get("highres") ==  "1":
                            yt = video.streams.get_highest_resolution()
                        else:
                            yt = video.streams.get_lowest_resolution()

                        yt.download('Downloads')

                
                target = 'Downloads'
                with ZipFile(buffer,'w') as zf:
                 for file in glob(os.path.join(target,'*.mp4')):
                    zf.write(file,os.path.basename(file))
                buffer.seek(0)
                return send_file(
                        buffer,
                        as_attachment=True,
                        download_name = 'Archive.zip' ,
                        max_age = 0,
                        )
                        #with youtube_dl.YoutubeDL(options) as y:
                        #    try:
                        #        r = y.extract_info(url, download=False)
                        #        return jsonify(r)
                        #    except:
                        #        return jsonify({'error':'An error has occured'})
                        #yt.download('Downloads')     
                        #yt.stream_to_buffer(buffer)
                        #buffer.seek(0)
                        #v = []
                        #v+= send_file(
                        # buffer,
                        # as_attachment=True,
                        # download_name = yt.default_filename ,
                        # max_age = 0,
                        # mimetype="video/mp4")
                        #return v
                         
                    
            #yt.download()
                #buffer = BytesIO();
                #stream_to_buffer(yt,buffer)
                

                #yt.stream_to_buffer(YouTube(url).streaming_data)
                #buffer =
                #return send_file(
                #    buffer,
                #    as_attachment=True,
                #    attachment_filename=yt.title,
                #    mimetype="video/mp4",
                #)
            
                #return render_template('index.html',test='Downloading .... ')
    else:
        return render_template('index.html')

    



if __name__ == "__main__":
    app.run(debug=True) 