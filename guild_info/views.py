import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class PlayerSearchInfo(APIView):
    def get(self, request, *args, **kwargs):
        def get_player_id():
            player_name = kwargs.get('player_name')

            if not player_name:
                return Response({'error': 'Player Name is required'}, status=400)

            player_name_url = f"https://gameinfo.albiononline.com/api/gameinfo/search?q={player_name}"

            # Make the API call
            response = requests.get(player_name_url)

            # Process the response
            data = response.json() if response.status_code == 200 else {}
            return data['players'][0]['Id']
        
        player_id = get_player_id()

        if not player_id:
            return Response({'error': 'Player Not Found'}, status=400)

        player_id = f"https://gameinfo.albiononline.com/api/gameinfo/players/{player_id}"

        # Make the API call
        response = requests.get(player_id)

        # Process the response
        data = response.json() if response.status_code == 200 else {}
        return Response(data)
    
class Top5MemberInfo(APIView):
    def get(self, request, *args, **kwargs):
        guild_id = "QLY0eIvEQNa3WJZ_tndijg"
        url = f"https://gameinfo.albiononline.com/api/gameinfo/guilds/{guild_id}/data"

        # Make the API call
        response = requests.get(url)

        # Process the response
        data = response.json() if response.status_code == 200 else {}
        return Response(data)