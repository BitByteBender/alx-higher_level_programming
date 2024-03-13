-- database dump from hbtn_0d_tvshows
SELECT tv_genres.name As genre, count(tv_show_genres.show_id) As number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
