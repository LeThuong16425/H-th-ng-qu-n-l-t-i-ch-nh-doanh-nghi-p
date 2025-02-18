from models.news_model import NewsModel

class NewsController:
    @staticmethod
    def get_all_news():
        return NewsModel.get_news()  # Fetch all news from the model

    @staticmethod
    def add_news(title, content):
        return NewsModel.insert_news(title, content)  # Add news to the database
