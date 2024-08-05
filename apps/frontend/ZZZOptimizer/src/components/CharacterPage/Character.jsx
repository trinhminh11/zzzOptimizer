import React from "react";
import NavBar from "../NavBar/NavBar";
import CharacterColumns from "./CharacterColumns";
import CharacterSort from "./CharacterSort";
import "./character.css";

function Character() {
  return (
    <div className="character-container">
      <NavBar />
      <CharacterSort />
      <CharacterColumns />
    </div>
  );
}

export default Character;
