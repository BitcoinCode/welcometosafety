from typing import BinaryIO
from urllib import response
from xml.dom.minidom import Document
from flask import Flask, redirect, render_template,request, send_file
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        url = request.form["txUrl"]
        #qs = url.split('/');
        #print(qs[3])
      
        if url != '':
            if request.form.get("highres") ==  "1":
                yt = YouTube(url).streams.get_highest_resolution()
            else:
                yt = YouTube(url).streams.get_lowest_resolution()
            
            #print(yt.title)
            #stream =  yt.streams.filter('mp4')
            #stream.download()
            #print(yt.streams)
            #videoid = yt.video_id
            #yt.exists_at_path,yt.title,NULL,True,NULL,NULL
           
            #yt.download()
            #buffer = BytesIO();
            #stream_to_buffer(yt,buffer)
            buffer = BytesIO()
            yt.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(
                buffer,
                as_attachment=True,
                attachment_filename = yt.default_filename ,
                mimetype="video/mp4"
            )

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
    app.run() 