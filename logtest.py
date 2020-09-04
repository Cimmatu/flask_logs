from flask import Flask, render_template

app = Flask(__name__)

f = open('/var/log/syslog')
f = list(f)
f.reverse()
    
@app.route('/')
def index():
    
    log_list = []
    
    lines = 10
    if lines>len(f):
        lines = len(f)
    
    for line in f[:lines]:
        log_list.append(line)


    return render_template('index.html', log_list=log_list)

if __name__ == '__main__':
    app.run(debug=True)
