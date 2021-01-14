SELECT directors.fname, directors.lname, movies.name, movies.year
FROM movies INNER JOIN moviesdirectors ON movies.id=moviesdirectors.movie_id
INNER JOIN directors ON directors.id=moviesdirectors.director_id
ORDER BY YEAR DESC;
