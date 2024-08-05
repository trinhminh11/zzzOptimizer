import React from "react";
import CharacterLeftColumn from "./CharacterLeftColumn";
import CharacterMainColumn from "./CharacterMainColumn";
import "./character.css";

function CharacterColumns() {
  return (
    <div className="row character-columns-holder">
      <div className="col-lg-3">
        <CharacterLeftColumn />
      </div>
      <div className="col-lg-9">
        <CharacterMainColumn />
      </div>
    </div>
  );
}

export default CharacterColumns;
