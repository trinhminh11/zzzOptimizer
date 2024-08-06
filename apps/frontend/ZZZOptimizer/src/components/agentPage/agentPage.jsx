import React from "react";
import NavBar from "../NavBar/NavBar";
import AgentBody from "./agentBody";
import AgentSort from "./agentSort";
import "./agent.css";

function agentPage() {
  return (
    <div className="agent-page-container">
      <NavBar />
      <AgentSort />
      <AgentBody />
    </div>
  );
}

export default agentPage;
