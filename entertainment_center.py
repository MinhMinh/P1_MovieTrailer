import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13""/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

interstellar = media.Movie(
    "Interstellar",
    "A man and his crew take a mission to save human life.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
)

moives = [toy_story, avatar, interstellar]
fresh_tomatoes.open_movies_page(moives)
