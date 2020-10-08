from django import forms


class ArtistForm(forms.Form):
    artist_name = forms.CharField(label='artist_name:', max_length=100)
