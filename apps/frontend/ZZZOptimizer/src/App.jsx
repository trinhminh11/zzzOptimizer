import { useState } from "react";
import "./App.css";
import NavBar from "./components/NavBar/NavBar";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/HomePage/Home";
import CharacterDisplay from "./components/CharacterPage/CharacterDisplay";

function App() {
  return (
    <>
      <div>
        <Routes>
          <Route path="/deploy-github/" element={<Home />}></Route>
          <Route
            path="/deploy-github/characters"
            element={<CharacterDisplay />}
          ></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
