import React from "react";
import CharacterLeftColumn from "./CharacterLeftColumn";
import CharacterMainColumn from "./CharacterMainColumn";
import CharacterInfo from "../../../../../backend/components/CharacterInfo";
import "./character.css";

function CharacterColumns() {
  return (
    <div className="row character-columns-holder">
      <div className="col-lg-3">
        <CharacterInfo />
      </div>
      <div className="col-lg-9">
        <CharacterMainColumn />
      </div>
    </div>
  );
}

export default CharacterColumns;
