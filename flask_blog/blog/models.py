from flask_blog import db, uploaded_images
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer,db.ForeignKey('author.id'))
    posts = db.relationship("Post", backref='blog', lazy='dynamic')
    
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        
    def __repr__(self):
        return "<Blog {}>".format(self.name)
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    image =db.Column(db.String(255))
    slug = db.Column(db.String(256), unique=True)
    # so slug is a string composed of date blog is published and the page name.
    # so slug kinda gives each blog post its own url
    publish_date= db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    # It is usally not a good practice to delete entries from DB
    # so what we do is set live to false which means it will not be visible
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))
    # we are establishing a relationship between catergory and posts
    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)
    
    def __init__(self, blog, author, title, body, category, image=None, slug=None, publish_date=None, live=True):
        self.blog_id = blog.id
        self.author_id = author.id
        self.category_id=category.id
        self.image = image
        self.title =title
        self.body =body
        self.slug = slug
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        self.live = live
    
    def __repr__(self):
        return "<Post > {}".format(self.title)
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
   
    
    def __init__(self,name):
        self.name=name
        
    def __repr__(self):
        return "{}".format(self.name)
    