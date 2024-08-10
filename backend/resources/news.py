from flask import jsonify, make_response, request
from flask_restful import Resource

from database import db
from models import News


class NewsResource(Resource):
    def get(self):
        news_items = News.query.all()
        return make_response(jsonify([news.to_dict() for news in news_items]), 200)

    def post(self):
        data = request.form

        new_news = News(
            image_url=data.get("image_url"),
            content=data.get("content"),
            link=data.get("link"),
        )

        db.session.add(new_news)
        db.session.commit()

        return make_response(jsonify(new_news.to_dict()), 201)


class NewsById(Resource):
    def get(self, news_id):
        news_item = News.query.get(news_id)
        if news_item:
            return make_response(jsonify(news_item.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "News item not found"}), 404)

    def put(self, news_id):
        data = request.form
        news_item = News.query.get(news_id)

        if news_item:
            news_item.image_url = data.get("image_url", news_item.image_url)
            news_item.content = data.get("content", news_item.content)
            news_item.link = data.get("link", news_item.link)

            db.session.commit()

            return make_response(jsonify(news_item.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "News item not found"}), 404)

    def delete(self, news_id):
        news_item = News.query.get(news_id)

        if news_item:
            db.session.delete(news_item)
            db.session.commit()
            return make_response(
                jsonify({"message": "News item deleted successfully"}), 200
            )
        else:
            return make_response(jsonify({"error": "News item not found"}), 404)
