from flask import Flask, render_template, request
from flask_elasticsearch import FlaskElasticsearch

app = Flask(__name__)
app.config.from_object('config.Config')
es = FlaskElasticsearch(app)

@app.route('/')
def show_entries():
    query =  {
        "size" : 100,
        "query": {
            "query_string": {
                "default_field" : "_all",
                "query" : "education OR healthcare OR architecture OR \"artificial intelligence\" OR \"deep learning\" OR \"natural language programming\" OR \"elastic search\" OR .net OR react OR remote OR python OR js OR javascript OR startup OR stakeholders OR learn OR education OR krakow OR bournemouth OR neo4j OR web OR scraping OR api OR maps OR nlp"
            }
        }
    }
    result = es.search(index="jobs", body=query)
    return render_template('index.html', results=result['hits']['hits'])

@app.route('/rate')
def rate():
    id = request.args.get('id')
    rating = request.args.get('rating')
    body = {
        "doc" : {
            "rating" : rating
        }
    }
    # es.update(index="jobs", doc_type='listing', id=id, body=body, refresh=True)
    return show_entries()

@app.route('/comment')
def comment():
    id = request.args.get('id')
    comment = request.args.get('comment')
    body = {
        "doc" : {
            "comment" : rating
        }
    }
    # es.update(index="jobs", doc_type='listing', id=id, body=body, refresh=True)
    return show_entries()