import { useState } from "react";
import "./App.css";
import NavBar from "./components/NavBar/NavBar";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./components/HomePage/Home";
import Character from "./components/CharacterPage/Character";

function App() {
  return (
    <>
      <div>
        <Routes>
          <Route path="/deploy-github/" element={<Home />}></Route>
          <Route
            path="/deploy-github/characters"
            element={<Character />}
          ></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
