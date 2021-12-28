import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from PIL import Image
# import pyheif

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/convert", ConvertHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload_form.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        #convert here
        with open("uploads/" + original_fname, 'wb') as output_file:
            output_file.write(file1['body'])
        

        self.finish("file " + original_fname + " is uploaded")

class ConvertHandler(tornado.web.RequestHandler):
    def post(self):
        print(self.request)
        # file1 = self.request.files['file1'][0]
        # img = convertFile(file1)
        # self.write(img)
        # self.write(file1['body'])
        self.finish()



settings = {
# 'template_path': 'templates',
'static_path': 'static',
"xsrf_cookies": False

}

application = tornado.web.Application([
   (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/convert", ConvertHandler)
], debug=True,**settings)


def convertFile(file):
    print(file)
    # file = pyheif.read("IMG_7424.HEIC")
    # image = Image.frombytes(
    #     heif_file.mode, 
    #     heif_file.size, 
    #     heif_file.data,
    #     "raw",
    #     heif_file.mode,
    #     heif_file.stride,
    # )
print ("Server started.")
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
