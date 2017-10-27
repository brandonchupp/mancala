from context import Mancala

game = Mancala.Mancala()

def test_make_new_game():
    assert game.p1_pits == [4, 4, 4, 4, 4, 4]
    assert game.p2_pits == [4, 4, 4, 4, 4, 4]
    assert game.p1_store == 0
    assert game.p2_store == 0