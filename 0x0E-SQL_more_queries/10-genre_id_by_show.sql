-- script that lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked. Each record should display: tv_shows.title -
-- tv_show_genres.genre_id. Results must be sorted in ascending order by
-- tv_shows.title and tv_show_genres.genre_id. You can use only one SELECT
-- statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
LEFT JOIN genre_id ON tv_shows.title = tv_show_genres.genre_id
ORDER BY tv_shows.title and tv_show_genres.genre_id ASC
