import React from "react";
import WEngineBody from "./WEngineBody";
import "./wEngine.css";
import NavBar from "../NavBar/NavBar";
import WEngineSort from "./WEngineSort";

function WEnginePage() {
  return (
    <div className="wEngine-page-container">
      <NavBar />
      <WEngineSort />
      <WEngineBody />
    </div>
  );
}

export default WEnginePage;
