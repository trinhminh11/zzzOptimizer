import React from "react";
import NavBar from "../NavBar/NavBar";
import AgentBody from "./agentBody";
import AgentSelect from "./agentSelect";
import { useState, useEffect } from "react";
import "./agent.css";

function AgentPage() {
  const [selectedOptions, setSelectedOptions] = useState({
    rank: null,
    attribute: null,
    specialty: null,
  });

  return (
    <div className="agent-page-container">
      <NavBar />
      <AgentSelect
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
      <AgentBody
        selectedOptions={selectedOptions}
        setSelectedOptions={setSelectedOptions}
      />
    </div>
  );
}

export default AgentPage;
