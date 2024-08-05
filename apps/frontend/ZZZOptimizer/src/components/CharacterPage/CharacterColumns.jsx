import React from "react";
import CharacterLeftColumn from "./CharacterLeftColumn";
import CharacterMainColumn from "./CharacterMainColumn";

function CharacterColumns() {
  return (
    <div className="row">
      <div className="col-lg-4">
        <CharacterLeftColumn />
      </div>
      <div className="col-lg-8">
        <CharacterMainColumn />
      </div>
    </div>
  );
}

export default CharacterColumns;
