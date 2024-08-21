import React, { useState } from "react";
import WEngineBody from "./WEngineBody";
import "./wEngine.css";
import NavBar from "../NavBar/NavBar";
import WEngineSort from "./WEngineSort";

function WEnginePage() {
  const [selectedOptions, setSelectedOptions] = useState({
    rank: null,
    specialty: null,
  });
  return (
    <div className="wEngine-page-container">
      <NavBar />
      <WEngineSort
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
      <WEngineBody
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
    </div>
  );
}

export default WEnginePage;
