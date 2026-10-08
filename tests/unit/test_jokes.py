from app.jokes import JOKES, select_joke


def test_jokes_contains_five_fixed_jokes() -> None:
    assert len(JOKES) == 5
    assert len(set(JOKES)) == 5


def test_select_joke_uses_the_fixed_jokes(monkeypatch) -> None:
    selected_jokes = []

    def choose(jokes: tuple[str, ...]) -> str:
        selected_jokes.append(jokes)
        return jokes[0]

    monkeypatch.setattr("app.jokes.random.choice", choose)

    assert select_joke() == JOKES[0]
    assert selected_jokes == [JOKES]