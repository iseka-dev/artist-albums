import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
from .forms import ArtistForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_discography(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            client_id = '46b9c72dfda645c78b170f3cfb0e6068'
            client_secret = 'b7de73060ce74465983df1debcf593d3'
            client_credentials_manager = SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )
            sp = spotipy.Spotify(
                client_credentials_manager=client_credentials_manager
            )

            name = form.cleaned_data['artist_name']
            result = sp.search(name)
            # Extract Artist's uri
            artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
            artist_uri
            # Pull all of the artist's albums
            sp_albums = sp.artist_albums(artist_uri, album_type='album')

            # Store artist's albums' names' and uris in separate lists
            album_names = []
            album_uris = []
            for i in range(len(sp_albums['items'])):
                album_names.append(sp_albums['items'][i]['name'])
                album_uris.append(sp_albums['items'][i]['uri'])

            album_names
            album_uris

            context = {
                'albums_list': album_names,
                'form': form,
            }
            return render(request, 'albums/index.html', context)
    else:
        form = ArtistForm()
        form = ArtistForm(request.POST)
        return render(request, 'albums/index.html', {'form': form})
