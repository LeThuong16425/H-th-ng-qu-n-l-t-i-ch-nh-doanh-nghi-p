from models.news_model import NewsModel

class NewsController:
    @staticmethod
    def get_all_news():
        return NewsModel.get_news()  # Fetch all news from the model
