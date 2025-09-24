from flask import jsonify, url_for


class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


def generate_sitemap(app):
    links = ['/admin/']
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join(["<li><a href='" + endpoint +
                         "'>" + endpoint + "</a></li>" for endpoint in links])

    # return """
    #     <div style="text-align: center;">

    #         <img style="max-height: 80px" src='https://storage.googleapis.com/breathecode/boilerplates/rigo-baby.jpeg' />

    #         <h1>Rigo welcomes you to your API!!</h1>

    #         <p>API HOST: <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>

    #         <p>Start working on your project by following the <a href="https://start.4geeksacademy.com/starters/full-stack" target="_blank">Quick Start</a></p>

    #         <p>Remember to specify a real endpoint path like: </p>

    #         <ul style="text-align: left;">
    #             """+links_html+"""
    #         </ul>

    #     </div>
    #     """

    return """
    <style>
        body {
            background-color: black;
        }

        h1 {
            text-align: center;
            margin: 10px 30px;
        }

        .big-container {
            border: 1px solid rgb(65, 65, 65);
            margin: 40px auto 0px;
            border-radius: 10px;
            width: 35%;
            background-color: rgb(226, 226, 226);">
        }

        .small-container {
            border: 1px solid black;
            width: 60%;
            margin: 20px auto 40px;
            padding: 10px;
            border-radius: 10px;
        }

        .small-title {
            padding-top: 5px;
            margin-bottom: 5px;
            display: block;
        }

        .method {
            padding: 3px;
            border-radius: 5px;
            color: white;
            font-family: monospace;
        }

        .get {
            background-color: rgb(0, 95, 177);
        }

        .post {
            background-color: rgb(0, 117, 23);
        }

        .delete {
            background-color: rgb(182, 0, 0);
        }

        .endpoint {
            padding: 3px;
            border-radius: 5px;
            color: rgb(170, 170, 170); 
            background-color: rgb(50, 50, 50);
            font-weight: bold;
        }

        .code-snippet {
            background-color: rgb(183, 183, 183);
            padding: 5px;
            border-radius: 5px;
            font-size: smaller;
        }

    </style>
    
    <div class="big-container">

        <h1>¡Welcome to your API!</h1>
        
        <div class="small-container">

            <strong class="small-title">API host: </strong>
            <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script>

            <hr>

            <strong class="small-title">Endpoint paths:</strong>
            
            <ul>
            """ + links_html + """
            </ul>

            <hr>

            <p>Start working on your project by following the <a href="https://start.4geeksacademy.com/starters/full-stack" target="_blank">Quick Start</a></p>
            """


#             <strong class="small-title">Get all members</strong>
#             <span class="method get">GET</span> <kbd class="endpoint">/members</kbd>

#             <hr>

#             <strong class="small-title">Get one member</strong>
#             <span class="method get">GET</span> <kbd class="endpoint">/members/:id</kbd>

#             <hr>

#             <strong class="small-title">Add new member</strong>
#             <span class="method post">POST</span> <kbd class="endpoint">/members</kbd>
#             <p>Request body:</p>

#             <pre class="code-snippet">
# {
#     "first_name": "String",
#     "age": Int (positive),
#     "lucky_numbers": [Int...]
# }</pre>

#             <hr>

#             <strong class="small-title">Delete one member</strong>
#             <span class="method delete">DELETE</span> <kbd class="endpoint">/members/:id</kbd>


#         </div>


#     </div>
#         """
