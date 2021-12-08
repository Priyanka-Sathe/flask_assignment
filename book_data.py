from flask import Flask, request
from flask import render_template
from util import util
from util import config as cfg
from flask import g
import time

app = Flask(__name__,template_folder='templates')


#before_request and teardown_request logging time taken by request.
@app.before_request
def before_request():
    g.start_time = time.time()
    
#subject_query function queries input data based on given subject
@app.route('/api/book/subject', methods=['GET'])
def subject_query():
    #Retrieve Subject
    subject = request.args['args']
    
    df = util.extract_csv()
    col_list = util.query_df(df,cfg.SUBJECT,subject)
    
    return render_template("result.html", df=df, col_list = col_list,
                            qtype=cfg.SUBJECT, arg1=subject)
                            
@app.teardown_request
def teardown_request(exception=None):
    time_taken = time.time() - g.start_time
    print(time_taken)
    
#published_year_query function queries input data based on input Year
@app.route('/api/book/YearPublished', methods=['GET'])
def published_year_query():
     #Retrieve Subject
    year = request.args['args']
    year = int(year)
    
    df = util.extract_csv()
    col_list = util.query_df(df,cfg.YEAR,year)

    return render_template("result.html", df=df, col_list = col_list,
                            qtype=cfg.YEAR, arg1=year)

#title_query function queries input data based on Tile or name of book
@app.route('/api/book/name', methods=['GET'])
def title_query():

    title = request.args['args']
    
    df = util.extract_csv()
    
    col_list = util.query_df(df,cfg.TITLE,title)

    return render_template("result.html", df=df, col_list = col_list,
                            qtype=cfg.TITLE, arg1=title)
    
#author_query function queries input data based on Author of book
@app.route('/api/book/author', methods=['GET'])
def author_query():

    author = request.args['args']
    
    df = util.extract_csv()
    
    col_list = util.query_df(df,cfg.AUTHOR,author)
    
    return render_template("result.html", df=df, col_list = col_list,
                            qtype=cfg.AUTHOR, arg1=author)


if __name__ == '__main__':

    app.run(debug=True,threaded=True)