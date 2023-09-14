// src/components/MovieList.js

import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [movies, setMovies] = useState([]);
  const [genreFilter, setGenreFilter] = useState("");
  const [titleFilter, setTitleFilter] = useState("");

  const url = "http://127.0.0.1:8000/movies/";
  useEffect(() => {
    // Fetch movies from your Django API
    axios
      .get(url)
      .then((response) => setMovies(response.data))
      .catch((error) => console.error(error));
  }, []);

  const filteredMovies = movies
    .filter(
      (movie) =>
        !genreFilter || movie.genres.some((genre) => genre.name === genreFilter)
    )
    .filter(
      (movie) =>
        !titleFilter ||
        movie.title.toLowerCase().includes(titleFilter.toLowerCase())
    );

  return (
    <div>
      <input
        type="text"
        placeholder="Search by Title"
        value={titleFilter}
        onChange={(e) => setTitleFilter(e.target.value)}
      />
      <select
        value={genreFilter}
        onChange={(e) => setGenreFilter(e.target.value)}
      >
        <option value="">All Genres</option>
        {/* Populate genre options */}
      </select>
      <ul>
        {filteredMovies.map((movie) => (
          <li key={movie.id}>
            <h3>{movie.title}</h3>

            <p>
              Genre(s): {movie.genres.map((genre) => genre.name).join(", ")}
            </p>
            <p>Rating: {movie.rating}</p>
            <p>Year Release: {movie.year_release}</p>
            <p>Metacritic Rating: {movie.metacritic_rating}</p>
            <p>Runtime: {movie.runtime} minutes</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
