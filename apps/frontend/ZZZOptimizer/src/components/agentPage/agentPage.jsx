import React from "react";
import NavBar from "../NavBar/NavBar";
import AgentBody from "./agentBody";
import AgentSort from "./agentSort";
import { useState, useEffect } from "react";
import "./agent.css";

function AgentPage() {
  const [selectedOptions, setSelectedOptions] = useState({
    rank: null,
    attribute: null,
    fighting: null,
  });
  return (
    <div className="agent-page-container">
      <NavBar />
      <AgentSort
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
      <AgentBody selectedOptions={selectedOptions} />
    </div>
  );
}

export default AgentPage;
