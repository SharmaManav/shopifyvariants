from flask import Flask, request
from processing import grab_variant

app = Flask(__name__)
app.config["DEBUG"] = True

link = ""

@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        try:
            link = request.form["url"]
        except:
            errors += "ERROR!"
        if link:
            result = grab_variant(link)
            vars_length = (len(result['product']['variants']))
            pic = (result['product']['image']['src'])
            variants_so_far = ""

            for i in range(0, int(vars_length)):
                variant = (result['product']['variants'][i]['id'])
                size = (result['product']['variants'][i]['title'])

                variants_so_far += "<p>Size {sz}: {var}</p>".format(sz=size, var=variant)

            return '''
                <html>
                    <body>
                        <p>Is that what you were looking for? </p>
                        <img src="{picture}" width="250" height="250">
                        <p>Sizes and variants are below: </p>
                        {variants_so_far}
                        <p><a href="/">Click here for another item!<a>
                    </body>
                </html>
            '''.format(variants_so_far=variants_so_far, picture=pic)


    return '''
        <html>
            <body>
                {errors}
                <p>Enter your Shopify product URL:</p>
                <form method="post" action="/">
                    <p><input name="url" /></p>
                    <p><input type="submit" value="Grab variants" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)