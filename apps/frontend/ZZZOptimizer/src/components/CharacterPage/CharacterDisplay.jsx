import React from "react";
import NavBar from "../NavBar/NavBar";
import CharacterColumns from "./CharacterColumns";
import CharacterSort from "./CharacterSort";
import "./character.css";
import Test from "./Test";
import CharacterInfo from "../../../../../backend/components/CharacterInfo";

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
