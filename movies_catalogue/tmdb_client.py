
import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZGY1ZjU5ZGZjNzk1ZjgxNmUxYzM0NmFjYjZiNjVkNiIsIm5iZiI6MTc1MjU5Nzk4MS41LCJzdWIiOiI2ODc2ODVkZDdjYzI4MmQwODQ3MzMzODMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.HMc5GqxsiBbX3uBX_IqCvEQoKPqgvrl3d5rEEXSEKlY"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])  





