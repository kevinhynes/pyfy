def test_save_album(spotify_user_auth, nothing_was_the_same_album_id):
    assert spotify_user_auth.save_albums(nothing_was_the_same_album_id) is not None

def test_save_albums(spotify_user_auth, scorpion_album_id, nothing_was_the_same_album_id):
    assert spotify_user_auth.save_albums([scorpion_album_id, nothing_was_the_same_album_id]) is not None

def test_owns_album(spotify_user_auth, scorpion_album_id):
    assert spotify_user_auth.owns_albums(scorpion_album_id)

def test_owns_albums(spotify_user_auth, scorpion_album_id, nothing_was_the_same_album_id):
    assert spotify_user_auth.owns_albums([scorpion_album_id, nothing_was_the_same_album_id])

def test_delete_album(spotify_user_auth, scorpion_album_id):
    assert spotify_user_auth.delete_albums(scorpion_album_id) is not None

def test_delete_albums(spotify_user_auth, scorpion_album_id, nothing_was_the_same_album_id):
    assert spotify_user_auth.delete_albums([scorpion_album_id, nothing_was_the_same_album_id]) is not None

def test_album(spotify_user_auth, reise_reise_album_id, ritual_spirit_album_id):
    assert spotify_user_auth.albums(album_ids=[reise_reise_album_id, ritual_spirit_album_id])

def test_albums(spotify_user_auth, reise_reise_album_id):
    assert spotify_user_auth.albums(reise_reise_album_id)
