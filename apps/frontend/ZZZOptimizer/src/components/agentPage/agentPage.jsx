import React from "react";
import NavBar from "../NavBar/NavBar";
import AgentBody from "./AgentBody";
import AgentSort from "./AgentSort";
import "./agent.css";

function AgentPage() {
  return (
    <div className="agent-page-container">
      <NavBar />
      <AgentSort />
      <AgentBody />
    </div>
  );
}

export default AgentPage;
