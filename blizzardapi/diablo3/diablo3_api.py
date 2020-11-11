from .diablo3_community_api import Diablo3CommunityApi
from .diablo3_game_data_api import Diablo3GameDataApi


class Diablo3Api:
    """Diablo3 API class.

    Attributes:
        client_id: A client id supplied by Blizzard.
        client_secret: A client secret supplied by Blizzard.
    """

    def __init__(self, client_id, client_secret):
        """Inits Diablo3Api"""
        self.community = Diablo3CommunityApi(client_id, client_secret)
        self.game_data = Diablo3GameDataApi(client_id, client_secret)
