from app.jokes import CATEGORIES, JOKES, select_joke


def test_jokes_contains_ten_unique_jokes_per_category() -> None:
    assert CATEGORIES == ("classic", "programming", "school")
    assert set(JOKES) == set(CATEGORIES)
    assert all(len(jokes) == 10 for jokes in JOKES.values())
    assert all(len(set(jokes)) == 10 for jokes in JOKES.values())


def test_select_joke_uses_the_fixed_jokes(monkeypatch) -> None:
    selected_jokes = []

    def choose(jokes: tuple[str, ...]) -> str:
        selected_jokes.append(jokes)
        return jokes[0]

    monkeypatch.setattr("app.jokes.random.choice", choose)

    assert select_joke("programming") == ("programming", JOKES["programming"][0])
    assert selected_jokes == [JOKES["programming"]]


def test_select_joke_without_category_uses_all_jokes(monkeypatch) -> None:
    selected_jokes = []

    def choose(jokes: tuple[str, ...]) -> str:
        selected_jokes.append(jokes)
        return jokes[0]

    monkeypatch.setattr("app.jokes.random.choice", choose)

    assert select_joke() == ("classic", JOKES["classic"][0])
    assert selected_jokes == [
        ("classic", "programming", "school"),
        JOKES["classic"],
    ]