
from flask import Flask, jsonify, request, render_template
from rk_yt_dl import rk_downloader

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		data = "HARE KRSNA  || RADHE RAHDE"
		return jsonify({'data': data})

@app.route('/admin', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/yt-api', methods = ['POST'])
def disp():
	print(request.json['url'])
	rk_data = rk_downloader(request.json['url'])
	return jsonify(rk_data)


if __name__ == '__main__':
	app.run(debug = True)

